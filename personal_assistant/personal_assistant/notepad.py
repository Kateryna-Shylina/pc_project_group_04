from collections import UserDict
import os
from main import Field
import pickle
from personal_assistant.address_book import read_from_file

##***************************************  ЦЕ САМ МОДУЛЬ **************************************************************

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"

#------------КЛАС ДЛЯ ОДНОГО ФАЙЛА З КОРОТКИМ ОПИСОМ--------------
#-----можна створити, викликати для редагування, додати опис----------------
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
    filename=os.path.join("files", "notepad.bin")

    def add_notepad(self):
        print("введіть назву файла")
        while True:
           name=input(">")
           if len(name)>0:
                notepad = Notepad(name)
                print("введіть короткий опис")
                notepad.describe = input(">")
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



    def save_to_file(self):
       with open(self.filename, 'wb') as fh:
           pickle.dump(self, fh)


#----------відкриття або створення notepad_dict------

path_different="my_dir"

filename=os.path.join("files", "notepad.bin")
try:
    notepad_dict = read_from_file(filename)
except Exception:
    notepad_dict=Notepad_dict()


#-----------------ця частина робится один раз, створюються всі необхідні папки---
# ---- можливо її треба запустити в setap

topics= ["video", "audio", "python", "photos","notes"]

if os.path.exists(path_different):
   pass
else:
   os.mkdir(path_different)
   [os.mkdir(os.path.join(path_different, d)) for d in  topics]
path_notes=os.path.join(path_different, "notes")

dir_notes = [os.path.splitext(p)[0] for p in os.listdir(path_notes)]
print(dir_notes)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#--------частина , яку треба додати до інтерфейсу спілкування з споживачем-------------
# -------якщо споживач набере неповне слово, то йому запропонують варіанти- того що він хотів------
# список повних команд у списку "command"
def start_bot():
    command=["exit", "look all notebooks", "edit notebook", "edit file","delete file",
             "look notebook", "edit description", "змінити опис","додати опис",
             "add description", "add file"]
    data=""
    while True:
        if data=="":
            data = input(">").lower()
        if data == "exit" :
            notepad_dict.save_to_file()
            break
        elif data == "look all notebooks" :
            notepad_dict.get_all()
            data=""
        elif data =="edit notebook" or data =="edit file"  or data=="look notebook" :
            try:
               notepad_dict[input("введіть назву файла >")].open_notepad()
            except KeyError:
                print("такого файла нема")
            data = ""
        elif data =="edit description" or data =="змінити опис" or data =="додати опис" or data =="add description"  :
            try:
               notepad_dict[input("введіть назву файла >")].add_description()
               data = ""
            except KeyError:
                print(f"такий файл відсутній")
            data = ""
        elif data=="add file" :
            notepad_dict.add_notepad()
            data = ""
        elif  data=="delete file":
            try:
                notepad_dict.delete_notepad(input("введіть назву файла >"))
                data = ""
            except KeyError:
                print("this file is not exist")
        else:
            data_temp=data
            for com in command:
                 if data in com:
                    print (f'perhaps you mean "{com}"? press {RED}"Y+ Enter"{RESET} if it is right or {RED}"Enter"{RESET} if no')
                    if input(">").upper()=="Y":
                        data=com
                        break

            if data_temp == data:
               print(" такої команди нема, спробуйте знову")
               data,data_temp = "", ""




start_bot()









