import json
import os
import argparse
from rich import print as rich_print
import pyperclip
import fnmatch

def list_files(directory, include_patterns, exclude_patterns, recursive):
    """Recursively list files in the directory with specified filename glob patterns."""
    file_structure = {}
    base_dir_name = os.path.basename(directory.rstrip(os.sep)) or '.'

    for root, dirs, files in os.walk(directory):
        if not recursive:
            dirs[:] = []

        relative_path = os.path.relpath(root, directory)
        relative_path = relative_path if relative_path != '.' else base_dir_name
        file_list = []

        for file in files:
            if include_patterns and not any(fnmatch.fnmatch(file, pat) for pat in include_patterns):
                continue
            if exclude_patterns and any(fnmatch.fnmatch(file, pat) for pat in exclude_patterns):
                continue

            file_list.append(os.path.join(root, file))

        if file_list:
            file_structure[relative_path] = file_list

    return file_structure

def process_single_file(file_path):
    """Process a single file and return its content in JSON format."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return {"filename": os.path.basename(file_path), "content": content}
    except Exception as e:
        rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_path}[/bold cyan]: [bold red]{e}[/bold red]")
        return None

def read_file_contents(file_structure, directory):
    output = {"directory": os.path.basename(directory), "contents": []}
    
    for path, files in file_structure.items():
        if path == os.path.basename(directory):
            dir_contents = output["contents"]
        else:
            dir_contents = []
            sub_dir = {"directory": path, "contents": dir_contents}
            output["contents"].append(sub_dir)

        for file_info in files:
            try:
                with open(file_info, 'r') as f:
                    content = f.read()
                file_dict = {"filename": os.path.basename(file_info), "content": content}
                dir_contents.append(file_dict)
            except Exception as e:
                rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_info}[/bold cyan]: [bold red]{e}[/bold red]")

    return output


def main():
    parser = argparse.ArgumentParser(description="Generate a JSON file from a directory's contents.")
    parser.add_argument(
        'target', 
        nargs='?', 
        default=os.getcwd(), 
        type=str, 
        help="Target directory. Defaults to the current directory if not specified."
    )
    parser.add_argument('-t', '--target-file', type=str, help="Target a single file. This option is mutually exclusive with other directory-based options.")
    parser.add_argument('-i', '--include', type=str, nargs='+', help="Patterns to include files. Enclose patterns in quotes to avoid shell expansion (supports fnmatch style, e.g., '*.py', 'data*', '?file.txt').")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="Patterns to exclude files. Enclose patterns in quotes to avoid shell expansion (supports fnmatch style, e.g., '*.xml', 'temp*').")
    parser.add_argument('-o', '--output-file', type=str, default='output.json', help="Name of the output JSON file.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Enable recursive search in directories. Not applicable with --target-file.")
    parser.add_argument('-p', '--print', action='store_true', help="Print the output to the console using rich formatting.")
    parser.add_argument('-c', '--clipboard', action='store_true', help="Copy the output to the clipboard.")


    args = parser.parse_args()

    if args.target_file:
        data = process_single_file(args.target_file)
        if data is None:
            return
    else:
        if args.include and args.exclude:
            rich_print("[bold red]Error:[/bold red] -i/--include and -e/--exclude cannot be used together. Please specify only one.")
            return
        file_structure = list_files(args.target, args.include, args.exclude, args.recursive)
        data = read_file_contents(file_structure, args.target)

    json_data = json.dumps(data, indent=4)

    if args.print:
        rich_print(json_data)
    elif args.clipboard:
        pyperclip.copy(json_data)
        rich_print("[bold green]Output has been copied to the clipboard.[/bold green]")
    else:
        with open(args.output_file, 'w') as file:
            file.write(json_data)

if __name__ == "__main__":
    main()