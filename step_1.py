from random import randint
from random import uniform
from time import sleep
from actions import *
from data import *

# записывает игрока
name = input('Введи своё имя, путник: ')
player['name'] = name


while True:
    action = int(input(f'Выберите действие: 1 - Бой, 2 - Тренировка, 3 - Лавка Бабы Зины: '))
    print()
    if action == 1:
        fight()
    elif action == 2:
        train()
    elif action == 3:
        shop()    
    