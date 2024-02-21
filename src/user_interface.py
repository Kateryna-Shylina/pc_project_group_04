"""
    User Interface Modul
"""

import os
import address_book
import notes
import notepad
import files
import different
from notepad import Notepad_dict
from different import Different_dict

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"
FLY_BLUE = "\033[38;5;117m"
PURPURE = "\033[35m"


def help_info():
    print(f'    {PURPURE}List of comand:{RESET}\n'
            f'-{YELLOW} "record contact" or "contact" {BLUE} - Interacting with contacts.{RESET}\n'
            f'-{YELLOW} "record note" or "note" {BLUE} - Interacting with notes.{RESET}\n'
            f'-{YELLOW} "notepad" {BLUE} - Opening a text document for your notes.{RESET}\n'
            f'-{YELLOW} "interacting with applications" or "iwa" {BLUE} - Turning on the music player, video player.{RESET}\n'
            f'-{YELLOW} "help" {BLUE} - Help{RESET}\n'
            f'-{YELLOW} "exit"  {BLUE} - Exit from program.\n{RESET}')

def help_record_contact():
    print(f"   {PURPURE}List of commands for 'record contacts':{RESET}\n"
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
            f"-{YELLOW} 'remove tag' or 'rt' {BLUE} - Delete tag.{RESET}\n"
            f"-{YELLOW} 'remove note' or 'rn' {BLUE} - Delete note.{RESET}\n"
            f"-{YELLOW} 'find by content' or 'fc' {BLUE} - Search within note text.{RESET}\n"
            f"-{YELLOW} 'find by tag' or 'ft' {BLUE} - Search within tag.{RESET}\n"
            f"-{YELLOW} 'sort by tag' or 'st' {BLUE} - Sort by tags.{RESET}\n"
            f"-{YELLOW} 'show all' or 'all' {BLUE} - Show all notes and their keys.{RESET}\n"
            f"-{YELLOW} 'help' {BLUE} - help.{RESET}\n"
            f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
            f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")

def help_opening_a_text_document():
    print(f"   {PURPURE}List of commands for 'working with text files':{RESET}\n"
          f"-{YELLOW} 'add' {BLUE} - Creating an empty text file (you can open it with the 'edit' command).{RESET}\n"
          f"-{YELLOW} 'all' {BLUE} - Show all posts.{RESET}\n"
          f"-{YELLOW} 'add descr' {BLUE} - Add text Document.{RESET}\n"
          f"-{YELLOW} 'edit' {BLUE} - Opening a text document to edit entries.{RESET}\n"
          f"-{YELLOW} 'delete' {BLUE} - Delete selected file.{RESET}\n"
          f"-{YELLOW} 'find' {BLUE} - Search by text in files.{RESET}\n"
          f"-{YELLOW} 'help' {BLUE} - help\n"
          f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
          f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")


def help_interacting_with_applications():
    print(f"   {PURPURE}List of commands for 'record_contacts':{RESET}\n"
          f"-{YELLOW} 'add' {BLUE} - add contact to phone book{RESET}\n"
          f"-{YELLOW} 'all' {BLUE} - show all records{RESET}\n"
          f"-{YELLOW} 'add tel' {BLUE} - add phone number to record with Name{RESET}\n"
          f"-{YELLOW} 'delete' {BLUE} - delete record from list{RESET}\n"
          f"-{YELLOW} 'find' {BLUE} - search for records by part of a name or phone number{RESET}\n"
          f"-{YELLOW} 'help' {BLUE} - help{RESET}\n"
          f"-{YELLOW} 'main menu' of 'back' {BLUE} - Return to main menu{RESET}\n"
          f"-{YELLOW} exit  {BLUE} - exit from program\n{RESET}")


def start_bot():
    print(f'{YELLOW}Hello! I`m your personal assistant! To finish working please enter {RED}"exit"{YELLOW}. To view all commands please enter "help"{RESET}')

    base_path = os.path.dirname(__file__)
    filename_address_book = os.path.join(base_path, "..", "files", "save_contacts.bin")
    filename_note_book = os.path.join(base_path, "..", "files", "save_notes.bin")
    filename_notepad_book = os.path.join(base_path, "..", "files", "save_notepad.bin")

    try:
        book = address_book.read_from_file(filename_address_book)
        book.find_birthday_people()
    except Exception:
        book = address_book.AddressBook()

    try:
        note = notes.NoteBook.load_pickle(filename_note_book)
    except Exception:
        note = notes.NoteBook()

    try:
        notepad_dict = notepad.read_from_file(filename_notepad_book)
    except Exception:
        notepad_dict = Notepad_dict()
    
    filename_different_dict= different.get_dict()
    
    PROGRAM_STATUS = True

    while PROGRAM_STATUS:
        data = input(f"{PURPURE}> {RESET}").lower()

        if data == "record contact" or data == "contact":
            while True:
                input_data = input(f"{FLY_BLUE}[record contact] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    book.save_to_file(filename_address_book)
                    PROGRAM_STATUS = False
                    break
                elif input_data == 'main menu' or input_data == 'back':
                    book.save_to_file(filename_address_book)
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
                        birthday = input(
                            f"{GREEN}Enter date of birth [DD-MM-YYYY](or press 'Enter' to continue): {RESET}")
                        if birthday:
                            record.add_birthday(birthday)
                        email = input(f"{GREEN}Enter email (or press 'Enter' to continue): {RESET}")
                        if email:
                            record.add_email(email)
                        address = input(f"{GREEN}Enter address (or press 'Enter' to continue): {RESET}")
                        if address:
                            record.add_address(address)
                        book.add_record(record)
                        book.save_to_file(filename_address_book)
                elif input_data == "add tel":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name):
                        rec = book.find(name)
                        if rec:
                            phone = input(f"{GREEN}Enter phone number: {RESET}")
                            rec.add_phone(phone)
                        else:
                            print(f"{RED}The name {name} was not found in the address book")
                    book.save_to_file(filename_address_book)
                elif input_data == "delete":
                    name = input(f"{GREEN}Enter name: {RESET}")
                    if (name):
                        nam = book.delete(name)
                        if nam:
                            print(f"{nam} deleted from address book")
                        else:
                            print(f"{RED}The name {name} was not found in the address book")
                    book.save_to_file(filename_address_book)
                elif input_data == "find":
                    find_contact = input(f"{GREEN}Enter text for searching (part of name or phone number): {RESET}")
                    book.get_find(find_contact)

                elif input_data == "all":
                    n = -1
                    if len(book.data.items()) > 10:
                        n = 10
                    book.get_all(n)
                else:
                    print(
                        f'{RED}Command "{data}" not found. The following command will "help" you know what the commands are.')

        elif data == 'record note' or data == 'note':
            while True:
                input_data = input(f"{FLY_BLUE}[record note] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    note.save_pickle(filename_note_book)
                    PROGRAM_STATUS = False
                    break
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    note.save_pickle(filename_note_book)
                    break
                elif input_data == 'help':
                    help_record_note()
                elif input_data == 'add' or input_data == 'add content':
                    # Создание новой заметки и добавление её в NoteBook
                    new_tag = input(f"{GREEN}Enter tags: {RESET}")
                    new_content = str(input(f"{GREEN}Enter content: {RESET}"))
                    note.add_note(notes.Note(new_content, [new_tag]))
                    note.save_pickle(filename_note_book)
                elif input_data == 'edit tag' or input_data == 'et':
                    # Код для редактирования тегов заметки
                    tag_to_edit = input(f"{GREEN}Enter the tag to search for: {RESET}")
                    new_tag = input(f"{GREEN}Enter new teg: {RESET}")
                    note.edit_tag_by_old_value(tag_to_edit, new_tag)
                    note.save_pickle(filename_note_book)
                    print(f"{YELLOW}Post tag changed to '{new_tag}'{RESET}")
                elif input_data == 'edit content' or input_data == 'ec':
                    # Код для редактирования содержимого заметки
                    input_tag = input(f"{GREEN}Enter the tag to search for: {RESET}")
                    input_new_content = input(f"{GREEN}Enter new content: {RESET}")
                    note.edit_content_by_tag(input_tag, input_new_content)
                    note.save_pickle(filename_note_book)
                    print(f"{YELLOW}content changed successfully{RESET}")
                elif input_data == 'remove tag' or input_data == 'rt':
                    # Код для удаления тегов заметки
                    delete_teg = input(f"{GREEN}Enter name tag dor delete: {RESET}")
                    found_notes = note.find_by_tag(delete_teg)
                    if found_notes:
                        note.edit_tag_by_old_value(delete_teg, [])
                        note.save_pickle(filename_note_book)
                        print(f"{YELLOW}You delete tag '{delete_teg}'{RESET}")
                    else:
                        print(f"{RED} No such tag")
                elif input_data == 'remove note' or input_data == 'rn':
                    # Код для удаления заметки
                    delete_id = input(f"{GREEN}Enter ID notes: {RESET}")
                    if delete_id in note.data:
                        note.remove_note(note.data[delete_id])
                        note.save_pickle(filename_note_book)
                        print(f"{YELLOW}Заметка с ID {delete_id} удалена.{RESET}")
                    else:
                        print(f"{RED} No such ID")
                elif input_data == 'find by content' or input_data == 'fc':
                    # Код для поиска заметок по содержимому
                    find_by_content = input(f"{GREEN}Enter the words that are in the text: {RESET}")
                    found_notes = note.find_by_content(find_by_content)
                    print(f"{YELLOW}{found_notes}")
                elif input_data == 'find by tag' or input_data == 'ft':
                    # Код для поиска заметок по тегам
                    find_by_tag = input(f"{GREEN}Enter the tag: {RESET}")
                    found_notes = note.find_by_tag(find_by_tag)
                    print(f"{YELLOW}{found_notes}")
                elif input_data == 'sort by tag' or input_data == 'st':
                    # Код для сортировки заметок по тегам
                    sorted_notes_contents = note.sort_by_tag()
                    # for content in sorted_notes_contents:
                    print(f"{YELLOW}{sorted_notes_contents}")
                elif input_data == 'show all' or input_data == 'all':
                    # Код для отображения всех заметок
                    print(note.show_all())
                else:
                    print(
                        f'{RED}Command "{input_data}" not found. The following command will "help" you know what the commands are.')

        elif data == 'notepad':
            while True:
                input_data = input(f"{FLY_BLUE}[notepad] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    PROGRAM_STATUS = False
                    notepad_dict.save_to_file(filename_notepad_book)
                    break
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    notepad_dict.save_to_file(filename_notepad_book)
                    break
                elif input_data == 'help':
                    help_opening_a_text_document()
                elif input_data == 'add':
                    notepad_dict.add_notepad()
                    notepad_dict.save_to_file(filename_notepad_book)
                elif input_data == 'all':
                    notepad_dict.get_all()
                    notepad_dict.save_to_file(filename_notepad_book)
                elif input_data == 'add descr':
                    try:
                        notepad_dict[input(f"{GREEN}Enter file name: {RESET}")].add_description()
                        notepad_dict.save_to_file(filename_notepad_book)
                    except KeyError:
                        print(f"{RED}This file is daily{RESET}")
                elif input_data == 'edit' or input_data == 'look':
                    try:
                        notepad_dict[input(f"{GREEN}Enter file name: {RESET}")].open_notepad()
                        notepad_dict.save_to_file(filename_notepad_book)
                    except KeyError:
                        print(f"{RED}no such file exists.{RESET}")
                elif input_data == "delete":
                    try:
                        notepad_dict.delete_notepad(input(f"{GREEN}Enter file name: {RESET}"))
                        notepad_dict.save_to_file(filename_notepad_book)
                    except KeyError:
                        print(f"{RED}this file is not exist.{RESET}")
                elif input_data == 'find':
                    notepad_dict.find(input(f"{GREEN}Enter text to search: {RESET}"))
                else:
                    print(f'{RED}Command "{input_data}" not found. The following command will "help" you know what the commands are.')
                
        elif data == 'interacting with applications' or data == 'iwa':
            while True:
                input_data = input(f"{FLY_BLUE}[interacting with applications] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    PROGRAM_STATUS = False
                    filename_different_dict.save_to_file(filename_different_dict)
                    break
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_interacting_with_applications()
                elif input_data == 'all':
                    filename_different_dict.get_all()
                elif input_data == 'add descr':
                    try:
                        filename_different_dict[input(f"{GREEN}File name:{RESET}")].add_description()
                    except KeyError:
                        print(f"{RED}this file is not exist.{RESET}")
                elif input_data == 'play':
                    try:
                        filename_different_dict[input(f"{GREEN}File name:{RESET}")].open_different()
                    except KeyError:
                        print(f"{RED}this file is not exist.{RESET}")
                elif input_data == 'look type':
                    filename_different_dict.get_all_type(input(f"{GREEN}File type(audio, video...):{RESET}"))
                elif input_data == 'find':
                    filename_different_dict.get_found(input(f"{GREEN}Search word:{RESET}"))
                else:
                    print(f'{RED}Command "{input_data}" not found. The following command will "help" you know what the commands are.')
                
        
        elif data == "help":
            help_info()

        elif data == "exit":
            book.save_to_file(filename_address_book)
            note.save_pickle(filename_note_book)
            notepad_dict.save_to_file(filename_notepad_book)
            PROGRAM_STATUS = False

        else:
            print(f"{RED}Command not found. The following command will 'help' you know what the commands are.{RESET}")


if __name__ == "__main__":
    start_bot()