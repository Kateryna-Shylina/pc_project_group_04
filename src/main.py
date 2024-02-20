
import os
import re
import uuid
import pickle
from collections import UserDict
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"
FLY_BLUE = "\033[38;5;117m"
PURPURE = "\033[35m"


def help_info():
    print(f'   {PURPURE}List of commands:{RESET}\n'
          f'-{YELLOW} "record contact" or "contact" {BLUE} - Interacting with contacts.{RESET}\n'
          f'-{YELLOW} "record note" or "note" {BLUE} - Interacting with notes.{RESET}\n'
          f'-{YELLOW} "notepad" {BLUE} - Opening a text document for your notes.{RESET}\n'
          f'-{YELLOW} interacting with applications {BLUE} - Turning on the music player, video player.{RESET}\n'
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
    print(f"   {PURPURE}List of commands for 'record note':{RESET}\n"
          f"-{YELLOW} 'add' or 'add content' {BLUE} - Add a note.{RESET}\n"
          f"-{YELLOW} 'edit content' or 'ec' {BLUE} - Edit note text.{RESET}\n"
          f"-{YELLOW} 'edit tag' or 'et' {BLUE} - Edit tag.{RESET}\n"
          f"-{YELLOW} 'remove content' or 'rc' {BLUE} - Delete note text.{RESET}\n"
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

    book = read_from_file(filename_address_book)
    """
    try:
        book = read_from_file(filename_address_book)
        book.find_birthday_people()
    except Exception:
        book = AddressBook()
    """
    try:
        note = NoteBook.load_pickle(filename_note_book)
    except Exception:
        note = NoteBook()

    try:
        notepad_dict = read_from_file(filename_notepad_book)
    except Exception:
        notepad_dict = Notepad_dict()

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
                        record = Record(name)
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
                    note.edit_tag_by_old_value(delete_teg, [])
                    note.save_pickle(filename_note_book)
                    print(f"{YELLOW}You delete tag '{delete_teg}'{RESET}")
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
                    note.save_pickle(filename_note_book)
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
                    print(
                        f'{RED}Command "{input_data}" not found. The following command will "help" you know what the commands are.')

        elif data == 'interacting with applications':
            while True:
                input_data = input(f"{FLY_BLUE}[interacting with applications] {RESET}| {GREEN}Enter command: {RESET}")
                if input_data == "exit":
                    PROGRAM_STATUS = False
                    break
                elif input_data == 'main menu' or input_data == 'back':
                    print(f"{YELLOW} You have returned to the main menu.")
                    break
                elif input_data == 'help':
                    help_interacting_with_applications()
                else:
                    print(
                        f'{RED}Command "{input_data}" not found. The following command will "help" you know what the commands are.')

        elif data == "help":
            help_info()

        elif data == "exit":
            book.save_to_file(filename_address_book)
            note.save_pickle(filename_note_book)
            notepad_dict.save_to_file(filename_notepad_book)
            PROGRAM_STATUS = False

        else:
            print(f"{RED}Command not found. The following command will 'help' you know what the commands are.{RESET}")


# Address book =============================================
def read_from_file(file):
    with open(file, 'rb') as fh:
        return pickle.load(fh)

class Field:
    mandatory = False
    
    def __init__(self, value):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super.__init__(self,value)



class Phone(Field):
    def __init__(self, value):
        if int(value) and len(value)==10:
            self.value = value
        else:
            raise ValueError


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = value
            d = value.split("-")
            self.date=datetime(int(d[2]),int(d[1]),int(d[0]))
        except Exception as e: 
            raise ValueError


class Name(Field):
    def __init__(self, value):
        self.value = value


class Address(Field):
    def __init__(self, value):
        self.value = value


class Email(Field):
    def __init__(self, value):    
        result = re.findall(r"[a-zA-Z][a-zA-Z0-9._]+@[a-z]{2,}\.[a-z]{2,}", value)
        if result[0] == value:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.email = None
        self.birthday = birthday
        if birthday:
            try:
                self.date = Birthday(birthday)
            except  ValueError:
                print('Please enter date of birth in string format "DD-MM-YYYY"')

    def add_birthday(self, birthday_s):
        try:
            self.value = birthday_s
            self.birthday = Birthday(birthday_s)
        except  ValueError:
            print(f'{birthday_s} Please enter date of birth in string format "DD-MM-YYYY"')

    def days_to_birthday(self):
        if self.birthday:
            current_datetime = datetime.now()
            dbirt = datetime(current_datetime.year, self.birthday.date.month, self.birthday.date.day)
            if current_datetime>dbirt:
                dbirt = datetime(current_datetime.year+1, self.birthday.date.month, self.birthday.date.day)

            days = dbirt - current_datetime
            print(f"{days.days} days before birthday of {self.name}")

    def add_phone(self, phone_s):
        try:
            self.phones.append(Phone(phone_s))
        except ValueError as e:
            if len(str(e))>0:
                print(f'{RED}{e}{YELLOW} - Phone number must consist of numbers only{RESET}')
            else:
                print(f'{RED}{phone_s}{YELLOW} - Phone number must consist of 10 numbers{RESET}')

    def edit_phone(self, old_phone, new_phone):
        n=0
        f=True
        for phone in self.phones:
            if phone.value == old_phone:
                f = False
                self.phones.pop(n)
                self.phones.insert(n,Phone(new_phone))
            n+=1
        if f:
            raise ValueError

    def remove_phone(self, phone):
        n = 0
        f = True
        try:
            for phon in self.phones:
                if phon.value == phone:
                    f = False
                    self.phones.pop(n)
                n += 1
            if f:
                raise ValueError
        except ValueError:
            print(f'{RED}{phone} {YELLOW} - not found{RESET}')

    def find_phone(self, num_phone):
        for phone in self.phones:
            if phone.value == num_phone:
                return phone
            
    def add_address(self, address_s):
        self.address = Address(address_s)

    def add_email(self, email_s):
        try:
            self.email = Email(email_s)
        except  ValueError:
            print(f'{RED}{email_s}{YELLOW} -  Wrong email address{RESET}')

    def __str__(self):
        sp = f"{BLUE} phones:{YELLOW} {'; '.join(p.value for p in self.phones)}" if self.phones else ""
        sb = f",{BLUE} birthday: {YELLOW} {self.birthday}{RESET}" if self.birthday else ""
        sa = f",{BLUE} address: {YELLOW} {self.address}{RESET}" if self.address else ""
        se = f",{BLUE} email: {YELLOW} {self.email}{RESET}" if self.email else ""
        return (f"{BLUE}Contact name:{YELLOW} {self.name.value} {sp} {sb} {sa} {se}")  


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value]=record

    def get_all_in_page(self, n=0):

        list_rec = []
        for name, record in self.data.items():
            list_rec.append(record)
        if n<=0:
            n=len(list_rec)

        def list_generator(n, x=0):
            y = n + x
            for l in list_rec[x:y]:
                print(l)
            if y >= len(list_rec):
                return
            
            if input("Press Enter to continue") == "":
                if (x + n) <= len(list_rec):
                    x = x + n
                    list_generator(n, x)

        list_generator(n)

    def get_find(self, found=""):
        for name, record in self.data.items():
            find_tel = 0
            for num in record.phones:
                if str(num).find(found)>=0:
                    find_tel = 1
            if (name.find(found) >= 0 or find_tel == 1):
                print(record)


    def get_some(self, x, y):
        i=0
        for name, record in self.data.items():
            if (x <= i and i <= y):
                print(record)
            i += 1

    def get_all(self, count = -1):
        if count == -1 or count > len(self.data.items()):
            a = len(self.data.items())
        else:
            a = count-1

        y = a
        self.get_some(0, y)
        while y < len(self.data.items()):
            if input("Press Enter to continue") == "":
                print("%" * 50)
                x=y+1
                y+=a+1
                self.get_some(x, y)

    def find(self, name):
        for nam, rec in self.data.items():
            if rec.name.value.lower() == name.lower():
                return rec

    def delete(self, name):
        for nam, rec in self.data.items():
            if nam == name:
                del self[nam]
                return nam
        return None
    
    def find_birthday_people(self):
        birthday_people_list = list()
        for name, record in self.data.items():            
            current_datetime = datetime.now().date()
            dbirt = datetime(current_datetime.year, record.birthday.date.month, record.birthday.date.day).date()
            if current_datetime == dbirt:
                sp = f"  {GREEN}{'; '.join(p.value for p in record.phones)}" if record.phones else ""
                sb = f"  {GREEN}{record.birthday}{RESET}" if record.birthday else ""
                se = f"  {GREEN}{record.email}{RESET}" if record.email else ""    
                birthday_people_list.append(f"{GREEN} {record.name.value:<8} {sb:<12} {sp:<12} {se:<20}")   
                          
        if (birthday_people_list):
            print(f"{GREEN}Today is the birthday of some of your friends, congratulate them:")
            print(f"{GREEN}{'\n'.join(person for person in birthday_people_list)}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self,fh)


#Notes=============================================================
class Content(Field):

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Tag(Field):

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Note:

    def __init__(self, content, tags=[]):
        self.id = str(uuid.uuid4())[:5]
        self.content = Content(content)
        if tags:
            self.tag = [Tag(tag) for tag in tags]
        else:
            self.tag = []
        self.creationdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def edit_content(self, new_content) -> None:
        self.content.value = new_content
        tags_found = re.findall(r'#\s*([\w-]+\d*)', self.content.value)
        tags_found = [Tag(tag) for tag in tags_found]  # перетворюємо знайдені рядки на об'єкти Tag
        if tags_found:
            self.tag.extend(tags_found)

    def remove_content(self) -> None:
        self.content.value = 'Content <<<<Сlassified>>>>'  # Замість видалення помічажмо матеріл Засекречено =)

    def add_tag(self, new_tag) -> None:
        self.tag.append(Tag(new_tag))

    def edit_tag(self, new_tag) -> None:
        self.tag = [Tag(new_tag)]

    def remove_tag(self) -> None:
        self.tag = []

    def __str__(self):
        return f'Content: {self.content.value}, Note ID: {self.id}, Date Created: {self.creationdate}, Tags: {[tag.value for tag in self.tag]}'

    def __repr__(self):
        return f'Content: {self.content.value}, Note ID: {self.id}, Date Created: {self.creationdate}, Tags: {[tag.value for tag in self.tag]}'


class NoteBook(UserDict):

    def add_note(self, note) -> None:
        self.data[note.id] = note

    def find_by_content(self, search_content) -> [Note]:
        found = []
        search_content = search_content.lower()
        for note in self.data:
            if search_content in self.data[note].content.value.lower():
                found.append(self.data[note])
        result = '\n'.join(str(line) for line in self.data.values())

        return f'Found notes by content:\n{result}'

    def find_by_tag(self, search_tag) -> [Note]:
        found = []
        search_tag = search_tag.lower()
        for note in self.data:
            for tag in self.data[note].tag:
                if search_tag == tag.value.lower():
                    found.append(self.data[note])  # для тестування замінити ці коментарі в цих 2 рядках місцями)

        result = '\n'.join(str(line) for line in self.data.values())

        return f'Found by tag:\n{result}'

    def edit_content_by_tag(self, search_tag, new_content):
        search_tag = search_tag.lower()
        for note in self.data.values():
            for tag in note.tag:
                if search_tag == tag.value.lower():
                    note.edit_content(new_content)
                    return f'Content edited for note with tag {search_tag}'
        return f'No note found with tag {search_tag}'

    def edit_tag_by_old_value(self, old_tag, new_tag):
        count_changed = 0
        for note in self.data.values():
            for tag in note.tag:
                if tag.value == old_tag:
                    tag.value = new_tag
                    count_changed += 1
        if count_changed > 0:
            return f"{count_changed} tag(s) '{old_tag}' successfully changed to '{new_tag}'."
        else:
            return f"No tag '{old_tag}' found in any note."

    # --------------------------------------------------------------------------------------------------------

    def remove_note(self, note_it_to_del) -> None:
        if note_it_to_del.id in self.data:
            del self.data[note_it_to_del.id]
            print(f'Note {Note(note_it_to_del).id} deleted')

    def sort_by_tag(self) -> [Note]:
        # сортуємо по тегу. При цьому, якщо в списку декілька тегів, то в кожному списку береться "1й" по алфавіту
        # і сортується по цим "1м" значенням
        sorted_notes_by_tags = sorted(self.data.items(), key=lambda x: min(tag.value.lower() for tag in x[1].tag))
        sorted_notes_by_tags = [note for id, note in sorted_notes_by_tags]  # залишаємо об'єкти Note

        result = '\n'.join(str(note) for note in sorted_notes_by_tags)

        return f'Sorted notes by TAG:\n{result}'

    def show_all(self) -> {Note}:
        result = '\n'.join(str(value) for value in self.data.values())
        return f'All Notes:\n{result}'

    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            deserialized = pickle.load(file)
        return deserialized            


# Notepad====================================================================
class Notepad(Field):
    def __init__(self, name, describe="нотатки" ):
        self.topic = "notes"
        self.describe = describe
        self.name=name
        self.dir=os.path.join(path_different,"notes")
        self.file=os.path.join(self.dir,name)+'.txt'
        try:
            with open(self.file, 'x'):
                pass
        except Exception:
            pass

    def open_notepad(self):
        os.system(self.file)
    def add_description(self):
        print("add your description to this notebook, please")
        self.describe=input(">")


    def __str__(self):
        return (f"{BLUE} name:{YELLOW} {self.name}, {BLUE}description:{YELLOW} {self.describe}{RESET}")


#------------КЛАС ДЛЯ списку текстових файлів-------------
#----можна показати список, видалити зі списку, при правильному виході все зберігається, --------------
#----можливо терба зробити зберігання після кожної зміни списку(додавання видалення)
class Notepad_dict(UserDict):
    filename=os.path.join("..\\files", "save_notepad.bin")

    def add_notepad(self):
        print("Enter file name")
        while True:
            name=input("> ")
            if len(name)>0:
                notepad = Notepad(name)
                print("Enter a short description")
                notepad.describe = input("> ")
                notepad.open_notepad()
                self[notepad.name] = notepad
                break
            else:
                continue

    def get_all(self):
        for n in self:
            print(self[n])

    def delete_notepad(self, name):
        os.remove(self[name].file)
        del self[name]



    def save_to_file(self,filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)

    def find(self, text):
        f=False
        for n in self:
            if text in self[n].name or text in self[n].describe:
                print(self[n])
                f=True
        if f==False:
            print(f"{YELLOW}{text}{BLUE} is not found{RESET}")



#----------відкриття або створення notepad_dict------

path_different= "my_dir"


#-----------------ця частина робится один раз, створюються всі необхідні папки---


topics= ["video", "audio", "python", "photos","notes"]

if os.path.exists(path_different):
    pass
else:
    os.mkdir(path_different)
    [os.mkdir(os.path.join(path_different, d)) for d in  topics]
path_notes=os.path.join(path_different, "notes")

dir_notes = [os.path.splitext(p)[0] for p in os.listdir(path_notes)]


if __name__ == "__main__":
    start_bot()