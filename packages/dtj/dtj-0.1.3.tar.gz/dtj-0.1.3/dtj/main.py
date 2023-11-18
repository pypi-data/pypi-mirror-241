import json
import os
import argparse
from rich import print as rich_print
import pyperclip

def list_files(directory, include_exts, exclude_exts, recursive):
    """Recursively list files in the directory with specified extensions and exclusions."""
    file_structure = {}
    base_dir_name = os.path.basename(directory.rstrip(os.sep)) or '.'

    for root, dirs, files in os.walk(directory):
        relative_path = os.path.relpath(root, directory)
        relative_path = relative_path if relative_path != '.' else base_dir_name

        file_list = []

        for file in files:
            if include_exts and not any(file.endswith(ext) for ext in include_exts):
                continue
            if exclude_exts and any(file.endswith(ext) for ext in exclude_exts):
                continue
            file_list.append(file)

        if file_list or not recursive:
            file_structure[relative_path] = file_list
            if not recursive:
                break

    return file_structure

def read_file_contents(file_structure, directory):
    for path, files in file_structure.items():
        for i, file in enumerate(files):
            file_path = os.path.join(directory, path, file) if path != os.path.basename(directory) else os.path.join(directory, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                file_structure[path][i] = {"filename": file, "content": content}
            except Exception as e:
                rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_path}[/bold cyan]: [bold red]{e}[/bold red]")
    return file_structure

def main():
    parser = argparse.ArgumentParser(description="Generate a JSON file from a directory's contents.")
    parser.add_argument(
        'target', 
        nargs='?', 
        default=os.getcwd(), 
        type=str, 
        help="Target directory. Defaults to the current directory if not specified."
    )
    parser.add_argument('-i', '--include', type=str, nargs='+', help="File extensions to include (e.g., py, html).")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="File extensions to exclude (e.g., xml).")
    parser.add_argument('-o', '--output-file', type=str, default='output.json', help="Output JSON file name.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Recursively search in directories.")
    parser.add_argument('-p', '--print', action='store_true', help="Print the output using rich.")
    parser.add_argument('-c', '--clipboard', action='store_true', help="Copy the output to the clipboard.")

    args = parser.parse_args()

    if args.include and args.exclude:
        rich_print("[bold red]Error:[/bold red] -i/--include and -e/--exclude cannot be used together. Please specify only one.")
        return

    file_structure = list_files(args.target, args.include, args.exclude, args.recursive)
    data = read_file_contents(file_structure, args.target)
    
    json_data = json.dumps(data, indent=4)

    if args.clipboard:
        pyperclip.copy(json_data)
        rich_print("[bold green]Output has been copied to the clipboard.[/bold green]")
    elif args.print:
        rich_print(json_data)
    else:
        with open(args.output_file, 'w') as file:
            file.write(json_data)

if __name__ == "__main__":
    main()