"""
Test cases for Isolation Manager

This module contains comprehensive test cases for the isolation manager,
following TDD principles with test cases written before implementation.
"""

import pytest
import time
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from src.security.isolation_manager import IsolationManager, ContainerConfig
from src.security.types import IsolationEnvironment


class TestIsolationManager:
    """Test cases for IsolationManager class"""

    def setup_method(self):
        """Setup test fixtures"""
        # Mock Docker for testing
        self.docker_patcher = patch('subprocess.Popen')
        self.mock_popen = self.docker_patcher.start()

        # Configure mock process
        self.mock_process = Mock()
        self.mock_process.returncode = 0
        self.mock_process.communicate.return_value = ("container123", "")
        self.mock_popen.return_value = self.mock_process

        self.manager = IsolationManager({'enable_docker': True})

    def teardown_method(self):
        """Cleanup test fixtures"""
        self.docker_patcher.stop()
        if hasattr(self.manager, 'stop_cleanup_thread'):
            self.manager.stop_cleanup_thread()

    def test_manager_initialization(self):
        """Test isolation manager initializes correctly"""
        assert self.manager is not None
        assert hasattr(self.manager, 'create_environment')
        assert hasattr(self.manager, 'execute_in_environment')
        assert hasattr(self.manager, 'reset_environment')
        assert hasattr(self.manager, 'destroy_environment')
        assert self.manager.enable_docker is True

    def test_create_environment_success(self):
        """Test successful environment creation"""
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("container123", "")
        self.mock_popen.return_value = mock_process

        config = ContainerConfig(image="python:3.9-slim")
        environment = self.manager.create_environment("test_type", config)

        assert isinstance(environment, IsolationEnvironment)
        assert environment.environment_type == "test_type"
        assert environment.container_id == "container123"
        assert environment.network_isolated is True
        assert environment.status == "running"
        assert isinstance(environment.created_at, datetime)

    def test_create_environment_max_concurrent_limit(self):
        """Test maximum concurrent environments limit"""
        # Fill up environments to max limit
        self.manager.max_concurrent_environments = 1
        self.manager.environments["existing_env"] = IsolationEnvironment(
            container_id="existing123",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=datetime.now()
        )

        config = ContainerConfig()
        with pytest.raises(RuntimeError, match="Maximum concurrent environments"):
            self.manager.create_environment("test_type", config)

    def test_execute_in_environment_success(self):
        """Test successful command execution in environment"""
        # Setup environment
        self.manager.environments["test_env"] = IsolationEnvironment(
            container_id="test_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=datetime.now()
        )

        # Mock successful command execution
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("success output", "")
        self.mock_popen.return_value = mock_process

        result = self.manager.execute_in_environment("test_env", ["echo", "hello"])

        assert result['returncode'] == 0
        assert result['stdout'] == "success output"
        assert result['stderr'] == ""
        assert result['timed_out'] is False

    def test_execute_in_environment_not_found(self):
        """Test command execution in non-existent environment"""
        with pytest.raises(ValueError, match="Environment nonexistent not found"):
            self.manager.execute_in_environment("nonexistent", ["echo", "hello"])

    def test_execute_in_environment_not_running(self):
        """Test command execution in stopped environment"""
        # Setup stopped environment
        self.manager.environments["stopped_env"] = IsolationEnvironment(
            container_id="stopped_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="stopped",
            created_at=datetime.now()
        )

        with pytest.raises(RuntimeError, match="Environment stopped_env is not running"):
            self.manager.execute_in_environment("stopped_env", ["echo", "hello"])

    def test_reset_environment_success(self):
        """Test successful environment reset"""
        # Setup environment
        original_time = datetime.now()
        self.manager.environments["reset_env"] = IsolationEnvironment(
            container_id="original_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=original_time
        )

        # Mock container operations
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("new_container456", "")
        self.mock_popen.return_value = mock_process

        result = self.manager.reset_environment("reset_env")

        assert result is True
        environment = self.manager.environments["reset_env"]
        assert environment.container_id == "new_container456"
        assert environment.status == "running"
        assert environment.last_reset is not None
        assert environment.last_reset > original_time

    def test_reset_environment_not_found(self):
        """Test reset of non-existent environment"""
        result = self.manager.reset_environment("nonexistent")
        assert result is False

    def test_destroy_environment_success(self):
        """Test successful environment destruction"""
        # Setup environment
        self.manager.environments["destroy_env"] = IsolationEnvironment(
            container_id="destroy_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=datetime.now()
        )
        self.manager.active_containers["destroy_container"] = "destroy_env"

        # Mock successful destruction
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("", "")
        self.mock_popen.return_value = mock_process

        result = self.manager.destroy_environment("destroy_env")

        assert result is True
        assert "destroy_env" not in self.manager.environments
        assert "destroy_container" not in self.manager.active_containers

    def test_destroy_environment_not_found(self):
        """Test destruction of non-existent environment"""
        result = self.manager.destroy_environment("nonexistent")
        assert result is False

    def test_get_environment_status_success(self):
        """Test successful environment status retrieval"""
        # Setup environment
        env = IsolationEnvironment(
            container_id="status_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={'memory': '512m', 'cpu': 1.0},
            status="running",
            created_at=datetime.now()
        )
        self.manager.environments["status_env"] = env

        # Mock Docker inspect command
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("running", "")
        self.mock_popen.return_value = mock_process

        status = self.manager.get_environment_status("status_env")

        assert status is not None
        assert status['environment_id'] == "status_env"
        assert status['container_id'] == "status_container"
        assert status['status'] == "running"
        assert status['environment_type'] == "test"
        assert status['network_isolated'] is True
        assert 'uptime_seconds' in status

    def test_get_environment_status_not_found(self):
        """Test status retrieval for non-existent environment"""
        status = self.manager.get_environment_status("nonexistent")
        assert status is None

    def test_list_environments(self):
        """Test listing all environments"""
        # Setup multiple environments
        for i in range(3):
            env = IsolationEnvironment(
                container_id=f"container_{i}",
                environment_type="test",
                network_isolated=True,
                resource_limits={},
                status="running",
                created_at=datetime.now()
            )
            self.manager.environments[f"env_{i}"] = env

        environments = self.manager.list_environments()

        assert len(environments) == 3
        for env in environments:
            assert 'environment_id' in env
            assert 'container_id' in env
            assert 'status' in env

    def test_cleanup_stale_environments(self):
        """Test cleanup of stale environments"""
        # Setup old environment (more than 1 hour ago)
        old_time = datetime.now() - timedelta(hours=2)
        old_env = IsolationEnvironment(
            container_id="old_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=old_time
        )
        self.manager.environments["old_env"] = old_env
        self.manager.active_containers["old_container"] = "old_env"

        # Setup recent environment
        recent_env = IsolationEnvironment(
            container_id="recent_container",
            environment_type="test",
            network_isolated=True,
            resource_limits={},
            status="running",
            created_at=datetime.now()
        )
        self.manager.environments["recent_env"] = recent_env
        self.manager.active_containers["recent_container"] = "recent_env"

        # Mock destruction of old environment
        mock_process = Mock()
        mock_process.returncode = 0
        mock_process.communicate.return_value = ("", "")
        self.mock_popen.return_value = mock_process

        # Execute cleanup
        self.manager._cleanup_stale_environments()

        # Verify old environment was removed, recent environment remains
        assert "old_env" not in self.manager.environments
        assert "old_container" not in self.manager.active_containers
        assert "recent_env" in self.manager.environments
        assert "recent_container" in self.manager.active_containers

    def test_process_isolation_fallback(self):
        """Test process-based isolation when Docker is not available"""
        # Create manager with Docker disabled
        manager = IsolationManager({'enable_docker': False})

        # Mock os and tempfile modules
        with patch('tempfile.mkdtemp') as mock_mkdtemp, \
             patch('builtins.open', create=True) as mock_open, \
             patch('os.path.exists') as mock_exists:

            mock_mkdtemp.return_value = "/tmp/test_env"
            mock_exists.return_value = True

            # Mock file operations
            mock_file = Mock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Mock process creation
            mock_process = Mock()
            mock_process.pid = 12345
            with patch('subprocess.Popen', return_value=mock_process):
                config = ContainerConfig()
                environment = manager.create_environment("test_type", config)

                assert isinstance(environment, IsolationEnvironment)
                assert environment.container_id == "12345"
                assert environment.environment_type == "test_type"

    def test_container_config_defaults(self):
        """Test ContainerConfig default values"""
        config = ContainerConfig()

        assert config.image == "python:3.9-slim"
        assert config.memory_limit == "512m"
        assert config.cpu_limit == 1.0
        assert config.network_isolated is True
        assert config.volume_mounts == {}
        assert config.environment_vars == {}
        assert config.timeout == 300

    def test_container_config_custom_values(self):
        """Test ContainerConfig with custom values"""
        config = ContainerConfig(
            image="custom:latest",
            memory_limit="1g",
            cpu_limit=2.0,
            network_isolated=False,
            timeout=600
        )

        assert config.image == "custom:latest"
        assert config.memory_limit == "1g"
        assert config.cpu_limit == 2.0
        assert config.network_isolated is False
        assert config.timeout == 600

    @pytest.mark.slow
    def test_performance_environment_creation(self):
        """Test performance of environment creation"""
        config = ContainerConfig()

        start_time = time.time()
        environments = []
        for i in range(5):
            mock_process = Mock()
            mock_process.returncode = 0
            mock_process.communicate.return_value = (f"container_{i}", "")
            self.mock_popen.return_value = mock_process

            env = self.manager.create_environment(f"perf_test_{i}", config)
            environments.append(env)

        end_time = time.time()

        assert len(environments) == 5
        # Performance requirement: environment creation should be fast
        assert (end_time - start_time) < 30.0

        # Cleanup
        for env in environments:
            self.manager.destroy_environment(env.container_id)