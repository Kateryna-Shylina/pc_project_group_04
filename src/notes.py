from collections import UserDict
from datetime import datetime
import uuid
import re
import pickle
import os


class Field:
    mandatory = False

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


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
        # self.id = '1111'  # для тесів залишено(щоб точно був відомий id), закоментувати попередній рядок, а цей розкоментувати
        self.content = Content(content)
        if tags:
            self.tag = [Tag(tag) for tag in tags]
        else:
            self.tag = []
        self.creationdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def edit_content(self, new_content) -> None:
        self.content.value = new_content
        tags_found = re.findall(r'#\s*([\w-]+\d*)', self.content.value)
        # print(f'Found :{tags_found}')
        tags_found = [Tag(tag) for tag in tags_found]  # перетворюємо знайдені рядки на об'єкти Tag
        # print(tags_found)
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
                found.append(self.data[note])  # для тестування замінити ці коментарі в цих 2 рядках місцями)
        return f'Found notes by content: {found}'
        #

    def find_by_tag(self, search_tag) -> [Note]:
        found = []
        search_tag = search_tag.lower()
        for note in self.data:
            for tag in self.data[note].tag:
                if search_tag == tag.value.lower():
                    found.append(self.data[note])  # для тестування замінити ці коментарі в цих 2 рядках місцями)
        return f'Found by tag: {found}'


    def remove_note(self, note_it_to_del) -> None:
        if note_it_to_del.id in self.data:
            del self.data[note_it_to_del.id]
            print(f'Note {Note(note_it_to_del).id} deleted')

    def sort_by_tag(self) -> [Note]:
        # сортуємо по тегу. При цьому, якщо в списку декілька тегів, то в кожному списку береться "1й" по алфавіту
        # і сортується по цим "1м" значенням
        sorted_notes_by_tags = sorted(self.data.items(), key=lambda x: min(tag.value.lower() for tag in x[1].tag))
        sorted_notes_by_tags = [note for id, note in sorted_notes_by_tags]  # залишаємо об'єкти Note
        return f'Sorted notes by TAG: {sorted_notes_by_tags}'


    def show_all(self) -> {Note}:
        return f'All Notes: {list(self.data.values())}'

    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            deserialized = pickle.load(file)
        return deserialized

if __name__ == '__main__':

    n1 = Note('1st cc', ['music', 'legends'])
    n2 = Note('2ndc', ['lali'])
    # n2.edit_content('"We Are the Champions" #is a song by the British rock band Queen, released from the band"s sixth album News of the World (1977). Written by lead singer Freddie Mercury, it remains among rock"s most recognisable anthems.')
    n2.edit_content('We')
    b1 = NoteBook()

    #
    b1.add_note(n1)
    b1.add_note(n2)
    print(b1.find_by_content('cc'))
    b1.remove_note(n2)
    print(b1.__dict__)
    exit()

    print(b1.sort_by_tag())

    print(b1.find_by_tag('is'))
    print(b1.show_all())

    b1.save_pickle('content_file.bin')

    if os.path.isfile('content_file.bin'):  # this block aut-ly runs everytime - to load objects if we have them in file
        try:  #  we use standard name of the file content_file.bin and the Notebook is always saved to the name re_stored_notebook
            re_stored_notebook = NoteBook.load_pickle('content_file.bin')  # its a static method, no need to run it from some instance
        except MemoryError:
            print('Not correct object')
        except Exception:
            print('Error reading the file')
    else:
        print('no file to load objects from found')

    if re_stored_notebook:
        print(re_stored_notebook)

    # в змінній re_stored_notebook знаходяться дані з файлу content_file - ті дані з якими ми останній раз працювали

    # print(n1.content.value)
    # n1.remove_content()

    # print(n1.content.value)

    # n1.edit_content('new #new #new-22 ')
    # n2.add_tag('new')
    # print(n2.tag)
    # print(n2.tag[0].value)
    # print(n2.tag[1].value)

    # print(b1.find_by_content('2'))
    # print(b1.find_by_tag('new'))

    # print(n1.content.value)
    # print(n1.tag[0].value)
    # print(n1.tag[1].value)
    # print(n1.tag[2].value)
    # exit()

    # n1.content.value = 'new'
    # print(n1.content.value)

    # print(n1.tag)
    #
    # n1.tag = [Tag('new tag')]
    # print(n1.content.value)

    # print(n1.__dict__)
    # exit()
    # print(n2.content.value)

    # print(n1.tag)
    #
    # n2.edit_content('new cont')
    # print(n2.content.value)
    # n2.remove_content()
    # print(n2.content.value)
    #
    # n1.edit_tag('new tag')
    # print(n1.tag[0].value)
    #
    # print(n1.tag)
    #
    # n1.remove_tag()
    # print(n1.tag)

    # print(n1.__dict__)
    # print(n2.__dict__)
    # print((n3.__dict__))
    #
    # b1 = NoteBook()
    # b2 = NoteBook()
    # #
    # # b1.add_note(n1)
    # # b1.add_note(n2)
    # # print(b1.__dict__)
    #
    #
    # b1.remove_note('1111')
    # print(b1.__dict__)
    # # print(b1.find_by_content('cc'))
    #
    #
    # b1.sort_by_tag()
    #
    # print(b1.find_by_tag('mus'))
    # print(b1.show_all())
    # print(b1)
