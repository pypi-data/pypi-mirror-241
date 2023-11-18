
# DTJ (Directory to JSON)

## Overview
DTJ (Directory to JSON) is a Python command-line tool, particularly useful for quickly generating and sharing representations of directory structures in a token-efficient manner, making it ideal for interactions with language models like ChatGPT.

## Example output
```bash
dtj
```

```json
[
    {
        "filename": "main.py",
        "content": "# Main application file\nimport app\n\napp.run()"
    },
    {
        "filename": "app.py",
        "content": "# App module\n\ndef run():\n    print('Running the app')"
    },
    {
        "filename": "utils.py",
        "content": "# Utility functions\n\ndef helper():\n    return 'Helper function'"
    }
]
```


### Features
- Convert directory contents to JSON format.
- Include or exclude specific file types.
- Recursive directory parsing.
- Options for output: printing to console, saving to a file, or copying to the clipboard.

## Installation

To use DTJ, you'll need Python installed on your system. Clone this repository or download the `DTJ.py` script.

```bash
git clone https://github.com/adriangalilea/dtj.git
cd DTJ
```

## Usage

Run DTJ from the command line with the following options:

```bash
python dtj.py <target-directory> [options]
```

If no target directory is specified, DTJ will default to the current working directory.

Options:
- `-i` or `--include`: Specify file extensions to include (e.g., `py`, `html`).
- `-e` or `--exclude`: Specify file extensions to exclude.
- `-o` or `--output-file`: Set the output JSON file name.
- `-r` or `--recursive`: Enable recursive search in directories.
- `-p` or `--print`: Print the output using rich formatting.
- `-c` or `--clipboard`: Copy the output to the clipboard.

## Example

```bash
python DTJ.py myfolder -i py html -o output.json -r
```

This command will parse all `.py` and `.html` files in `myfolder` recursively and save the JSON output to `output.json`.

## Authors

- Adrian Galilea - *Initial work*

## Acknowledgments

- Hat tip to ChatGPT for assistance with project setup and documentation.
