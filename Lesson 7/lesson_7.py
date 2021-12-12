from os import name, getlogin, listdir
import numpy as np
from test_funk import num_5, Hello

'''Номер 4'''
print('Четвертый номер\n'
     f'Наименование ОС: {name}, \n'
     f'Имя пользователя: {getlogin()}, \n'
     f'Список файлов и дирректорий: {"".join(map(str, listdir(path=".")))}\n')

'''Номер 5'''
array = np.random.random((3, 3))
print('Пятый номер\n'
      f'Исходная матрица: \n{array} \n'
      f'Транспонированная матрица: \n{array.T}')

'''Номер 6'''
Hello()
num_5()