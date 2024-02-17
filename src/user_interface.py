"""
    User Interface Modul
"""

import address_book
import notes
import files

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"
FLY_BLUE = "\033[38;5;117m"
PURPURE = "\033[35m"


def help_info():
    print(f'    List of comand:\n'
            f'-{YELLOW} record contact {BLUE} - Interacting with contacts.\n'
            f'-{YELLOW} record note {BLUE} - Interacting with notes.\n'
            f'-{YELLOW} opening a text document {BLUE} - Opening a text document for your notes.\n'
            f'-{YELLOW} interacting with applications {BLUE} - Turning on the music player, video player.\n'
            f'-{YELLOW} help {BLUE} - Help\n'
            f'-{YELLOW} exit  {BLUE} - Exit from program.\n{RESET}')

def help_record_contact():
    print(f"    List of comand for 'record_contacts':\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book\n"
            f"-{YELLOW} 'all' {BLUE} - show all records\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number\n"
            f"-{YELLOW} 'help' {BLUE} - help\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - help\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_record_note():
    print(f"    List of comand for 'record_contacts':\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book\n"
            f"-{YELLOW} 'all' {BLUE} - show all records\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number\n"
            f"-{YELLOW} 'help' {BLUE} - help\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - help\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_opening_a_text_document():
    print(f"   {PURPURE}List of comand for 'record_contacts':\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book\n"
            f"-{YELLOW} 'all' {BLUE} - show all records\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number\n"
            f"-{YELLOW} 'help' {BLUE} - help\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - help\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_interacting_with_applications():
    print(f"    List of comand for 'record_contacts':\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book\n"
            f"-{YELLOW} 'all' {BLUE} - show all records\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number\n"
            f"-{YELLOW} 'help' {BLUE} - help\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - help\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def start_bot():
    print(f'{YELLOW}Hello! I`m your personal assistant! To finish working please enter "exit". To view all commands please enter "Help"{RESET}')

    filename = "files\\save_contacts.bin"
    try:
        book = address_book.read_from_file(filename)
    except Exception:
        book = address_book.AddressBook()
    program_status = True

    while program_status:
        data = input(f"{PURPURE}> {RESET}").lower()
        
        if data == "record contact":
            while True:
                input_data = input(f"{FLY_BLUE}[record contact] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    book.save_to_file(filename)
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == "help":
                    help_record_contact()
                elif input_data == "add":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name):
                        record = address_book.Record(name)
                        phone = input(f"{GREEN}Enter phone number (or press 'Enter' to continue): {RESET}")
                        if phone:
                            record.add_phone(phone)
                        birthday = input(f"{GREEN}Enter date of birth [DD-MM-YYYY](or press 'Enter' to continue): {RESET}")
                        if birthday:
                            record.add_birthday(birthday)
                        book.add_record(record)
                elif input_data == "add tel":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name):
                        rec = book.find(name)
                        if rec:
                            phone = input(f"{GREEN}Enter phone number: {RESET}")
                            rec.add_phone(phone)
                        else:
                            print(f"{RED}The name {name} was not found in the address book")

                elif input_data=="delete":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name ):
                        nam=book.delete(name)
                        if nam:
                            print(f"{nam} deleted from address book")
                        else:
                            print(f"{RED}The name {name} was not found in the address book")
                elif input_data == "find":
                    find_contact=input(f"{GREEN}Enter text for searching (part of name or phone number): {RESET}")
                    book.get_find(find_contact)

                elif input_data == "all":
                    n=-1
                    if len(book.data.items())>10:
                        n=10
                    book.get_all(n)
                else:
                    print(f'The command "{data}" not defined')
                
        elif data == 'record note':
            while True:
                input_data = input(f"{FLY_BLUE}[record note] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_record_note()
        
        elif data == 'opening a text document':
            while True:
                input_data = input(f"{FLY_BLUE}[opening a text document] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif data == 'help':
                    help_opening_a_text_document()
        
        elif data == 'interacting with applications':
            while True:
                input_data = input(f"{FLY_BLUE}[interacting with applications] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_interacting_with_applications()
        
        elif data == "help":
                help_info()
        
        elif data == "exit":
                book.save_to_file(filename)
                program_status = False
        
        else:
            print(f"{RED}Invalid command, please enter one of: 'record contact', 'record note', 'opening a text document', 'interacting with_applications'.{RESET}")

start_bot()