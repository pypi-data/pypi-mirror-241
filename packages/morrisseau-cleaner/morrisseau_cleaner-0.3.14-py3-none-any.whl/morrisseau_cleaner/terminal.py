import functions as f
import askii_art as aa
import datetime

def help_menu() -> None:
    print("Available commands:")
    print("  Choose a file")
    print("  Clean spaces")
    print("  Clean pipes")
    print("  Clean dates")
    print("  Clean titles")
    print("  Clean page numbers ")
    print("  Clean lexicon entries")
    print("  Clean empty cells")
    print("  Clean capitalization")
    print("  Help")
    print("  Exit")  

def display_menu():
    print("Welcome to the Morrisseau Project Cleaner Module!")
    print("  help - Show available commands")
    print("  exit - Exit the program")

def terminal():
    aa.askii_art()
    display_menu()
    # f.write_to_log("###############################\n")
    # f.write_to_log(f"Program started at {datetime.datetime.now}\n")
    while True:
        command = input("Enter a command: ").lower()
        if command == "choose a file":
            input_file = f.get_input_file()
            output_file = f.get_output_file_path(input_file)
            f.create_output_file(input_file, output_file)

            f.write_to_log(f"User Chose file: {input_file}\n")
            f.write_to_log(f"Output file: {output_file}\n")

        # elif command == "clean spaces":
        #     f.clean_spaces(input_file, output_file)
        #     f.write_to_log(f"User cleaned spaces\n")
        #     print("Spaces cleaned!")
        
        # elif command == "clean pipes":
        #     f.clean_pipes(input_file, output_file)
        #     f.write_to_log(f"User cleaned pipes\n")
        #     print("Pipes cleaned!")

        # elif command == "clean dates":
        #     f.clean_dates(input_file, output_file)
        #     f.write_to_log(f"User cleaned dates\n")
        #     print("Dates cleaned!")

        # elif command == "clean titles":
        #     f.clean_titles(input_file, output_file)
        #     f.write_to_log(f"User cleaned titles\n")
        #     print("Titles cleaned!")

        # elif command == "clean page numbers":
        #     f.clean_page_numbers(input_file, output_file)
        #     f.write_to_log(f"User cleaned page numbers\n")
        #     print("Page numbers cleaned!")
        # elif command == "clean lexicon entries":
        #     f.clean_lexicon_entries(input_file, output_file)
        #     f.write_to_log(f"User cleaned lexicon entries\n")
        #     print("Lexicon entries cleaned!")
        # elif command == "clean empty cells":
        #     f.clean_empty_cells(input_file, output_file)
        #     f.write_to_log(f"User cleaned empty cells\n")
        #     print("Empty cells cleaned!")
        # elif command == "clean capitalization":
        #     f.clean_capitalization(input_file, output_file)
        #     f.write_to_log(f"User cleaned capitalization\n")
        #     print("Capitalization cleaned!")
            
        elif command == "help":
            help_menu()
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Error: command not recognized!")