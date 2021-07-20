import numpy as np


def game_core(number):
    """ Работа функции заключается в том, что каждую итерацию мы сокращаем колличество возможных вариантов в два раза,
    меняя переменные min_num(минимальное возможное загаданное число) и max_num (максимальное возможное загаданное число)
    на переменную prediction, которая изменяется в зависиости от значений min_num и max_num являясь среднеарифметическим
     их суммы """
    min_num = 1
    max_num = 101  # Ставится 101, вместо 100 из-за особеностей целочисленного деления
    prediction = 50
    count = 0  # Счетчик колличества попыток
    while number != prediction:
        count += 1
        if number > prediction:
            min_num = prediction
            prediction = (max_num + min_num) // 2
        elif number < prediction:
            max_num = prediction
            prediction = (max_num + min_num) // 2
    return count


def score_game(core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
