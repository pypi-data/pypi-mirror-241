import os
import argparse
from rich import print as rich_print
import pyperclip
import fnmatch
import yaml

class LiteralString(str):
    pass

def literal_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_presenter)

def list_files(directory, include_patterns, exclude_patterns, recursive):
    file_structure = {}
    for root, dirs, files in os.walk(directory):
        if not recursive:
            dirs[:] = []
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
                relative_path = os.path.basename(directory)
            file_structure[relative_path] = file_list
    return file_structure

def process_single_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return {"filename": os.path.basename(file_path), "content": content}
    except Exception as e:
        rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_path}[/bold cyan]: [bold red]{e}[/bold red]")
        return None

def read_file_contents(file_structure, directory):
    output = {}
    base_dir = os.path.basename(directory)
    output[base_dir] = {}

    for path, files in file_structure.items():
        dir_dict = output[base_dir] if path == base_dir else {}

        for file_info in files:
            try:
                with open(file_info, 'r') as f:
                    content = f.read()
                filename = os.path.basename(file_info)
                dir_dict[filename] = LiteralString(content)
            except Exception as e:
                rich_print(f"[bold yellow]Warning:[/bold yellow] Could not read file [bold cyan]{file_info}[/bold cyan]: [bold red]{e}[/bold red]")

        if path != base_dir:
            output[base_dir][path] = dir_dict

    return output


def main():
    parser = argparse.ArgumentParser(description="Generate a YAML file from a directory's contents.")
    parser.add_argument('target', nargs='?', default=os.getcwd(), type=str, help="Target directory. Defaults to the current directory if not specified.")
    parser.add_argument('-t', '--target-file', type=str, help="Target a single file. This option is mutually exclusive with other directory-based options.")
    parser.add_argument('-i', '--include', type=str, nargs='+', help="Patterns to include files. Enclose patterns in quotes to avoid shell expansion (supports fnmatch style, e.g., '*.py', 'data*', '?file.txt').")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="Patterns to exclude files. Enclose patterns in quotes to avoid shell expansion (supports fnmatch style, e.g., '*.xml', 'temp*').")
    parser.add_argument('-o', '--output-file', type=str, default='output.yaml', help="Name of the output YAML file.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Enable recursive search in directories. Not applicable with --target-file.")
    parser.add_argument('-p', '--print', action='store_true', help="Print the output to the console using rich formatting.")
    parser.add_argument('-c', '--clipboard', action='store_true', help="Copy the output to the clipboard.")

    args = parser.parse_args()

    if args.target_file:
        data = process_single_file(args.target_file)
        if data is None:
            return
    else:
        file_structure = list_files(args.target, args.include, args.exclude, args.recursive)
        data = read_file_contents(file_structure, args.target)

    yaml_data = yaml.dump(data, default_flow_style=False)

    if args.print:
        rich_print(yaml_data)
    elif args.clipboard:
        pyperclip.copy(yaml_data)
        rich_print("[bold green]Output has been copied to the clipboard.[/bold green]")
    else:
        with open(args.output_file, 'w') as file:
            file.write(yaml_data)

if __name__ == "__main__":
    main()
