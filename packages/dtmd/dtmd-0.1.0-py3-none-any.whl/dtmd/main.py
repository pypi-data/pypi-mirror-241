import os
import argparse
from rich import print as rich_print
import pyperclip
import fnmatch

def list_files(directory, include_patterns, exclude_patterns, recursive):
    """Recursively list files in the directory with specified filename glob patterns."""
    file_structure = {}

    for root, dirs, files in os.walk(directory):
        if not recursive and root != directory:
            break

        relative_path = os.path.relpath(root, directory)
        file_list = []

        for file in files:
            if include_patterns and not any(fnmatch.fnmatch(file, pat) for pat in include_patterns):
                continue
            if exclude_patterns and any(fnmatch.fnmatch(file, pat) for pat in exclude_patterns):
                continue
            file_list.append(os.path.join(root, file))

        if file_list:
            if relative_path == '.':
                relative_path = ''

            file_structure[relative_path] = file_list

    return file_structure

def read_file_contents_to_markdown(file_structure, directory):
    """Convert file structure to Markdown format."""
    root_directory_name = os.path.basename(directory)
    markdown_output = f"# /{root_directory_name}\n"
    
    for path, files in file_structure.items():
        if path:
            depth = path.count(os.sep) + 2
            heading_level = '#' * depth
            markdown_output += f"{heading_level} /{path}\n"
        else:
            depth = 2

        for file_info in files:
            try:
                with open(file_info, 'r') as f:
                    content = f.read()
                file_name = os.path.basename(file_info)
                file_heading_level = '#' * depth
                markdown_output += f"{file_heading_level} {file_name}\n```python\n{content}\n```\n"
            except Exception as e:
                rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_info}[/bold cyan]: [bold red]{e}[/bold red]")

    return markdown_output

def process_single_file_to_markdown(file_path):
    """Process a single file and return its content in Markdown format."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        file_name = os.path.basename(file_path)
        return f"### {file_name}\n```python\n{content}\n```"
    except Exception as e:
        rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_path}[/bold cyan]: [bold red]{e}[/bold red]")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown representation of a directory's contents.")
    parser.add_argument(
        'target', 
        nargs='?', 
        default=os.getcwd(), 
        type=str, 
        help="Target directory. Defaults to the current directory if not specified."
    )
    parser.add_argument('-t', '--target-file', type=str, help="Target a single file. This option is mutually exclusive with other directory-based options.")
    parser.add_argument('-i', '--include', type=str, nargs='+', help="Patterns to include files.")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="Patterns to exclude files.")
    parser.add_argument('-o', '--output-file', type=str, default='output.md', help="Name of the output Markdown file.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Enable recursive search in directories.")
    parser.add_argument('-p', '--print', action='store_true', help="Print the output to the console using rich formatting.")
    parser.add_argument('-c', '--clipboard', action='store_true', help="Copy the output to the clipboard.")

    args = parser.parse_args()

    if args.target_file:
        markdown_data = process_single_file_to_markdown(args.target_file)
        if markdown_data is None:
            return
    else:
        file_structure = list_files(args.target, args.include, args.exclude, args.recursive)
        markdown_data = read_file_contents_to_markdown(file_structure, args.target)

    if args.print:
        rich_print(markdown_data)
    elif args.clipboard:
        pyperclip.copy(markdown_data)
        rich_print("[bold green]Output has been copied to the clipboard.[/bold green]")
    else:
        with open(args.output_file, 'w') as file:
            file.write(markdown_data)

if __name__ == "__main__":
    main()