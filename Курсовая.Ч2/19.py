# Создать квадратную матрицу A, имеющую N строк и N столбцов со
# случайными элементами. Определить сумму элементов, расположенных
# параллельно главной диагонали (ближайшие к главной). Элементы главной
# диагонали имеют индексы от [0,0] до [N,N].

import numpy as np
import random

N = random.randint(2, 5)
print("N =", str(N))
A = np.random.randint(-50, 50, (N, N))
print(str(A) + "\n")

s = A.diagonal(-1).sum() + A.diagonal(1).sum()
print("Сумма элементов, расположенных параллельно главной диагонали =", str(s))
