# консольный файловый менеджер
from my_invoice import*
from victory import*
from oss import*
from change_pa import*

baza=[]
baza.append(("create_pa","создать папку"))
baza.append(("delete_pa","удалить (файл/папку)"))
baza.append(("copy_pa", "копировать (файл/папку)"))
baza.append(("look_pa", "просмотр содержимого рабочей директории"))
baza.append(("look_pap","посмотреть только папки"))
baza.append(("look_files","посмотреть только файлы"))
baza.append(("look_os","просмотр информации об операционной системе"))
baza.append(("the_creator","создатель программы"))
baza.append(("play_vict","играть в викторину"))
baza.append(("invoice","мой банковский счет"))
baza.append(("change_pa","смена рабочей директории"))
baza.append(("exit","выход"))

y=True
while y:
    print("Это консольный файловый менеджер")
    for i in range(len(baza)):
        print(str(i)+'-'+baza[i][1])

    choice=int(input("___Выберите пункт меню: "))
    print("*"*10)
    if choice>=0 and choice<len(baza)-1:
        locals()[baza[choice][0]]()
        print("*"*10)
    elif choice==len(baza)-1:
        y=False
        print('Конец работы')
    else:
        print('Неверный пункт меню!')