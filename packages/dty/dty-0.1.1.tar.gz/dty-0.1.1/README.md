
# DTY (Directory-to-YAML)

## Overview
DTY (Directory-to-YAML) is a Python command-line tool designed for quickly generating representations of directory structures and their contents in YAML format. This tool is especially useful for structuring directory data in a token-efficient manner, making it ideal for interactions with language models like ChatGPT.

## Example output
```bash
dty
```

```yaml
my_project:
  __init__.py: ""
  main.py: |
    # Main application file
    import app

    app.run()
  app.py: |
    # App module

    def run():
        print('Running the app')
  utils:
    helper.py: |
      # Utility functions

      def helper():
          return 'Helper function'
```

### Features
- Convert directory contents to YAML format.
- Include or exclude files using patterns (supports fnmatch style, e.g., `*.py`, `data*`).
- Recursive directory parsing.
- Options for output: printing to console, saving to a file, or copying to the clipboard.

## Installation

```bash
pip install dty
```

## Usage

Run DTY from the command line with the following options:

```bash
dty <target-directory> [options]
```

If no target directory is specified, DTY will default to the current working directory.

Options:
- `-t` or `--target-file`: Target a single file. This option is mutually exclusive with `-i`, `-e`, and `-r`.
- `-i` or `--include`: Patterns to include files. Enclose patterns in quotes to avoid shell expansion (e.g., `'*.py'`, `'data*'`).
- `-e` or `--exclude`: Patterns to exclude files. Enclose patterns in quotes to avoid shell expansion (e.g., `'*.xml'`, `'temp*'`).
- `-o` or `--output-file`: Set the output YAML file name.
- `-r` or `--recursive`: Enable recursive search in directories. Not valid when targeting a single file.
- `-p` or `--print`: Print the output using rich formatting.
- `-c` or `--clipboard`: Copy the output to the clipboard.

## Example

```bash
dty myfolder -i '*.py' '*.html' -o output.yaml -r
```

This command will parse all `.py` and `.html` files in `myfolder` recursively and save the YAML output to `output.yaml`.

## Authors

- Adrian Galilea - *Initial work*

## Acknowledgments

- Hat tip to ChatGPT for assistance with project setup and documentation.
