import random
import time


class character():
    health = 4
    attack = 2
    defense = 1
    def __init__(self, username):
        self.username = username
    def getCharacter(self, health, attack, defense):
        print(f'Привет, мое имя: {self.username}\n *** \nЗдоровье: {health}\nАтака: {attack} \nЗащита: {defense} \n ***')


class wizard(character):
    def __init__(self, username):
        character.__init__(self, username)
        character.attack += 1.2
        character.getCharacter(self, character.health, character.attack, character.defense)
    def getClass(self):
        print('Вы выбрали класс: Маг')


class warrior(character):
    def __init__(self, username):
        character.__init__(self, username)
        character.health += 1.5
        character.getCharacter(self, character.health, character.attack, character.defense)
    def getClass(self):
        print('Вы выбрали класс: Воин')


class healer(character):
    def __init__(self, username):
        character.__init__(self, username)
        character.defense += 1.1
        character.getCharacter(self, character.health, character.attack, character.defense)
    def getClass(self):
        print('Вы выбрали класс: Целитель')


class character_improved(character):
    critical_damage = 0.4
    avoidance = 0.2
    def __init__(self, element):
        self.element = element
    def getCharacter_improved(self, critical_damage, avoidance):
        print(f'Крит. урон: {critical_damage}\nУклонение: {avoidance} \nСтихия: {self.element} \n ***')


class wizard_improved(character_improved):
    def __init__(self, username, element):
        wizard.__init__(self, username)
        character_improved.__init__(self, element)
        character_improved.getCharacter_improved(
            self, character_improved.critical_damage, character_improved.avoidance)


class warrior_improved(character_improved):
    def __init__(self, username, element):
        warrior.__init__(self, username)
        character_improved.__init__(self, element)
        character_improved.getCharacter_improved(
            self, character_improved.critical_damage, character_improved.avoidance)


class healer_improved(character_improved):
    def __init__(self, username, element):
        healer.__init__(self, username)
        character_improved.__init__(self, element)
        character_improved.getCharacter_improved(
            self, character_improved.critical_damage, character_improved.avoidance)


def create_character(user_class = False, user_improve = False):
    input_error = '⚠️ Произошла ошибка ввода'
    while user_class == False:
        user_class = input('Выберите класс персонажа: ' + ' маг (wizard)' + ' воин (warrior)' + ' целитель (healer): ')
        if user_class == 'wizard' or user_class == 'маг':
            username = input('Введите имя: ')
            user_character = wizard(username)
            user_character.getClass()
        elif user_class == 'warrior' or user_class == 'воин':
            username = input('Введите имя: ')
            user_character = warrior(username)
            user_character.getClass()
        elif user_class == 'healer' or user_class == 'целитель':
            username = input('Введите имя: ')
            user_character = healer(username)
            user_character.getClass()
        else:
            user_class = False
            print(input_error)
    while user_improve == False:
        user_improve = input('Вы хотите улучшить своего персонажа? (y/n): ')
        if user_improve == 'y':
            element = input('Введите стихию: ')
            if user_class == 'wizard' or user_class == 'маг':
                user_character = wizard_improved(username, element)
            elif user_class == 'warrior' or user_class == 'воин':
                user_character = warrior_improved(username, element)
            elif user_class == 'healer' or user_class == 'целитель':
                user_character = healer_improved(username, element)
            return user_character
        elif user_improve == 'n':
            print('Вы не улучшили персонажа, как этот задрот может драться? Конец программы')
            return False
        else:
            user_improve = False
            print(input_error)


def fight_character(user_1, user_2):
    while user_1.health and user_2.health >= 0:
        print(f' ***\nHP {user_1.username}: {round(user_1.health, 2)} \nHP {user_2.username}: {round(user_2.health, 2)}\n ***')
        if bool(random.getrandbits(1)) == True:
            if bool(random.getrandbits(1)) == True:
                hit = user_1.attack + user_1.critical_damage - user_2.defense
                print(f'{user_1.username} нанес критический урон [{round(hit, 2)}] по {user_2.username}')
                user_2.health = user_2.health - hit
            else:
                hit = user_1.attack - user_2.defense
                print(f'{user_1.username} нанес урон [{round(hit, 2)}] по {user_2.username}')
            user_2.health = user_2.health - hit
        else: print(f'{user_1.username} промахнулся по {user_2.username}')
        if user_2.health <= 0:
            user_2.health = 0
            break
        time.sleep(1)
        if bool(random.getrandbits(1)) == True:
            if bool(random.getrandbits(1)) == True:
                hit = user_2.attack + user_2.critical_damage - user_1.defense
                print(f'{user_2.username} нанес критический урон [{round(hit, 2)}] по {user_1.username}')
                user_1.health = user_1.health - hit
            else:
                hit = user_2.attack - user_1.defense
                print(f'{user_2.username} нанес урон [{round(hit, 2)}] по {user_1.username}')
            user_1.health = user_1.health - hit
        else: print(f'{user_2.username} промахнулся по {user_1.username}')
        time.sleep(1)
        if user_1.health <= 0:
            user_1.health = 0
            break
    if user_1.health <= user_2.health: user_winner = user_2.username
    elif user_1.health >= user_2.health: user_winner = user_1.username
    print(f' ***\nHP {user_1.username}: {round(user_1.health, 2)} \nHP {user_2.username}: {round(user_2.health, 2)}\n ***')
    print(f'Победу в битве одержал: {user_winner}')

print('Персонаж 1: ')
user_1 = create_character()
if user_1 != False:
    print('Персонаж 2: ')
    user_2 = create_character()
    if user_2 != False:
        fight_character(user_1, user_2)