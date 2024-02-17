from collections import UserDict
from datetime import date, datetime
import uuid
import re


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
        self.creationdate = datetime.now()

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


class NoteBook(UserDict):

    def add_note(self, note) -> None:
        self.data[note.id] = note

    def find_by_content(self, search_content) -> [Note]:
        found = []
        search_content = search_content.lower()
        for note in self.data:
            if search_content in self.data[note].content.value.lower():
                found.append(self.data[note])  # для тестування замінити ці коментарі в цих 2 рядках місцями)
                # found.append(self.data[note].content.value)
        return f'Found by content: {found}'
        #

    def find_by_tag(self, search_tag) -> [Note]:
        found = []
        search_tag = search_tag.lower()
        for note in self.data:
            for tag in self.data[note].tag:
                if search_tag == tag.value.lower():
                    found.append(self.data[note])  # для тестування замінити ці коментарі в цих 2 рядках місцями)
                    # found.append(self.data[note].content.value)
        return f'Found by tag: {found}'

    def remove_note(self, note_it_to_del) -> None:
        if note_it_to_del in self.data:
            del self.data[note_it_to_del]
            print(f'Note {Note(note_it_to_del).id} deleted')

    def sort_by_tag(self) -> [Note]:
        sorted_notes_by_tags = sorted(self.data.items(), key=lambda x: min(tag.value.lower() for tag in x[1].tag))

        print('Sorted notes by TAG:')
        for note in sorted_notes_by_tags:
            print(note[1].content.value)

        return sorted_notes_by_tags

    def show_all(self) -> {Note}:
        return self.data

    def save_pickle(self, filename):
        pass

    @staticmethod
    def load_pickle(filename):
        pass

    def __str__(self):
        pass  # help


# n1 = Note('1st cc', ['mu', 'eamu'])
# n2 = Note('2nd CC', ['mu', 'da'])
# n1 = Note('1st cc', ['films', 'bv'])
# n2 = Note('2nd CC', ['films', 'av'])
n1 = Note('1st cc', ['mus', 'lu'])
n2 = Note('2ndc', ['lali'])
n2.edit_content('dfds #mus')

b1 = NoteBook()
#
b1.add_note(n1)
b1.add_note(n2)
print(b1.__dict__)


# b1.remove_note('1111')
# print(b1.__dict__)
print(b1.find_by_content('cc'))

print(b1.sort_by_tag())

print(b1.find_by_tag('mus'))
print(b1.show_all())





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
