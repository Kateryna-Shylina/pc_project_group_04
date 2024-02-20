"""
    User Interface Modul
"""

import personal_assistant.address_book
import personal_assistant.notes
#import files

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"
FLY_BLUE = "\033[38;5;117m"
PURPURE = "\033[35m"


def help_info():
    print(f'    {PURPURE}List of comand:{RESET}\n'
            f'-{YELLOW} record contact {BLUE} - Interacting with contacts.{RESET}\n'
            f'-{YELLOW} record note {BLUE} - Interacting with notes.{RESET}\n'
            f'-{YELLOW} opening a text document {BLUE} - Opening a text document for your notes.{RESET}\n'
            f'-{YELLOW} interacting with applications {BLUE} - Turning on the music player, video player.{RESET}\n'
            f'-{YELLOW} help {BLUE} - Help{RESET}\n'
            f'-{YELLOW} exit  {BLUE} - Exit from program.\n{RESET}')

def help_record_contact():
    print(f"   {PURPURE}List of comand for 'record contacts':{RESET}\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book{RESET}\n"
            f"-{YELLOW} 'all' {BLUE} - show all records{RESET}\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name{RESET}\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list{RESET}\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number{RESET}\n"
            f"-{YELLOW} 'help' {BLUE} - help{RESET}\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_record_note():
    print(f"   {PURPURE}List of comand for 'record note':{RESET}\n"
            f"-{YELLOW} 'add' or 'add content' {BLUE} - Add a note.{RESET}\n"
            f"-{YELLOW} 'edit content' or 'ec' {BLUE} - Edit note text.{RESET}\n"
            f"-{YELLOW} 'edit tag' or 'et' {BLUE} - Edit tag.{RESET}\n"
            f"-{YELLOW} 'remove content' or 'rc' {BLUE} - Delete note text.{RESET}\n"
            f"-{YELLOW} 'remove tag' or 'rt' {BLUE} - Delete tag.{RESET}\n"
            f"-{YELLOW} 'remove note' or 'rn' {BLUE} - Delete note.{RESET}\n"
            f"-{YELLOW} 'find by content' or 'fc' {BLUE} - Search within note text.{RESET}\n"
            f"-{YELLOW} 'find by tag' or 'ft' {BLUE} - Search within tag.{RESET}\n"
            f"-{YELLOW} 'sort by tag' or 'st' {BLUE} - Sort by tags.{RESET}\n"
            f"-{YELLOW} 'show all' or 'sa' {BLUE} - Show all notes and their keys.{RESET}\n"
            f"-{YELLOW} 'help' {BLUE} - help.{RESET}\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_opening_a_text_document():
    print(f"   {PURPURE}List of comand for 'record_contacts':{RESET}\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book{RESET}\n"
            f"-{YELLOW} 'all' {BLUE} - show all records{RESET}\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name{RESET}\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list{RESET}\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number{RESET}\n"
            f"-{YELLOW} 'help' {BLUE} - help\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_interacting_with_applications():
    print(f"   {PURPURE}List of comand for 'record_contacts':{RESET}\n"
            f"-{YELLOW} 'add' {BLUE} - add contact to phone book{RESET}\n"
            f"-{YELLOW} 'all' {BLUE} - show all records{RESET}\n"
            f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name{RESET}\n"
            f"-{YELLOW} 'delete' {BLUE} - delete record from list{RESET}\n"
            f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number{RESET}\n"
            f"-{YELLOW} 'help' {BLUE} - help{RESET}\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def start_bot():
    print(f'{YELLOW}Hello! I`m your personal assistant! To finish working please enter "exit". To view all commands please enter "Help"{RESET}')

    #filename_address_book = "files\\save_contacts.bin"
    #filename_note_book = "files\\save_notes.bin"
    filename_address_book = "save_contacts.bin"
    filename_note_book = "save_notes.bin"
    
    try:
        book = personal_assistant.address_book.read_from_file(filename_address_book)
        book.find_birthday_people()
    except Exception:
        book = personal_assistant.address_book.AddressBook()
    
    # try:
    #     note = personal_assistant.notes.NoteBook.load_pickle(filename_note_book)
    # except Exception:
    #     note = personal_assistant.notes.NoteBook()
    note = personal_assistant.notes.NoteBook()
    
    program_status = True

    while program_status:
        data = input(f"{PURPURE}> {RESET}").lower()
        
        if data == "record contact":
            while True:
                input_data = input(f"{FLY_BLUE}[record contact] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename_address_book)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    book.save_to_file(filename_address_book)
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == "help":
                    help_record_contact()
                elif input_data == "add":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name):
                        record = personal_assistant.address_book.Record(name)
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
                    note.save_pickle(filename_note_book)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_record_note()
                elif input_data == 'add' or input_data == 'add content':
                    # Создание новой заметки и добавление её в NoteBook
                    new_tag = input(f"{GREEN}Enter tags: {RESET}")
                    new_content = str(input(f"{GREEN}Enter content: {RESET}"))
                    note.add_note(personal_assistant.notes.Note(new_content, [new_tag]))
                elif input_data == 'edit content' or input_data == 'ec':
                    # Код для редактирования содержимого заметки
                    tag_to_search = input(f"{GREEN}Enter the tag to search for: {RESET}")
                    found_notes = note.find_by_tag(tag_to_search)
                    if found_notes:
                        for found_note in found_notes:
                            edit_contents = input(f"{GREEN}Enter new content: {RESET}")
                            found_note.edit_content(edit_contents)
                    else:
                        print(f"{RED}No notes found with tag '{tag_to_search}'.")
                
                elif input_data == 'edit tag' or input_data == 'et':
                    # Код для редактирования тегов заметки
                    tag_to_search = input(f"{GREEN}Enter the tag to search for: {RESET}")
                    found_notes = note.find_by_tag(tag_to_search)
                    if found_notes:
                        new_tag = input(f"{GREEN}Enter new tag: {RESET}")
                        for found_note in found_notes:
                            found_note.edit_tag(new_tag)
                    else:
                        print(f"{RED}No such tag found.")
                elif input_data == 'remove content' or input_data == 'rc':
                    # Код для удаления содержимого заметки
                    tag_to_search = input(f"{GREEN}Enter the tag to search for: {RESET}")
                    found_notes = note.find_by_tag(tag_to_search)
                    if found_notes:
                        for found_note in found_notes:
                            found_note.remove_content()
                    else:
                        print(f"{RED}No notes found with tag '{tag_to_search}'.")
                elif input_data == 'remove tag' or input_data == 'rt':
                    # Код для удаления тегов заметки
                    tag_to_search = input(f"{GREEN}Enter the tag: {RESET}")
                    found_notes = note.find_by_tag(tag_to_search)
                    if found_notes:
                        for found_note in found_notes:
                            found_note.remove_tag(tag_to_search)
                    else:
                        print(f"{RED}No notes found with tag '{tag_to_search}'.")
                elif input_data == 'remove note' or input_data == 'rn':
                    # Код для удаления заметки
                    tag_to_search = input(f"{GREEN}Enter the tag: {RESET}")
                    found_notes = note.find_by_tag(tag_to_search)
                    if found_notes:
                        print("Found notes with the tag:")
                        for key, found_note in found_notes.items():
                            print(f"Key: {key}, Content: {found_note.content.value}")
                            
                        key_to_delete = input(f"{RED}Enter the key of the note you want to delete: {RESET}")
                        if key_to_delete in found_notes:
                            del note[key_to_delete]
                            print(f'{YELLOW}Note with key {key_to_delete} deleted {RESET}')
                        else:
                            print(f"{RED}Invalid key. No note deleted.")
                    else:
                        print(f"{RED}No notes found with tag '{tag_to_search}'.")
                elif input_data == 'find by content' or input_data == 'fc':
                    # Код для поиска заметок по содержимому
                    find_by_content = input(f"{GREEN}Enter the tag: {RESET}")
                    found_notes = note.find_by_content(find_by_content)
                    print(f"{YELLOW}{found_note}")
                elif input_data == 'find by tag' or input_data == 'ft':
                    # Код для поиска заметок по тегам
                    find_by_tag = input(f"{GREEN}Enter the tag: {RESET}")
                    found_notes = note.find_by_tag(find_by_tag)
                    print(f"{YELLOW}{found_note}")
                elif input_data == 'sort by tag' or input_data == 'st':
                    # Код для сортировки заметок по тегам
                    sorted_notes_contents = note.sort_by_tag()
                    for content in sorted_notes_contents:
                        print(f"{YELLOW}{content}")
                elif input_data == 'show all' or input_data == 'sa':
                    # Код для отображения всех заметок
                    show_all = note.show_all()
                    for note_id, note_content in show_all.items():
                        print(f"{YELLOW}Note ID: {note_id}, Content: {note_content}")
                else:
                    print(f'Command "{data}" not found.')
        
        elif data == 'opening a text document':
            while True:
                input_data = input(f"{FLY_BLUE}[opening a text document] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename_address_book)
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
                    # book.save_to_file(filename)
                    program_status = False
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_interacting_with_applications()
        
        elif data == "help":
                help_info()
        
        elif data == "exit":
                # book.save_to_file(filename)
                program_status = False
        
        else:
            print(f"{RED}Invalid command, please enter one of: 'record contact', 'record note', 'opening a text document', 'interacting with_applications'.{RESET}")


if __name__ == "__main__":
    start_bot()