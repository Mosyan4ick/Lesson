import random
print("Первый номер \n\n\n")

def buble_sort(a):
    '''
    Сортировка пузырьком

    >>> buble_sort([717, -527, 910, -698, -27, 276, -6, -903, 179, 568, -18, 977, 521, -950, -167, -849, 757, -962, -591, -332])
    [-962, -950, -903, -849, -698, -591, -527, -332, -167, -27, -18, -6, 179, 276, 521, 568, 717, 757, 910, 977]
    >>> buble_sort([-429, -518, 434, -891, 738, -955, -290, -582, -177, 172])
    [-955, -891, -582, -518, -429, -290, -177, 172, 434, 738]
    >>> buble_sort([6, -49, -38, 25, 19])
    [-49, -38, 6, 19, 25]

    :param a: Не отсортированный список a
    :return: Результатом является список, отсортированный по средством алгоритма сортировки "Пузырьком".
    '''
    f = False
    for i in range(len(a)):
        f = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                f = True
        if not f:
            break
    return a


help(buble_sort)
lst = [random.randint(-49, 51) for i in range(10)]
print(f"Исходный список: {lst}")
print(f"Отсортированный список: {buble_sort(lst)}")


def transformation(color):
    '''
    Преобразование кода цвета

    >>> transformation(255)
    'ff'
    >>> transformation(15)
    '0f'
    >>> transformation(8)
    '08'

    :param color: Код цвета (0-255)
    :return: Строковое обозначение кода цвета в 16 ричной системе (от 00 до FF)
    '''

    if color < 16:
        return "0" + str(hex(color)[2:])
    else:
        return str(hex(color)[2:])


print('\n')
print("Второй номер \n\n\n")
print("Код закомментирован, т.к. требует много ресурсов. Ответ лежит в файле rgb.txt. Полная версия файла находится в облаке по ссылке в комментариях внутри кода.")
help(transformation)
#file = open('rgb.txt', 'w')
#rgb = {}
#for red in range(256):
#    for green in range(256):
#        for blue in range(256):
#           rgb[transformation(red) + transformation(green) + transformation(blue)] = (red, green, blue)
#
#file.write(str(rgb)[1:-1])
#file.close()
# Результатом работы кода является файл rgb.txt.
# По причине того, что выполнение требует много ресурсов я закомментировал этот участок кода. 
# Вы можете проверить по результату или раскомментировав код. Если слишком усложнил, приношу свои извинения.
# Полный файл я загрузил в облако: https://drive.google.com/drive/folders/1Hcto8gYTR6B7ov668EW7MSdoaianNKV3?usp=sharing
# Короткую версию файла прикрепил в github. (В короткой использовал red до 128 green до 64 blue до 64)

print("Третий номер \n\n\n")
set_one = {random.randint(-19, 20) for k in range(25)}
set_two = {random.randint(-19, 20) for j in range(25)}
print(f'Набор №1: \n{set_one} \n'
      f'Набор №2: \n{set_two} \n'
      f'Одновременно в оба: \n{set_one & set_two} \n'
      f'Входят в первое, но не входят во второе: \n{set_one - set_two} \n'
      f'Входят во второе, но не входят в первое: \n{set_two - set_one} \n'
      f'Множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих: \n{set_one ^ set_two} \n')

print("Четвертый номер \n\n\n")

inventory = []
inventory_volume = 10


def inventory_weight_sum():
    '''
    Считает суммарный вес инвентаря

    :return: Сумма веса всех предметов в инвентаре
    '''
    global inventory
    summ = 0
    for indx in range(len(inventory)):
        summ += list(inventory[indx].items())[0][1]
    return summ


def inventory_add(item_name, item_weight):
    '''
    Добавляет предмет в инвентарь

    :param item_name: Наименование предмета
    :param item_weight: Вес предмета
    '''
    global inventory, inventory_volume
    if item_weight + inventory_weight_sum() <= inventory_volume:
        inventory.append({item_name: item_weight})
    else:
        print("В инвентаре нет места. Слишком тяжелый предмет.")


print("Добрый день. \n"
      "Игра 'Инвентарь'.\n"
      "Правила игры:\n"
      f"Вы имеете {inventory_volume} кг доступного объема\n"
      "Вы можете:\n"
      "Добавить новый предмет\n"
      "Удалить уже лежащий в инвентаре предмет\n"
      "Посмотреть содержимое инвентаря\n"
      "Для добавления используйте команду '+'\n"
      "Для удаления используйте команду '-'\n"
      "Для отображения содержимого инвентаря используйте команду '*'\n"
      "Для завершения игры используйте команду 'Конец'\n"
      "\n"
      "Ввод команд выполняется следующим образом:\n"
      "[действие] [наименование] [вес в кг]\n"
      "Пример:\n"
      "+ камень 0.1\n"
      "\n"
      "-\n"
      " Выберите содержимое инвентаря которое хотите удалить:\n"
      " 0: {'конфета': 2.0}\n"
      "0\n"
      "\n"
      "*\n"
      " Содержимое инвентаря:\n"
      " [{'конфета': 2.0}]\n"
      " На текущий момент занято 2.0 кг, а доступно 8.0 кг\n"
      "\n"
      "Обязательно разделяйте действие/наименование/вес пробелами, иначе выдаст ошибку\n"
      "Приятной игры!\n")
while True:

    item = input("Необходимые действия: ").split(" ")
    if item[0] == 'Конец':
        break
    elif item[0] == "+":
        try:
            if float(item[2]) > 0:
                inventory_add(item[1], float(item[2]))
            else:
                print("Данные введены некорректно")
                continue
        except:
            print("Данные введены некорректно")
            continue
    elif item[0] == "-":
        print(f"Выберите содержимое инвентаря которое хотите удалить:")
        for itm in range(len(inventory)):
            print(f"{itm + 1}: {inventory[itm]}")
        try:
            selection_of_the_deleted = int(input())
        except:
            print("Неверно введен номер")
            continue
        inventory.pop(selection_of_the_deleted - 1)
    elif item[0] == "*":
        iws = inventory_weight_sum()
        print(f"Содержимое инвентаря:\n{inventory}\n"
              f"На текущий момент занято {iws} кг, а доступно {inventory_volume - iws} кг")
