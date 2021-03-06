import math
import cmath

print("Номер 1")
# Номер 1
print(
    "   Ходилка \n"
    "Возможные действия:\n"
    "Вверх\n"
    "Вниз\n"
    "Влево\n"
    "Вправо\n"
    "Все действия вводить в формате 'Куда насколько': Вниз 5\n"
    "Шаг указывать в кол-ве позиций(целое число)")
Fx, Fy = 0, 0
print(f"Ваше местоположение {Fx}, {Fy}")
move = input("Напишите, куда хотите сдвинуться: ").split(" ")
try:
    if move[0] == "Вверх":
        Fy += int(move[1])
    elif move[0] == "Вниз":
        Fy -= int(move[1])
    elif move[0] == "Вправо":
        Fx += int(move[1])
    elif move[0] == "Влево":
        Fx -= int(move[1])
    else:
        exit()  # Для попадания в исключение
except:
    print(
        "Введенные данные не соответствуют правилам \n"
        "(Можно использовать: 'Вверх', 'Вниз', 'Вправо', 'Влево' и целые числа)")
    exit()

print(f"Ваше местоположение {Fx}, {Fy}")

print("\n \n \nНомер 2")
# Номер 2
print(
    "   Ходилка \n"
    "Возможные действия:\n"
    "Вверх\n"
    "Вниз\n"
    "Влево\n"
    "Вправо\n"
    "Все действия вводить в формате 'Куда насколько': Вниз 5\n"
    "Шаг указывать в кол-ве позиций(целое число) \n"
    "Для завершения игры используйте 'Конец' или 'End'")
Fx, Fy = 0, 0
while True:
    print(f"Ваше местоположение {Fx}, {Fy}")
    move = input("Напишите, куда хотите сдвинуться: ").split(" ")
    if (move[0] == "Конец") or (move[0] == "End"):
        print("☻ Спасибо за игру! ☺")
        break
    try:
        if move[0] == "Вверх":
            Fy += int(move[1])
        elif move[0] == "Вниз":
            Fy -= int(move[1])
        elif move[0] == "Вправо":
            Fx += int(move[1])
        elif move[0] == "Влево":
            Fx -= int(move[1])
        else:
            exit()  # Для вызова исключения
    except:
        print(
            "Введенные данные не соответствуют правилам \n"
            "(Можно использовать: 'Вверх', 'Вниз', 'Вправо', 'Влево', 'Конец', 'End' и целые числа)")
        exit()

print("\n \n \nНомер 3 и 4")

# Примеры:
# ДВА КОРНЯ: 1 4 3 0
# ОДИН КОРЕНЬ: 3 -18 27 0
# КОРНИ - КОМПЛЕКСНЫЕ ЧИСЛА: 1 -6 34 0
print(" Квадратное уравнение \n"
      "ax^2 + bx + c = d")
F = list(map(float, input("Введите коэфициенты уравнения в формате 'a b c d' через пробел: ").split(" ")))
F[2] = F[2] - F[3]
F = F[:-1]
if F[0] == 0 and F[1] != 0:
    print(f"Корень уравнения = {-F[2] / F[1]}")
elif F[0] == 0 and F[1] == 0:
    print("Уравнения не существует")
dis = math.pow(F[1], 2) - 4*F[0]*F[2]
print(f"Дискриминант = {dis}")
if dis > 0:
    print(f"Первый корень уравнения = {(-F[1] + math.sqrt(dis)) / (2*F[0])}")
    print(f"Второй корень уравнения = {(-F[1] - math.sqrt(dis)) / (2*F[0])}")
elif dis == 0:
    print(f"Корень уравнения = {(-F[1]) / (2*F[0])}")
else:
    print(f"Первый корень уравнения = {(-F[1] + complex(cmath.sqrt(dis))) / (2*F[0])}")
    print(f"Второй корень уравнения = {(-F[1] - complex(cmath.sqrt(dis))) / (2*F[0])}")
