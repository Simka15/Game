from data import *
from random import randint, uniform
from time import sleep

def fight():
        # пока хп есть и у игрока и у врага
        # рандомно выбираем врага
        current_enemy = randint(0, 2)

        # рандомное число 1 или 2
        round = randint(1, 2)

        # записали врага в enemy
        enemy = enemies[current_enemy]

        # записываем хп врага в перменную enemy_hp 
        enemy_hp = enemies[current_enemy]['hp']

        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()
        while player['hp'] > 0 and enemy_hp > 0:
            # если не четное аттакует игрок
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                # у врага отнимается жизнь, равная аттаке игрок
                # ЕСТЬ НЕСКОЛЬКО ВАРИАНТОВ ПРИДУМАТЬ СВОЙ 
                if 'зелье удачи' in player['inventory']:
                    rand_luck = randint(5, 20)
                    if player['luck'] == rand_luck:
                        print(f'Вам повезло! Ваша атака увеличена на 3 и составляет:{player["attack"]*3}')
                        enemy_hp -= player['attack'] * 3
                else:
                    enemy_hp -= player['attack']
                sleep(1)
                # пишем сколько хп у игрока и врага
                print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            # если не четное аттакует враг
            else:
                # аттакует враг
                print(f'{enemy["name"]} атакует {player["name"]}.')
                # у игрока отнимается жизнь, равная аттаке врага
                player['hp'] -= enemy['attack'] * player['armor'] # поглатили 5% урона с броней
                sleep(1)
                # пишем сколько хп у игрока и врага
                print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        # пишем кто победил
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

def train():
        choise = int(input(f'Что будем тренировать? 1 - броню, 2 - атаку: '))
        print()
        for i in range(0, 101, 20):
            print(f'Тренировака завершена на {i}%')
            sleep(1)
        if choise == 1:
            if player["armor"] < 0.99:
                new_ar = uniform(0, 0.3)
                player['armor'] -= new_ar
                print(f'Ваша броня после тренировки: {100 - player["armor"] * 100}%')
            else:
                 print(f'Броня прокачена на максимум: {player["armor"]}')
        elif choise == 2:
            if player["attack"] < 0.99:
                new_at = randint(1, 5)
                player['attack'] += new_at
                print(f'Ваша атака после тренировки: {player["attack"]}')
            else:
                print(f'Атака прокачена на максимум: {player["attack"]}')



def shop():
    # ДОБАВИТЬ ВЫХОД ИЗ МАГАЗИНА
    print('Добро пожаловать, путник! Я Баба Зина. Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in shop_items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    question = int(input("Хотите ли вы что-то купить? 1 - да, 2 - нет: "))
    if question == 1 :
        print(f'Напиши, что купить из этого')
    # записываем что хочет купить игрок
        item = input()
        # провряем нет ли уже этого предмета в интентаре 
        if item in player['inventory']:
            print(f'У тебя уже есть {shop_items[item]["name"]}')
        # иначе если хватает денег, то добавляем в инвентарь  
        elif player['money'] >= shop_items[item]['price']:
            print(f'Ты успешно купил {shop_items[item]["name"]}')
            # добавляем товар в инвентарь  
            player['inventory'].append(shop_items[item]["name"])
            # вычитаем деньги у игрока
            player['money'] -= shop_items[item]['price']
        else:
            print('Не хватает монет :(')
        print('\n')
    else :
        print('Буду ждать тебя снова, путник!')