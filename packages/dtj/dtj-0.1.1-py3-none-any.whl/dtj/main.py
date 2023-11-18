import json
import os
import argparse
from rich import print as rich_print

def list_files(directory, include_exts, exclude_exts, recursive):
    """List files in the directory with specified extensions and exclusions."""
    file_paths = []
    for root, dirs, files in os.walk(directory):
        if not recursive:
            dirs[:] = []  # Stop recursion into subdirectories
        for file in files:
            if include_exts:
                if any(file.endswith(ext) for ext in include_exts):
                    file_paths.append(os.path.join(root, file))
            elif exclude_exts:
                if not any(file.endswith(ext) for ext in exclude_exts):
                    file_paths.append(os.path.join(root, file))
            else:
                file_paths.append(os.path.join(root, file))
    return file_paths

def main():
    parser = argparse.ArgumentParser(description="Generate a JSON file from a directory's contents.")
    parser.add_argument(
        'target', 
        nargs='?', 
        default=os.getcwd(), 
        type=str, 
        help="Target directory. Defaults to the current directory if not specified."
    )
    parser.add_argument('target', type=str, help="Target directory.")
    parser.add_argument('-i', '--include', type=str, nargs='+', help="File extensions to include (e.g., py html).")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="File extensions to exclude (e.g., xml).")
    parser.add_argument('-o', '--output-file', type=str, default='output.json', help="Output JSON file name.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Recursively search in directories.")
    parser.add_argument('-p', '--print', action='store_true', help="Print the output using rich.")
    parser.add_argument('-c', '--clipboard', action='store_true', help="Copy the output to the clipboard.")

    args = parser.parse_args()

    if args.include and args.exclude:
        rich_print("[bold red]Error:[/bold red] -i/--include and -e/--exclude cannot be used together. Please specify only one.")
        return

    file_paths = list_files(args.target, args.include, args.exclude, args.recursive)

    data = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                data.append({"filename": os.path.basename(file_path), "content": content})
        except Exception as e:
            rich_print(f"[bold yellow]Warning:[/bold yellow] Skipped file [bold cyan]{file_path}[/bold cyan] due to error: [bold red]{e}[/bold red]")

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