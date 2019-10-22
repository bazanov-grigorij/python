import random, time

# Вступление
def intro ():
    print('''
    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры
    В одной из них - дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.
    ''')

# Выбор пещеры
def chooseCave():
    print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
    user_cave = int(input())
    return user_cave

# Проверка пещеры
def checkCave(cave):
    friendly_cave = random.randint(1, 2)

    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    time.sleep(2)

    if cave == friendly_cave:
        print('делиться с вами своими сокровищами')
    else:
        print('моментально вас съедает')

play_again = 'да'
intro()

while play_again == 'да':
    checkCave(chooseCave())
    print('Сыграем ещё? (да или нет)')
    play_again = input()
