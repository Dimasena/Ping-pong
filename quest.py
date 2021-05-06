import time, random, sys, inspect, pygame
# print(inspect.getsourcefile(random))

def super_print(a):
    for i in a:
        print(i, end='', flush=True)
        time.sleep(0.03)
    print()

def narcissistic(value):
    str_value = str(value)
    length = len(str_value)
    result = 0
    for i in str_value:
        result += int(i)**length
    return result == value


def death(hunger_lose, time_limit_lose):
    global hunger, time_limit
    hunger -= hunger_lose
    time_limit -= time_limit_lose
    if hunger < 0:
        super_print('Ты умер, от недостатка еды')
    elif time_limit < 0:
        super_print(f'Ты умер, от бури {storm_name}')
    else:
        super_print(f'Осталось времени: {time_limit}')
        super_print(f'Осталось припасов: {hunger}')


time_limit = 30
hunger = 40

pygame.mixer.init()
soundtrack = pygame.mixer.Sound('b4d2f6fbda4f739.mp3')
soundtrack.set_volume(0.5)
soundtrack.play(-1)

super_print('Вы вылетели в космос и в вас попал астероид. Вы потерпели крушение на планете!')
super_print('Введите ваши данные для управления кораблем')
name = input('Имя: ')
name_planet = input('Введите название планеты: ')
super_print(f'Капитан, {name}! Мы приземлились на планете {name_planet}. Корабль больше не в состоянии взлететь. Необходимо провести вылазку в поисках ресурсов.')
super_print(f'Вы хотите остаться на планете {name_planet} или начать починку корабля?')

while True:
    choice_1 = input('остаться/ улететь: ').lower()
    if choice_1 == 'остаться':
        super_print(f'Капитан, {name}! Вы решили остаться на планете {name_planet} и построить здесь свою колонию!')
        storm_name = input('Наши ученые нашли бурю под названием... ')
        super_print(f'Через 30 дней буря {storm_name} прилетит и не оставит живого места, мы можем создать город и большой щит, который должен будет защитить от бури')

        # Квест 1
        super_print('Наша первая цель: добыть глину')
        choice_2 = int(input('1) Отправиться к ближайшему озеру/ 2) отправиться в горы \nВыберите 1 или 2 '))
        if choice_2 == 2:
            death(1, 1)
            super_print('Мы потеряли время, на горе нет глины')
            choice_2 = 1

        if choice_2 == 1:
            game_done = False
            super_print('Спустя 1-ни сутки вы пришли к озеру')
            super_print('Ура, капитан! Мы добрались до источника глины, но для того, чтобы нам перевезти глину к месту крушения корабля понадобится 5 дней, но мы можем ускорить процесс, построив робота. Что прикажете делать?')
            while True:
                choice_3=int(input('Построить робота/ приказать команде нести в руках \nВыберите 1 или 2 '))
                if choice_3 == 2:
                    random_game = random.randint(1, 2)
                    print(random_game)
                    if random_game==1:
                        super_print('Вам повезло, погода сегодня была дождливая и команда успешно перевезла глину через 5 дней')
                        break
                    else:
                        super_print('Вам не повезло, наступил период была засуха и глина затвердела, придется идти назад')
                    death(10, 5)

                elif choice_3 == 1:
                    while True:
                        random_game = random.randint(0, 10)
                        super_print(f'Чтобы запрограммировать робота вам нужно перевести число на дисплее в двоичный код. Бип-буп, {random_game}.')
                        game = input('Введите число: ')
                        if game == format(random_game, 'b'):
                            super_print(f'Капитан, {name}! Вы успешно запрограммировали робота и он доставил глину до нужного места за 1 день')
                            game_done = True
                            break
                        else:
                            super_print('Вы не справились, попробуйте еще раз')
                            super_print(f'Дней до бури: {time_limit}')
                        death(hunger, time_limit)

                if game_done:
                    break
        # Квест 2
        super_print('Люди постепенно начали строить поселение')
        super_print('Мы начали выкапывать ямы и нашли неизвестную технологию, на ней есть цветовой код и вы должны его разгадать')
        try_again= True
        while try_again:
            choice_4 = int(input('Вы хотите сами разгадать код или предоставить команде, но они недостаточно умны для этого \nВыберите 1 или 2 '))
            if choice_4 == 1:
                super_print('На экране вы видите цвет и вы должны перевести на русский')
                colors = {'(255, 0, 255 )': 'фиолетовый', '(255, 145, 0)': 'оранжевый', '(255, 255, 0)': 'жёлтый', '(0, 0, 0)':'чёрный', '(255, 255, 255)':'белый', '(0, 255, 0)':'зелёный', '(0, 0, 255)': 'синий', '(255, 0, 0)': 'красный'}
                color_wins = 0
                while color_wins < 3:
                    computer_choice = random.choice(list(colors.items()))
                    game_choice = input(f'{computer_choice[0]}: ')
                    if game_choice == computer_choice[1]:
                        super_print('Молодец! Ты смог!')
                        color_wins += 1
                        try_again = False

                    else:
                        color_wins = 0
                        super_print('Не молодец! Заново')
                        death(3, 2)
            else:
                random_game1 = random.randint(1, 3)
                if random_game1 == 2:
                    super_print('Тебе повезло, они смогли решить задачу')
                    death(2, 1)
                    try_again = False
                else:
                    super_print('Не повезло, команда не справилась')
                    death(2, 1)



        super_print('Глава 3. Рассвет')
        super_print('Почти все готово! Осталось найти источник питания, для такого объема питания понадобится сильнейший двигатель')
        super_print('Чтобы его достать потребуется пройти квест')
        super_print('Задача такова:\nНадо написать 3 сомовлюбленных чисел')
        n = 0
        while n < 3:
            choice = input('Введи число: ')
            if narcissistic(choice) == True:
                super_print(f'Молодец! Ты смог!')
                n += 1
            else:
                super_print('Не молодец! Заново.')
                n = 0
                death(2, 3)

        time.sleep(2)
        super_print('Вы слышите, как запитывается найденная вами технология и лёгкое сияние начинает распространяться в стороны от вас.')
        super_print('В конечном итоге оно выходит далеко за пределы вашего поселения и со временем останавливается')
        super_print('Ваши учёные говорят, что эта технология - силовой щит, способный защитить нас от бури.')
        super_print(f'Капитан, {name}! Ваша колония может развиваться на планете {name_planet} ничего не страшась.')
        super_print('Поздравляем, вы смогли основать процветающую колонию!')

    elif choice_1 == 'улететь':
        pass
    else:
        super_print(f'Капитан, {name}! Мы вас не поняли')
'''n = int(input())

suma = 0

while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10

print("Сумма:", suma)'''
