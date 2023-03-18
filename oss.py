import os
import sys
import shutil

def create_pa():
    print("*"*10)
    pa=input('Ведите имя создаваемой папки: ')
    if not os.path.exists(pa):
        os.mkdir(pa)
    else:
        print('Такая папка уже существует')

def delete_pa():
    print("*"*10)
    look_pa()
    pa=input('Введите имя удаляемой папки или файла: ')
    if os.path.exists(os.path.join(os.getcwd(),pa)):
        if os.path.isfile(pa):
            os.remove(pa)
        elif os.path.isdir(pa):
            os.rmdir(os.path.join(os.getcwd(), pa))
    else:
        print('Такая папка не существует')

def look_pa(): #"просмотр содержимого рабочей директории"))
    print(os.listdir(os.getcwd()))

def copy_pa(): # "copy_pa", "копировать (файл/папку)"))
    look_pa()
    pa=input('Ведите имя копируемой папки или файла: ')
    if os.path.exists(os.path.join(os.getcwd(),pa)):
        pa_new = input('Ведите новое имя копируемой папки или файла: ')
        if os.path.isfile(pa):
            shutil.copy(os.path.join(os.getcwd(), pa), pa_new)
        elif os.path.isdir(pa):
            shutil.copytree(os.path.join(os.getcwd(), pa), pa_new)
    else:
        print('Такая папка не существует')

def look_pap():
    for i in os.listdir(os.getcwd()):
            if os.path.isdir(os.path.join(os.getcwd(),i)):
                print(os.path.join(i))

def look_files(): # "look_files","посмотреть только файлы"))
    for i in os.listdir(os.getcwd()):
            if not os.path.isdir(os.path.join(os.getcwd(),i)):
                print(os.path.join(i))

def look_os():  # "look_os","просмотр информации об операционной системе"))
    print(sys.platform)

def the_creator():  #cоздатель программы"))
    print('Создатель программы - AlexCreo')


