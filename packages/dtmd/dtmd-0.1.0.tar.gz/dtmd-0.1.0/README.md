
# DTMD (Directory-to-Markdown)

## Overview
DTMD (Directory-to-Markdown) is a Python command-line tool, particularly useful for quickly generating and sharing representations of directory structures and their contents in a structured and readable Markdown format. This makes it ideal for documenting project structures, especially for interactions with language models like ChatGPT.

Markdown is the most token efficient manner to interact with LLM's

## Example output
```bash
dtmd
```

```markdown
# /my_project
## main.py
```python
# Main application file
import app

app.run()
```
## app.py
```python
# App module

def run():
    print('Running the app')
```
## /utils
### helper.py
```python
# Utility functions

def helper():
    return 'Helper function'
```
```

### Features
- Convert directory contents to Markdown format.
- Include or exclude files using patterns (supports fnmatch style, e.g., `*.py`, `data*`).
- Recursive directory parsing.
- Options for output: printing to console, saving to a file, or copying to the clipboard.

## Installation

```bash
pip install dtmd
```

## Usage

Run DTMD from the command line with the following options:

```bash
dtmd <target-directory> [options]
```

If no target directory is specified, DTM will default to the current working directory.

Options:
- `-i` or `--include`: Patterns to include files. Enclose patterns in quotes to avoid shell expansion (e.g., `'*.py'`, `'data*'`).
- `-e` or `--exclude`: Patterns to exclude files. Enclose patterns in quotes to avoid shell expansion (e.g., `'*.xml'`, `'temp*'`).
- `-o` or `--output-file`: Set the output Markdown file name.
- `-r` or `--recursive`: Enable recursive search in directories.
- `-p` or `--print`: Print the output using rich formatting.
- `-c` or `--clipboard`: Copy the output to the clipboard.

## Example

```bash
dtmd myfolder -i '*.py' '*.html' -o output.md -r
```

This command will parse all `.py` and `.html` files in `myfolder` recursively and save the Markdown output to `output.md`.

## Authors

- Adrian Galilea - *Initial work*

## Acknowledgments

- Hat tip to ChatGPT for assistance with project setup and documentation.
