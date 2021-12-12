import numpy as np


def Hello():
    print("\n\nШестой номер. \nПовторим номер 5:\n")


def num_5():
    array = np.random.random((3, 3))
    print(f'Исходная матрица: \n{array} \n'
          f'Транспонированная матрица: \n{array.T}')

if __name__ == "__main__":
    print('Это сообщение появится только в случае запуска конкретно этого файла.')