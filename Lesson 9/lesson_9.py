di = dict()
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

def password(string):
    if len(string) < 6:
        print('Пароль должен содержать 6 и более символов!')
        return False
    elif string.isdigit():
        print('Пароль должен состоять не только из цифр!')
        return False
    elif (set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) & set(string)) == set():
        print('Пароль должен содержать хотя бы 1 цифру!')
        return False
    elif 'password' in string.lower():
        print('Пароль не должен содержать слово "password"!')
        return False
    else:
        return True