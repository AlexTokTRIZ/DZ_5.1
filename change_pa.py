import os
def path_exist(path):
    if os.path.exists(path):
        os.chdir(path)
        print('Теперь рабочая директория такая: ',path)
    else:
        print('Такой директории не существует: ',path)

def compare_recurs(spis1,spis2,i):   # рекурсивная функция поиска пересечения списков.
        print(spis1,spis2,i)
        print(i!=0, i>=abs((len(spis1)-len(spis2))))# Результат - список составляющих директорий - baza
        if i>0 or i>=abs((len(spis1)-len(spis2))): # пока не закончится один или другой список
            if spis1[i:]!=spis2[:len(spis1)-i]: # пока списки не одинаковые
                print (i, len(spis1)-i)
                return compare_recurs(spis1,spis2,i-1)
            else:
                new_spis=spis1[:i]+spis2
                work_path = '\\'.join(new_spis)  # превращение списка в путь
                path_exist(work_path)
                print(work_path)
                return
        else:
            return print('Такой директории не существует: ', '\\'.join(spis2))

def dirpath_recurs(path):   # рекурсивная функция разделения пути на составляющие.
                                # Результат - список составляющих директорий - baza
        my_path=[]
        dirpath, filename = os.path.split(path)
        if filename!='':
            my_path.append(filename)
            return dirpath_recurs(dirpath)
        else:
            my_path.append(dirpath)
            return path

def change_pa():  # "смена рабочей директории"))
    pa = input('Ведите имя новой рабочей директории: ')
    other_path= pa.replace('\\', '/').split('/') # приведение слэшей к одному виду
    #print(pa)
    dirpath, filename = os.path.split(os.getcwd())
    if pa.find('/')==-1 or pa.find('\\')==-1:  #если нет / то значит имя дирректории не содержит пути
        path_exist(os.path.join(dirpath, pa))
    elif pa.find(':')!=-1: #если есть : значит указан полный путь
        path_exist(pa)
    elif filename == pa:
        print('Введённая директория совпадает с текущей')
    else:  # во введенной строке есть слэш - требуется проверить на совпадение частей пути
        path = os.getcwd()
        my_path = []
        dirpath_recurs(path)  #
        my_path.reverse()  # разворот списка, так как он дополнялся с конца
        #print(my_path)
        work_path = '\\'.join(my_path)  # превращение списка в путь
        print(work_path)
        i = len(my_path) - 1
        compare_recurs(my_path, other_path, i)

if __name__ == '__main__':
    change_pa()
