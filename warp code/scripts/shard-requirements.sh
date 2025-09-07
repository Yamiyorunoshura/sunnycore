#!/bin/bash

# shard-requirements.sh
# Split docs/requirements.md by level 1 headings and requirement items into multiple files
# Supports both section-based splitting and requirement-based splitting (F-xxx, NFR-xxx, NFP-xxx)

set -e  # Exit immediately on error

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Input and output paths
INPUT_FILE="docs/requirements.md"
OUTPUT_DIR="docs/requirements"

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Clean filename function
clean_filename() {
    local title="$1"
    # Remove "# " prefix if exists
    title="${title#\# }"
    # Replace spaces with hyphens
    title="${title// /-}"
    # Remove special characters, keep only letters, numbers, hyphens and underscores
    title=$(echo "$title" | sed 's/[^a-zA-Z0-9_-]//g')
    # Convert to lowercase
    title=$(echo "$title" | tr '[:upper:]' '[:lower:]')
    echo "$title"
}

# Extract requirement ID from line
extract_requirement_id() {
    local line="$1"
    # Extract F-001, NFR-P-001, NFP-001 etc.
    if [[ "$line" =~ ^(F-[0-9]{3}|NFR-[A-Z]*-[0-9]{3}|NFP-[0-9]{3}): ]]; then
        echo "${BASH_REMATCH[1]}"
    elif [[ "$line" =~ ^(F-[0-9]{3}|NFR-[A-Z]*-[0-9]{3}|NFP-[0-9]{3})$ ]]; then
        echo "${BASH_REMATCH[1]}"
    else
        echo ""
    fi
}

# Check if line is a level 1 heading
is_h1_title() {
    local line="$1"
    # Check if starts with "# " but not "##" etc.
    [[ "$line" =~ ^#[[:space:]] ]] && [[ ! "$line" =~ ^##.* ]]
}

# Check if line is a functional requirement
is_functional_requirement() {
    local line="$1"
    [[ "$line" =~ ^F-[0-9]{3}: ]] || [[ "$line" =~ ^F-[0-9]{3}$ ]]
}

# Check if line is a non-functional requirement
is_nonfunctional_requirement() {
    local line="$1"
    [[ "$line" =~ ^(NFR-[A-Z]*-[0-9]{3}|NFP-[0-9]{3}): ]] || [[ "$line" =~ ^(NFR-[A-Z]*-[0-9]{3}|NFP-[0-9]{3})$ ]]
}

# Check if line is any requirement
is_requirement() {
    local line="$1"
    is_functional_requirement "$line" || is_nonfunctional_requirement "$line"
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

# Save current section/requirement to file
save_current_item() {
    local current_title="$1"
    local current_filename="$2"
    local current_content="$3"
    local item_type="$4"
    
    if [[ -n "$current_title" && -n "$current_content" ]]; then
        local output_file="$OUTPUT_DIR/$current_filename.md"
        echo -e "$current_content" > "$output_file"
        log_success "Saved $item_type: $current_filename.md"
        return 0
    fi
    return 1
}

# Main function to split document
shard_document() {
    local current_title=""
    local current_filename=""
    local current_content=""
    local current_type="" # "section" or "requirement"
    local line_count=0
    local section_count=0
    local requirement_count=0

    log_info "Starting document processing..."

    # Read input file line by line
    while IFS= read -r line || [[ -n "$line" ]]; do
        line_count=$((line_count + 1))
        
        # Check if this is a new level 1 heading
        if is_h1_title "$line"; then
            # Save previous item if exists
            if save_current_item "$current_title" "$current_filename" "$current_content" "$current_type"; then
                if [[ "$current_type" == "section" ]]; then
                    section_count=$((section_count + 1))
                else
                    requirement_count=$((requirement_count + 1))
                fi
            fi
            
            # Start new section
            current_title="$line"
            current_filename=$(clean_filename "$line")
            current_content="$line"
            current_type="section"
            
            log_info "Found level 1 heading: $line"
            
        # Check if this is a requirement (F-xxx, NFR-xxx, NFP-xxx)
        elif is_requirement "$line"; then
            # Save previous item if exists
            if save_current_item "$current_title" "$current_filename" "$current_content" "$current_type"; then
                if [[ "$current_type" == "section" ]]; then
                    section_count=$((section_count + 1))
                else
                    requirement_count=$((requirement_count + 1))
                fi
            fi
            
            # Extract requirement ID
            local req_id=$(extract_requirement_id "$line")
            
            # Start new requirement
            current_title="$line"
            current_filename="$req_id"
            current_content="$line"
            current_type="requirement"
            
            log_info "Found requirement: $req_id"
            
        else
            # Add content to current section/requirement
            if [[ -n "$current_title" ]]; then
                if [[ -n "$current_content" ]]; then
                    current_content="$current_content"$'\n'"$line"
                else
                    current_content="$line"
                fi
            fi
        fi
    done < "$INPUT_FILE"
    
    # Process last item
    if save_current_item "$current_title" "$current_filename" "$current_content" "$current_type"; then
        if [[ "$current_type" == "section" ]]; then
            section_count=$((section_count + 1))
        else
            requirement_count=$((requirement_count + 1))
        fi
    fi
    
    log_success "Document splitting completed!"
    log_info "Processed $line_count lines"
    log_info "Generated $section_count section files"
    log_info "Generated $requirement_count requirement files"
    log_info "Total: $((section_count + requirement_count)) files"
}

# Main function
main() {
    log_info "Starting Requirements document splitting..."
    
    check_input_file
    create_output_dir
    shard_document
    
    log_success "All operations completed!"
    log_info "Check output files in: $OUTPUT_DIR"
    
    # List generated files
    if ls "$OUTPUT_DIR"/*.md >/dev/null 2>&1; then
        log_info "Generated files:"
        ls -la "$OUTPUT_DIR"/*.md | while read -r line; do
            filename=$(echo "$line" | awk '{print $NF}')
            log_info "  - $(basename "$filename")"
        done
    else
        log_warning "No files were generated"
    fi
}

# Execute main function
main "$@"