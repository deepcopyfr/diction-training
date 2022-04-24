from playsound import playsound
from openpyxl import worksheet


def play_sound() -> None:
    """Воспроизводит звуковое оповещение."""
    playsound('ding_sound.mp3')


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


def print_tutorial() -> None:
    """Вывод руководства по использованию программы."""
    tutorial = """\n\t\tРуководство к программе\n
    \tДанная программа предназначена для тренировки дикции.\n
    \tВ самом начале укажите время, необходимое для прохождения тренировки.\n
    \tЗатем после прочтения скороговорки нажмите клавишу <Enter>, чтобы
    перейти к следующей скороговорке.\n
    \tПо окончании тренировки вы услышите звук оповещения и увидите, сколько
    скороговорок вы успели прочитать за введённое вами время."""
    print(tutorial)
    print_dashes()


def convert_from_excel_to_dict(sheet_with_patters: worksheet) -> dict:
    """Перевод данных из Excel в словарь Python.

    Args:
        sheet_with_patters(openpyxl.sheet): Лист книги Excel со скороговорками.

    Returns:
        Словарь со скороговорками.
    """
    patters = dict()
    for row in range(1, sheet_with_patters.max_row):
        # Заполнение словаря скороговорками из листа.
        patters[row] = sheet_with_patters[row + 1][1].value.splitlines()
    return patters
