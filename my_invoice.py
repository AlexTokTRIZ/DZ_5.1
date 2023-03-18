# Программа "Личный счет"
def invoice():
    y=True
    invoice=0
    hist={}
    while y:
        print('-'*10)
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        choice = input('Выберите пункт меню: ')
        print('-'*10)
        if choice == '1':
            sum=int(input('Введите сумму (целое положительное число): '))
            invoice+=sum
        elif choice == '2':
            sum=int(input('Введите сумму покупки (целое положительное число): '))
            if invoice>=sum:
                pok = input('Введите название покупки: ')
                hist[pok] = sum
            else:
                print('Недостаточно средств для покупки')
        elif choice == '3':
            if len(hist)!=0:
                print('Список покупок:')
                for i in hist:
                    print('Покупка: ',i,'  Цена: ',hist[i])
            else:
                print('У Вас нет покупок')
        elif choice == '4':
            y=False
        else:
            print('Неверный пункт меню')

# print('__name__', __name__)
if __name__ == '__main__':
    my_invoice()