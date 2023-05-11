# подключить 4 файла

# ключевое True:
    # ключевое слово:
        num, operator, num2 = get_input_data()
        if operator == '+':
            print('Результат операции:', add(num, num2))
        elif operator == '-':
            print('Результат операции:', sub(num, num2))
        elif operator == '*':
            print('Результат операции:', mult(num, num2))
        else:
            print('Ошибка! Некорректный оператор.')
    #ключевое слово  ValueError:
        print('Ошибка ввода! Введите число.')