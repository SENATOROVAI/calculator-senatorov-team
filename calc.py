from addition import add
from run import get_input_data
from subtraction import sub
from multiplication import mult

while True:
    num = float(input('Введите число: '))
    operator = input('Введите операцию: ')
    num2 = float(input('Введите число: '))
    # ключевое слово:
#          переменная, переменная, переменная = фукнция()
        if operator == '+':
            print('Результат операции:', add(?))
        elif operator == '-':
            print('Результат операции:', sub(?))
        elif operator == '*':
            print('Результат операции:', mult(?))
        else:
            print('Ошибка! Некорректный оператор.')
    #ключевое слово  ValueError:
        print(?)
