# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к элементам каждой строки такой новый
# элемент, чтобы сумма положительных элементов стала бы равна модулю
# суммы отрицательных элементов. Результат оформить в виде матрицы из N
# строк и M + 1 столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

M_n = np.sum(A, axis=1) * (-1)
A = np.hstack((A, M_n.reshape(-1, 1)))
print(A)
