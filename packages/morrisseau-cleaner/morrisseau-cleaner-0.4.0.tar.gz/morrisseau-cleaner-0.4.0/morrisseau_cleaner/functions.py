import tkinter as tk
from tkinter import filedialog
import re
import csv

def highlight_changes(old_str, new_str) -> None:
    highlighted_str = ""

    for old_char, new_char in zip(old_str, new_str):
        if old_char != new_char:
            highlighted_str += f"\033[91m{new_char}\033[0m"  # Red color for additions
        else:
            highlighted_str += old_char

    # Handle remaining characters if one string is longer than the other
    if len(new_str) > len(old_str):
        highlighted_str += f"\033[91m{new_str[len(old_str):].replace(' ', '␣')}\033[0m"

    print(f"-: {old_str.replace(' ', '␣')} -> {new_str.replace(' ', '␣')} +: {highlighted_str}")

def get_file_path() -> str:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def get_output_file_path(input_file: str) -> str:
    # Pattern to match the 'output-N' format at the end of the file name
    pattern = r'output-(\d+)'

    # Check if the input file name contains 'output-N' format
    match = re.search(pattern, input_file)
    if match:
        # Extract the version number and increment it
        version = int(match.group(1)) + 1
        output_file = re.sub(pattern, f'output-{version}', input_file)
    else:
        # If 'output-N' format is not found, add it with version 1 before the file extension
        base, ext = input_file.rsplit('.', 1)
        output_file = f"{base}-output-1.{ext}"

    return output_file


def clean_spaces(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as input_csv:
        with open(output_file, 'w') as output_csv:
            reader = csv.reader(input_csv)
            writer = csv.writer(output_csv)
            for row in reader:
                new_row = []
                for cell in row:
                    cell = cell.strip()
                    cell = re.sub(' +', ' ', cell)
                    new_row.append(cell)
                writer.writerow(new_row)


def clean_pipes(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as input_csv:
        with open(output_file, 'w') as output_csv:
            reader = csv.reader(input_csv)
            writer = csv.writer(output_csv)
            for row in reader:
                new_row = []
                for cell in row:
                    cell = cell.replace(' |', '|').replace('| ', '|')
                    new_row.append(cell)
                writer.writerow(new_row)



