"""
Isolation Manager for Security Testing

This module provides containerized isolation environment management for security testing,
ensuring tests run in completely isolated environments without affecting production systems.
"""

import json
import os
import shutil
import tempfile
import threading
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from subprocess import PIPE, STDOUT, Popen
from typing import Any, Dict, List, Optional, Union

from .types import IsolationEnvironment, SecurityConfig


@dataclass
class ContainerConfig:
    """Configuration for containerized isolation environment."""

    image: str = "python:3.9-slim"
    memory_limit: str = "512m"
    cpu_limit: float = 1.0
    network_isolated: bool = True
    volume_mounts: Dict[str, str] = field(default_factory=dict)
    environment_vars: Dict[str, str] = field(default_factory=dict)
    timeout: int = 300


class IsolationManager:
    """
    Manager for creating and maintaining isolated testing environments.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the isolation manager.

        Args:
            config: Configuration dictionary for isolation parameters
        """
        self.config = config or {}
        self.environments: Dict[str, IsolationEnvironment] = {}
        self.active_containers: Dict[str, str] = {}  # container_id -> environment_id

        # Configuration parameters
        self.default_timeout = self.config.get("isolation_timeout", 300)
        self.max_concurrent_environments = self.config.get(
            "max_concurrent_environments", 5
        )
        self.cleanup_interval = self.config.get("cleanup_interval", 60)
        self.enable_docker = self.config.get("enable_docker", True)

        # Threading for cleanup
        self._cleanup_thread = None
        self._stop_cleanup = threading.Event()

        # Initialize cleanup thread
        self.start_cleanup_thread()

    def create_environment(
        self,
        env_type: str = "security_test",
        container_config: Optional[ContainerConfig] = None,
    ) -> IsolationEnvironment:
        """
        Create a new isolated testing environment.

        Args:
            env_type: Type of environment to create
            container_config: Container configuration

        Returns:
            IsolationEnvironment: Created environment information
        """
        if len(self.environments) >= self.max_concurrent_environments:
            raise RuntimeError(
                f"Maximum concurrent environments ({self.max_concurrent_environments}) reached"
            )

        # Generate unique environment ID
        env_id = f"env_{uuid.uuid4().hex[:8]}"

        # Use default container config if not provided
        if container_config is None:
            container_config = ContainerConfig()

        try:
            if self.enable_docker:
                container_id = self._create_docker_container(env_id, container_config)
            else:
                container_id = self._create_process_isolation(env_id, container_config)

            environment = IsolationEnvironment(
                container_id=container_id,
                environment_type=env_type,
                network_isolated=container_config.network_isolated,
                resource_limits={
                    "memory": container_config.memory_limit,
                    "cpu": container_config.cpu_limit,
                },
                status="running",
                created_at=datetime.now(),
            )

            self.environments[env_id] = environment
            self.active_containers[container_id] = env_id

            return environment

        except Exception as e:
            raise RuntimeError(f"Failed to create isolation environment: {str(e)}")

    def _create_docker_container(self, env_id: str, config: ContainerConfig) -> str:
        """
        Create a Docker container for isolation.

        Args:
            env_id: Environment ID
            config: Container configuration

        Returns:
            str: Docker container ID
        """
        # Build Docker command
        docker_cmd = [
            "docker",
            "run",
            "-d",
            "--name",
            f"sec_test_{env_id}",
            "--memory",
            config.memory_limit,
            "--cpus",
            str(config.cpu_limit),
        ]

        # Add network isolation if requested
        if config.network_isolated:
            docker_cmd.extend(["--network", "none"])

        # Add volume mounts
        for host_path, container_path in config.volume_mounts.items():
            docker_cmd.extend(["-v", f"{host_path}:{container_path}"])

        # Add environment variables
        for key, value in config.environment_vars.items():
            docker_cmd.extend(["-e", f"{key}={value}"])

        # Add timeout handling
        docker_cmd.extend(["--timeout", str(config.timeout)])

        # Add image and command
        docker_cmd.extend(
            [config.image, "tail", "-f", "/dev/null"]
        )  # Keep container running

        # Execute Docker command
        try:
            result = self._execute_command(docker_cmd)
            if result["returncode"] == 0:
                return result["stdout"].strip()
            else:
                raise RuntimeError(f"Docker command failed: {result['stderr']}")
        except FileNotFoundError:
            raise RuntimeError(
                "Docker not found. Please install Docker or disable Docker isolation."
            )

    def _create_process_isolation(self, env_id: str, config: ContainerConfig) -> str:
        """
        Create process-based isolation (fallback when Docker is not available).

        Args:
            env_id: Environment ID
            config: Container configuration

        Returns:
            str: Process ID as container ID
        """
        # Create temporary directory for the isolated environment
        temp_dir = tempfile.mkdtemp(prefix=f"sec_test_{env_id}_")

        # Create a simple Python script that maintains isolation
        script_content = f'''
import os
import sys
import time
import signal
import threading

def isolated_worker():
    """Isolated worker process."""
    # Set up isolated environment
    os.chdir("{temp_dir}")

    # Override environment variables for isolation
    isolated_env = {{
        "PATH": "/usr/bin:/bin",
        "PYTHONPATH": "",
        "SECURITY_TEST_ENV": "{env_id}",
        **{json.dumps(config.environment_vars)}
    }}

    # Update environment
    os.environ.update(isolated_env)

    # Signal handler for graceful shutdown
    shutdown_event = threading.Event()

    def signal_handler(signum, frame):
        shutdown_event.set()

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # Keep process alive until signaled
    while not shutdown_event.is_set():
        time.sleep(1)

    # Cleanup
    import shutil
    shutil.rmtree("{temp_dir}", ignore_errors=True)
    sys.exit(0)

if __name__ == "__main__":
    isolated_worker()
'''

        # Write script to temporary file
        script_path = os.path.join(temp_dir, "isolation_script.py")
        with open(script_path, "w") as f:
            f.write(script_content)

        # Start isolated process
        process = Popen(
            [sys.executable, script_path],
            stdout=PIPE,
            stderr=PIPE,
            env={**os.environ, **config.environment_vars},
        )

        return str(process.pid)

    def execute_in_environment(
        self, env_id: str, command: Union[str, List[str]], timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Execute a command within an isolated environment.

        Args:
            env_id: Environment ID
            command: Command to execute (string or list)
            timeout: Execution timeout in seconds

        Returns:
            Dict: Command execution result
        """
        if env_id not in self.environments:
            raise ValueError(f"Environment {env_id} not found")

        environment = self.environments[env_id]
        if environment.status != "running":
            raise RuntimeError(f"Environment {env_id} is not running")

        if timeout is None:
            timeout = self.default_timeout

        try:
            if self.enable_docker:
                return self._execute_docker_command(
                    environment.container_id, command, timeout
                )
            else:
                return self._execute_process_command(
                    environment.container_id, command, timeout
                )
        except Exception as e:
            return {
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "timed_out": False,
            }

    def _execute_docker_command(
        self, container_id: str, command: Union[str, List[str]], timeout: int
    ) -> Dict[str, Any]:
        """Execute command in Docker container."""
        if isinstance(command, str):
            command = ["sh", "-c", command]

        docker_cmd = ["docker", "exec", container_id] + command

        result = self._execute_command(docker_cmd, timeout=timeout)
        return {
            "returncode": result["returncode"],
            "stdout": result["stdout"],
            "stderr": result["stderr"],
            "timed_out": result.get("timed_out", False),
        }

    def _execute_process_command(
        self, process_id: str, command: Union[str, List[str]], timeout: int
    ) -> Dict[str, Any]:
        """Execute command in isolated process (simplified)."""
        # This is a simplified implementation for process-based isolation
        # In a real implementation, you'd need more sophisticated IPC

        if isinstance(command, str):
            command = ["sh", "-c", command]

        try:
            result = self._execute_command(command, timeout=timeout)
            return {
                "returncode": result["returncode"],
                "stdout": result["stdout"],
                "stderr": result["stderr"],
                "timed_out": result.get("timed_out", False),
            }
        except Exception as e:
            return {
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "timed_out": False,
            }

    def _execute_command(self, command: List[str], timeout: int = 30) -> Dict[str, Any]:
        """Execute a command with timeout."""
        try:
            process = Popen(
                command, stdout=PIPE, stderr=PIPE, stdin=PIPE, universal_newlines=True
            )

            stdout, stderr = process.communicate(timeout=timeout)

            return {
                "returncode": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "timed_out": False,
            }

        except Exception as e:
            # Terminate the process on timeout or other errors
            process.terminate()
            try:
                process.wait(timeout=5)
            except:
                process.kill()

            return {
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "timed_out": isinstance(e, TimeoutError),
            }

    def reset_environment(self, env_id: str) -> bool:
        """
        Reset an isolated environment to clean state.

        Args:
            env_id: Environment ID to reset

        Returns:
            bool: True if reset was successful
        """
        if env_id not in self.environments:
            return False

        environment = self.environments[env_id]

        try:
            # Stop and remove current container
            self._destroy_container(environment.container_id)

            # Create new container with same configuration
            container_config = ContainerConfig(
                network_isolated=environment.network_isolated,
                memory_limit=environment.resource_limits.get("memory", "512m"),
                cpu_limit=environment.resource_limits.get("cpu", 1.0),
            )

            if self.enable_docker:
                new_container_id = self._create_docker_container(
                    env_id, container_config
                )
            else:
                new_container_id = self._create_process_isolation(
                    env_id, container_config
                )

            # Update environment
            environment.container_id = new_container_id
            environment.status = "running"
            environment.last_reset = datetime.now()

            # Update active containers mapping
            if environment.container_id in self.active_containers:
                del self.active_containers[environment.container_id]
            self.active_containers[new_container_id] = env_id

            return True

        except Exception as e:
            environment.status = "error"
            return False

    def destroy_environment(self, env_id: str) -> bool:
        """
        Destroy an isolated environment.

        Args:
            env_id: Environment ID to destroy

        Returns:
            bool: True if destruction was successful
        """
        if env_id not in self.environments:
            return False

        environment = self.environments[env_id]

        try:
            # Destroy container
            self._destroy_container(environment.container_id)

            # Remove from tracking
            del self.environments[env_id]
            if environment.container_id in self.active_containers:
                del self.active_containers[environment.container_id]

            return True

        except Exception:
            return False

    def _destroy_container(self, container_id: str):
        """Destroy a container by ID."""
        if self.enable_docker:
            # Stop and remove Docker container
            self._execute_command(["docker", "stop", container_id])
            self._execute_command(["docker", "rm", container_id])
        else:
            # Terminate process
            try:
                import signal

                os.kill(int(container_id), signal.SIGTERM)
            except:
                pass

    def get_environment_status(self, env_id: str) -> Optional[Dict[str, Any]]:
        """
        Get status information for an environment.

        Args:
            env_id: Environment ID

        Returns:
            Dict: Environment status information or None if not found
        """
        if env_id not in self.environments:
            return None

        environment = self.environments[env_id]

        # Check container health
        try:
            if self.enable_docker:
                result = self._execute_command(
                    [
                        "docker",
                        "inspect",
                        "--format",
                        "{{.State.Status}}",
                        environment.container_id,
                    ]
                )
                if result["returncode"] == 0:
                    container_status = result["stdout"].strip()
                    environment.status = container_status
            else:
                # For process isolation, check if process is still running
                try:
                    import signal

                    os.kill(int(environment.container_id), 0)  # Check if process exists
                    environment.status = "running"
                except:
                    environment.status = "stopped"
        except:
            environment.status = "unknown"

        return {
            "environment_id": env_id,
            "container_id": environment.container_id,
            "status": environment.status,
            "environment_type": environment.environment_type,
            "network_isolated": environment.network_isolated,
            "resource_limits": environment.resource_limits,
            "created_at": environment.created_at.isoformat(),
            "last_reset": (
                environment.last_reset.isoformat() if environment.last_reset else None
            ),
            "uptime_seconds": (datetime.now() - environment.created_at).total_seconds(),
        }

    def list_environments(self) -> List[Dict[str, Any]]:
        """
        List all active environments.

        Returns:
            List[Dict]: List of environment information
        """
        environments = []
        for env_id in self.environments:
            env_info = self.get_environment_status(env_id)
            if env_info:
                environments.append(env_info)
        return environments

    def start_cleanup_thread(self):
        """Start the background cleanup thread."""
        if self._cleanup_thread is None or not self._cleanup_thread.is_alive():
            self._stop_cleanup.clear()
            self._cleanup_thread = threading.Thread(
                target=self._cleanup_loop, daemon=True, name="IsolationCleanup"
            )
            self._cleanup_thread.start()

    def stop_cleanup_thread(self):
        """Stop the background cleanup thread."""
        if self._cleanup_thread and self._cleanup_thread.is_alive():
            self._stop_cleanup.set()
            self._cleanup_thread.join(timeout=5.0)

    def _cleanup_loop(self):
        """Background cleanup loop."""
        while not self._stop_cleanup.is_set():
            try:
                self._cleanup_stale_environments()
                time.sleep(self.cleanup_interval)
            except Exception as e:
                print(f"Cleanup error: {e}")

    def _cleanup_stale_environments(self):
        """Clean up stale environments."""
        current_time = datetime.now()
        stale_threshold = timedelta(hours=1)  # Environments older than 1 hour

        environments_to_remove = []
        for env_id, environment in self.environments.items():
            if current_time - environment.created_at > stale_threshold:
                environments_to_remove.append(env_id)

        for env_id in environments_to_remove:
            try:
                self.destroy_environment(env_id)
            except Exception as e:
                print(f"Failed to cleanup environment {env_id}: {e}")

    def __del__(self):
        """Cleanup when isolation manager is destroyed."""
        # Destroy all environments
        for env_id in list(self.environments.keys()):
            try:
                self.destroy_environment(env_id)
            except:
                pass

        # Stop cleanup thread
        self.stop_cleanup_thread()
