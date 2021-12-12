# Номер 1
try:
    count = int(input('Введите кол-во строк: '))
    if count < 0:
        raise ValueError
    if count > 0:
        print("Вводите необходимые строки, разделяя их клавишей 'Enter'")
        text_lines = []
except ValueError:
    print("Для ввода используются только целые числа")

for line in range(count):
    text_lines.append(input().split(' '))


def string_to_bytes(list_line):
    """Переводит все строки списка в байт-представление.
    
    Ключевые аргументы:
    list_line -- переводимый список
    """
    for word in range(len(list_line)):
        list_line[word] = list_line[word].encode('utf-8')


def bytes_to_string(list_bytes):
    """Переводит все байт-представления строк в строки

    Ключевые аргументы:
    list_bytes -- список байт-представлений строк
    """
    for word in range(len(list_bytes)):
        list_bytes[word] = list_bytes[word].decode('utf-8')


def view(list):
    view_string = ''
    len_list = len(list)
    for word in range(len_list):
        view_string += str(list[word])
        if word != len_list-1:
            view_string += " "
    return view_string


if count > 0:
    print(f"\nСтроки преобразованные в байты: ")
    for i in text_lines:
        print(f'\tИсходная строка: {view(i)}')
        string_to_bytes(i)
        print(f'\tЗакодированная строка: {view(i)}\n')

    print(f"\nБайты преобразованные в строки: ")
    for i in text_lines:
        print(f'\tЗакодированная строка: {view(i)}')
        bytes_to_string(i)
        print(f'\tИсходная строка: {view(i)}\n')

# Номер 2
try:
    with open('input.txt', 'r') as f_r:
        text_f_r = f_r.read()
    f_wr = open('output.txt', 'w')
    count_alcohol = list(map(int, text_f_r.split(' ')))
    f_wr.write(f'The number of molecules is {min(count_alcohol[0]//2, count_alcohol[1]//6, count_alcohol[2]//1)}')
    f_r.close()
    f_wr.close()
except FileNotFoundError:
    print("Создайте файл input.txt и поместите данные по C, H, O через пробел")
except ValueError:
    print("Файл input.txt должен содержать 3 целых числа через пробел(кол-во атомов C, H, O, соответственно)")
except IndexError:
    print("Файл input.txt должен содержать 3 целых числа через пробел(кол-во атомов C, H, O, соответственно)")
