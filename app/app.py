from time import sleep
from playsound import playsound

from random import randint

import openpyxl
import threading


number_of_seconds = 0


def countdown(number_of_minutes: int) -> None:
    """Воспроизводит:
    1) таймер для обратного отсчёта времени;
    2) звуковое оповещение;
    3) текстовое оповещение.

    Args:
          number_of_minutes(int): Количество минут для чтения.

    Returns: None
    """
    global number_of_seconds
    number_of_seconds = number_of_minutes * 60
    while number_of_seconds:
        number_of_seconds -= 1
        sleep(1)

    play_sound()
    print_dashes(1, 0)
    print_final_message()


def play_sound() -> None:
    """Воспроизводит звуковое оповещение."""
    playsound('uwu_sound.mp3')


def print_final_message() -> None:
    """Печатает сообщение об окончании времени."""
    print('\nВремя закончилось!')


def print_dashes(empty_lines_before: int = 1,
                 empty_lines_after: int = 1) -> None:
    """Печатает знаки тире (---).

    В зависимости от введённых аргументов функция имеет возможность
    добавить пустые строки между знаками тире.

    Args:
        empty_lines_before(int): Пустые строки до печати тире.
        empty_lines_after(int): Пустые строки после печати тире.

    Returns: None
    """
    if empty_lines_before < 0 or empty_lines_after < 0:
        raise ValueError("Строки 'до' и 'после' должны быть >= 0!")

    elif empty_lines_before and empty_lines_after:
        print()
        print('-' * 115)
        print()

    elif empty_lines_before == 1 and empty_lines_after == 0:
        print()
        print('-' * 115)

    elif empty_lines_before == 0 and empty_lines_after == 1:
        print('-' * 115)
        print()

    elif empty_lines_before == 0 and empty_lines_after == 0:
        print('-' * 115)


# Получение данных из книги Excel.
book = openpyxl.load_workbook('patters.xlsx')
sheet = book.active


# Запись данных из Excel в словарь Python.
patters = dict()
for row in range(1, sheet.max_row):
    # Заполнение словаря скороговорками из листа.
    patters[row] = sheet[row + 1][1].value.splitlines()


# Вывод руководства по использованию программы.
tutorial = """\n\t\tРуководство к программе\n
\tДанная программа предназначена для тренировки дикции.\n
\tВ самом начале укажите время, необходимое для прохождения тренировки.\n
\tЗатем после прочтения скороговорки нажмите клавишу <Enter>, чтобы
перейти к следующей скороговорке.\n
\tПо окончании тренировки вы услышите звук оповещения и увидите, сколько
скороговорок вы успели прочитать за введённое вами время."""
print(tutorial)
print_dashes()


# Ввод времени.
while True:
    try:
        numberOfMinutes = int(input('Введите время (в минутах): '))
        break
    except ValueError:
        print('\nВы ввели не целочисленное значение!\n')

print_dashes()


# Запуск фонового таймера.
countdown_thread = threading.Thread(target=countdown, args=(numberOfMinutes,))
countdown_thread.start()

# Список, в который будут заноситься использованные скороговорки.
keys = []
# Количество прочитанных скороговорок.
countPatters = 0

while number_of_seconds > 0:
    # Делаем столько итераций, сколько скороговорок есть в словаре.
    for i in range(len(patters)):
        # Выбираем случайную скороговорку.
        key = randint(1, len(patters))

        # Если скороговорка уже была, то
        while key in keys:
            # заново выбираем случайную скороговорку
            key = randint(1, len(patters))
        else:
            # иначе помечаем скороговорку как прочитанную.
            keys.append(key)

        # Так как в словаре есть списки с 2-мя и более количеством
        # строк, то необходимо вывести каждое предложение скороговорки
        # на новой строке.
        for k in patters[key]:
            # Вывод каждой строки в списке.
            print(k)

        countPatters += 1

        # Любой ввод, чтобы понять, что чтение текущей скороговорки окончено.
        anyInput = input()
        print_dashes(0, 1)

        if number_of_seconds == 0:
            break

print(f'Количество прочитанных скороговорок: {countPatters}')
print_dashes(1, 0)
