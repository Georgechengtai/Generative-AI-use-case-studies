import os
import re
import sys

def check_file(filepath):
    """Checks a single file for formatting errors."""
    error_count = 0
    list_item_pattern = re.compile(r'^\s*[-*]\s+')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return 0

    for i, line in enumerate(lines):
        if i == 0: continue
        
        current_line = line.rstrip()
        prev_line = lines[i-1].rstrip()
        
        if list_item_pattern.match(current_line):
            is_prev_empty = (len(prev_line.strip()) == 0)
            is_prev_list_item = list_item_pattern.match(prev_line)
            
            if not is_prev_empty and not is_prev_list_item:
                print(f"[ERROR] {filepath}:{i+1}")
                print(f"    Line {i}: {prev_line.strip()}")
                print(f"    Line {i+1}: {current_line.strip()}")
                print("    -> RULE VIOLATION: Insert a blank line before the list item.\n")
                error_count += 1
    return error_count

def validate_path(target_path):
    """Scans a file or directory for formatting errors."""
    total_errors = 0
    
    if os.path.isfile(target_path):
        total_errors += check_file(target_path)
    elif os.path.isdir(target_path):
        for dirpath, _, filenames in os.walk(target_path):
            if 'storage' in dirpath.split(os.sep):
                continue
            for filename in filenames:
                if filename.endswith('.md'):
                    total_errors += check_file(os.path.join(dirpath, filename))
    else:
        print(f"Error: Path not found: {target_path}")
        return

    if total_errors == 0:
        print(f"✅ No formatting errors found in {target_path}")
    else:
        print(f"❌ Found {total_errors} formatting errors in {target_path}")

if __name__ == "__main__":
    # Default to docs dir if no arg provided
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_path = os.path.join(project_root, 'docs')

    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        # Handle relative paths from CWD
        if not os.path.isabs(target_path):
            target_path = os.path.abspath(target_path)

    print(f"Scanning: {target_path}\n")
    validate_path(target_path)
