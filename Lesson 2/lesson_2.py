import math

variable_1, variable_2 = map(float, input("Введите первое и второе значения через пробел: ").split(" "))
print(f"Операции для {variable_1}, {variable_2} \n"
      f"{variable_1} + {variable_2} = {variable_1 + variable_2} \n"
      f"{variable_1} - {variable_2} = {variable_1 - variable_2} \n"
      f"{variable_2} - {variable_1} = {variable_2 - variable_1} \n"
      f"{variable_1} * {variable_2} = {variable_1 * variable_2} \n"
      f"{variable_1} / {variable_2} = {variable_1 / variable_2 if variable_2 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_2} / {variable_1} = {variable_2 / variable_1 if variable_1 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_1} ** {variable_2} = {variable_1 ** variable_2} \n"
      f"{variable_2} ** {variable_1} = {variable_1 ** variable_2} \n"
      f"{variable_1} деление по модулю на {variable_2} = {abs(variable_1) / abs(variable_2) if variable_2 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_2} деление по модулю на {variable_1} = {abs(variable_2) / abs(variable_1) if variable_1 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_1} // {variable_2} = {variable_1 // variable_2 if variable_2 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_2} // {variable_1} = {variable_2 // variable_1 if variable_1 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_1} % {variable_2} = {variable_1 % variable_2 if variable_2 != 0 else 'Ошибка деления на 0'} \n"
      f"{variable_2} % {variable_1} = {variable_2 % variable_1 if variable_1 != 0 else 'Ошибка деления на 0'}")

user_name = input("Введите имя: ")
print(f"Привет, {user_name}!")

two_simbol = input("Введите слово: ")[::-1]
print(f"Последние два символа в обратном порядке: {two_simbol[:2]}")

rad = float(input("Введите радиус окружности: "))
print(f"Площадь окружности: {math.pi * rad**2}")
