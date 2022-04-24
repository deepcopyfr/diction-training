from time import sleep

from random import randint

import functions
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

    functions.play_sound()
    functions.print_dashes(1, 0)
    functions.print_final_message()


# Получение данных из книги Excel.
book = openpyxl.load_workbook('patters.xlsx')
sheet = book.active

# Переносим скороговорки из листа Excel в словарь Python.
patters = functions.convert_from_excel_to_dict(sheet)

# Вывод руководства к программе.
functions.print_tutorial()

# Проверка на "дурака" при вводе времени.
while True:
    try:
        numberOfMinutes = int(input('Введите время (в минутах): '))
        break
    except ValueError:
        print('\nВы ввели не целочисленное значение!\n')

functions.print_dashes()

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
        functions.print_dashes(0, 1)

        if number_of_seconds == 0:
            break

print(f'Количество прочитанных скороговорок: {countPatters}')
functions.print_dashes(1, 0)
