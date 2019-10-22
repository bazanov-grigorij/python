print('Введите команду:')
command = input()
engine_status = ''

while command:

    # если ввели неправильную комманду
    while command not in {'help', 'on', 'off', 'status', 'exit'}:
        print('''
Вы ввели недопустимую комманду.
Наберите 'help' для помощи.
        ''')
        print()
        print('Введите команду:')
        command = input()

    # список комманд
    if command == 'help':
        print('''
        status - статус двигателя
        on - завести двигатель
        off - заглушить двигатель
        exit - выйти из машины
        ''')

    # статус двигателя
    if command == 'status':
        if engine_status:
            print('двигатель запущен')
            engine_status = True
        else:
            print('двыгатель выключен')

    # завести двигатель
    if command == 'on':
        if not engine_status:
            print('завожу двигатель')
            engine_status = True
        else:
            print('двыгатель уже заведён')

    # выключить двигатель
    if command == 'off':
        if engine_status:
            print('глушу двигатель')
            engine_status = False
        else:
            print('двыгатель уже заглушен')

    # завершить работу программы
    if command == 'exit':
        print('выхожу из машины')
        break

    print()
    print('Введите команду:')
    command = input()