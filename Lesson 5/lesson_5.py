# Номер 1
passwd = input("Введите пароль: ")


def check(word):
    """Провряет введенный пароль на правильность:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
    Возвращает значение True, если все правильно
    
    Ключевые аргументы:
    word -- слово пароль
    """
    if len(word) < 6:
        print('Пароль должен содержать 6 и более символов!')
        return False
    elif word.isdigit():
        print('Пароль должен состоять не только из цифр!')
        return False
    elif (set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) & set(word)) == set():
        print('Пароль должен содержать хотя бы 1 цифру!')
        return False
    elif 'password' in word.lower():
        print('Пароль не должен содержать слово "password"!')
        return False
    else:
        return True


print(f'Пароль {check(passwd)}')
# Номер 2
el_ments = input("Введите суммируемые данные через пробел: ").split(' ')


def sum_all_elem(*args):
    """ Считает и выводит сумму аргументов

    Ключевые арументы:
    args -- кортеж суммируемых аргументов
    """
    if args[0][0].isdigit():
        return sum([float(i) for i in args[0]])
    elif not args[0][0].isdigit():
        try:
            map(float, args[0])
            sum_elem = 0
            for elem in args[0]:
                sum_elem += float(elem)
            return sum_elem
        except:
            sum_elem = ''
            for elem in args[0]:
                sum_elem += elem
            return sum_elem


print(f'Сумма элементов равна {sum_all_elem(el_ments)}')
# Номер 3
di = dict()
try:
    number = int(input("Введите номер числа Фибоначчи: "))
    if number < 0:
        raise ValueError
except ValueError:
    print("Неверно введено значение")
    exit()


def fib(n):
    """Считает и выводит число Фибоначчи, имеющее порядковый номер n

    Ключевые аргументы:
    n -- порядковый номер числа Фибоначчи
    """
    global di
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n in di.keys():
        return di.get(n)
    di[n] = fib(n-2) + fib(n-1)
    return fib(n-2) + fib(n-1)


print(f'Нужное Вам число: {fib(number)}')
print("\nДля демонстрации скорости вот подсчет чисел Фибоначчи под номером\n")
print(f'50: {fib(50)}')
print(f'100: {fib(100)}')
print(f'400: {fib(400)}')
print(f'1000: {fib(1000)}')
