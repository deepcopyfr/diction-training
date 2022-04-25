<h1>
    <p align="center"> Тренировка дикции </p>
</h1>

Программа выводит скороговорки для тренировки дикции.

>Искусство оратора прежде всего заключается в том, чтобы никто не замечал искусства.


## Как начать пользоваться

### Установка

1. Клонируйте репозиторий </br>

`$ git clone git@github.com:deepcopyfr/diction-training.git`

2. Перейдите в каталог

`cd dictiong-training`

3. Создайте виртаульное окружение и активируйте его

```
$ python3 -m venv env
$ source venv/bin/activate
```

4. Установите зависимости

```
pip install -U pip
pip install -r requirements.txt
```

5. Запустите **app.py**


### Использование

В самом начале укажите время, необходимое для прохождения тренировки. </br>

![](https://github.com/deepcopyfr/diction-training/blob/master/GIFs/input_time.gif)

Затем после прочтения скороговорки нажмите клавишу `Enter`, чтобы
перейти к следующей скороговорке. <br>

![](https://github.com/deepcopyfr/diction-training/blob/master/GIFs/print_message.gif)
![](https://github.com/deepcopyfr/diction-training/blob/master/GIFs/print_patters.gif)

По окончании тренировки вы услышите звук оповещения и увидите, сколько
скороговорок вы успели прочитать за введённое вами время. </br>

![](https://github.com/deepcopyfr/diction-training/blob/master/GIFs/print_message.gif)


### Добавление новых скороговорок
Чтобы добавить новые скороговорки, необходимо:
1. скопировать откуда угодно нужные скороговорки
2. открыть **patters.xlsx** 
3. в столбец "Скороговорка" вставить скороговорки
4. столбец "N" растянуть до последней скороговорки, чтобы установить нумерацию
5. для читабельности установите высоту каждой новой строки 2.0.

![](https://github.com/deepcopyfr/diction-training/blob/master/GIFs/work_with_excel_file.gif)

Если скороговорка состоит из нескольких строк (как стих), вставьте её </br>
отдельно, предварительно нажав  клавишу `F2` на нужную ячейку.


## Лицензия

**Тренировка дикции** — это программное обеспечение с открытым исходным кодом,
распространяемое по лицензии **MIT**.
