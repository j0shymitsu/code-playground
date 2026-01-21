# Export all Python TODO comments in a folder to a markdown to-do list

import os
import re
from pathlib import Path
from datetime import datetime

def find_python_files(root_dir):
    '''Recursively find all .py files'''
    python_files = []
    root_path = Path(root_dir)

    if not root_path.exists():
        raise ValueError(f"Directory '{root_dir}' does not exist!")
    
    for file in root_path.rglob('*.py'):        # Recursively yield
        python_files.append(file)

    return python_files

def extract_todos(file_path):
    '''Extract TODO comments from Python file'''
    todos = []
    todo_pattern = re.compile(r'#\s*TODO[:\s]*(.+)', re.IGNORECASE)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                match = todo_pattern.search(line)
                if match:
                    todo_text = match.group(1).strip()
                    todos.append({
                        'line': line_num,
                        'text': todo_text,
                        'file': file_path
                    })
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    
    return todos

def generate_markdown(todos_by_file, root_dir):
    '''Generate md file with checkboxes'''
    lines = []

    for file_path, todos in sorted(todos_by_file.items()):
        relative_path = file_path.relative_to(root_dir)
        lines.append(f'## {relative_path}\n')

        for todo in todos:
            lines.append(f"- [ ] **Line {todo['line']}:** {todo['text']}")

        lines.append("")

    return "\n".join(lines)

def main():
    root_dir = input("Enter root directory path: ").strip()

    try:
        root_path = Path(root_dir).expanduser().resolve()

        print(f"\nSearching for Python files in: {root_path}")
        python_files = find_python_files(root_path)
        print(f"Found {len(python_files)} Python file(s)")

        print("\nExtracting TODOs...")
        todos_by_file = {}
        total_todos = 0

        for file in python_files:
            todos = extract_todos(file)
            if todos:
                todos_by_file[file] = todos
                total_todos += len(todos)

        print(f"Found {total_todos} TODO(s) in {len(todos_by_file)} file(s)")

        if not todos_by_file:
            print("No TODOs found!")
            return
        
        markdown_content = generate_markdown(todos_by_file, root_path)
        output_file = root_path / "TODO_LIST.md"

        # Append if exists
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\nTODOs appended to: {output_file}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    main()
