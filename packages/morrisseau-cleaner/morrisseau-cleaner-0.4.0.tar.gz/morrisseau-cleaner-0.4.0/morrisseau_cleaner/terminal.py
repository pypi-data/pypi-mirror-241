from .askii_art import askii_art_main
from morrisseau_cleaner import functions

def display_menu():
    """Display the menu of options for the user."""

    print("Welcome to the Morrisseau Project Cleaner Module!")
    print("  choose a file - Choose input and output files")
    print("  clean spaces - Clean spaces in the chosen file")
    print("  clean pipes - Clean pipes in the chosen file")
    print("  help - Show available commands")
    print("  exit - Exit the program")

def terminal_main():
    askii_art_main()
    display_menu()

    input_file = None
    output_file = None

    while True:
        command = input("Enter a command: ").lower()

        if command == "choose a file":
            input_file = functions.get_file_path()
            output_file = functions.get_output_file_path(input_file)
        elif command == "clean spaces":
            if input_file and output_file:
                functions.clean_spaces(input_file, output_file)
            else:
                print("Please choose a file first.")
        elif command == "clean pipes":
            if input_file and output_file:
                functions.clean_pipes(input_file, output_file)
            else:
                print("Please choose a file first.")
        elif command == "help":
            display_menu()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    terminal_main()
