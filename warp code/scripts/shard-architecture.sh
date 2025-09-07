#!/bin/bash

# shard-architecture.sh
# Split docs/architecture.md by level 1 headings into multiple files

set -e  # Exit immediately on error

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Input and output paths
INPUT_FILE="docs/architecture.md"
OUTPUT_DIR="docs/architecture"

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Clean filename function
clean_filename() {
    local title="$1"
    # Remove "# " prefix
    title="${title#\# }"
    # Replace spaces with hyphens
    title="${title// /-}"
    # Remove special characters, keep only letters, numbers, hyphens and underscores
    title=$(echo "$title" | sed 's/[^a-zA-Z0-9_-]//g')
    # Convert to lowercase
    title=$(echo "$title" | tr '[:upper:]' '[:lower:]')
    echo "$title"
}

# Check input file
check_input_file() {
    if [[ ! -f "$INPUT_FILE" ]]; then
        log_error "Input file not found: $INPUT_FILE"
        exit 1
    fi
    log_info "Found input file: $INPUT_FILE"
}

# Create output directory
create_output_dir() {
    if [[ ! -d "$OUTPUT_DIR" ]]; then
        mkdir -p "$OUTPUT_DIR"
        log_info "Created output directory: $OUTPUT_DIR"
    else
        log_info "Output directory exists: $OUTPUT_DIR"
        # Clean old files in directory
        rm -f "$OUTPUT_DIR"/*.md
        log_info "Cleaned old files in output directory"
    fi
}

# Identify level 1 heading function
is_h1_title() {
    local line="$1"
    # Check if starts with "# " but not "##" etc.
    [[ "$line" =~ ^#[[:space:]] ]] && [[ ! "$line" =~ ^##.* ]]
}

# Main function to split document
shard_document() {
    local current_title=""
    local current_filename=""
    local current_content=""
    local line_count=0
    local section_count=0

    log_info "Starting document processing..."

    # Read input file line by line
    while IFS= read -r line || [[ -n "$line" ]]; do
        line_count=$((line_count + 1))
        
        if is_h1_title "$line"; then
            # If encountering new level 1 heading, save previous section first
            if [[ -n "$current_title" ]]; then
                local output_file="$OUTPUT_DIR/$current_filename.md"
                echo -e "$current_content" > "$output_file"
                log_success "Saved: $current_filename.md"
                section_count=$((section_count + 1))
            fi
            
            # Start new section
            current_title="$line"
            current_filename=$(clean_filename "$line")
            current_content="$line"
            
            log_info "Found level 1 heading: $line"
        else
            # Add content to current section
            if [[ -n "$current_title" ]]; then
                current_content="$current_content"$'\n'"$line"
            fi
        fi
    done < "$INPUT_FILE"
    
    # Process last section
    if [[ -n "$current_title" ]]; then
        local output_file="$OUTPUT_DIR/$current_filename.md"
        echo -e "$current_content" > "$output_file"
        log_success "Saved: $current_filename.md"
        section_count=$((section_count + 1))
    fi
    
    log_success "Document splitting completed!"
    log_info "Processed $line_count lines, generated $section_count files"
}

# Main function
main() {
    log_info "Starting Architecture document splitting..."
    
    check_input_file
    create_output_dir
    shard_document
    
    log_success "All operations completed!"
    log_info "Check output files:"
    ls -la "$OUTPUT_DIR"/*.md 2>/dev/null || log_info "No files generated"
}

# Execute main function
main "$@"