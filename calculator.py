while True:
    try:
        num, operator, num2 = get_input_data()
        if operator == '+':
            print('Результат операции:', add(num, num2))
        elif operator == '-':
            print('Результат операции:', sub(num, num2))
        elif operator == '*':
            print('Результат операции:', mult(num, num2))
        elif operator == '/':
            if num2 == 0:
                print('Деление на ноль!')
            else:
                print('Результат операции:', div(num, num2))
        elif operator == '%':
            print('Результат операции:', mod(num, num2))
        else:
            print('Ошибка! Некорректный оператор.')
    except ValueError:
        print('Ошибка ввода! Введите число.')
