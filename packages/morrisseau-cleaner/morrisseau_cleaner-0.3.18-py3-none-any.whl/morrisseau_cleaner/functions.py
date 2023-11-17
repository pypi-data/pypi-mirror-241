def highlight_changes(old_str, new_str):
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


