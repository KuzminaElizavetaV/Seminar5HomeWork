'''задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа,
описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
*Пример:*
[1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
[1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]'''

from random import randint
#numsequence = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1]
#numsequence = [1, 5, 2, 3, 4, 6, 1, 7]
numsequence = [randint(1, 15) for i in range(10)]
def len_seq(el, numsequence):
    len_list = 1
    for _ in range(len(numsequence)):
        if el+1 in numsequence:
             len_list += 1
             el += 1
    return len_list

max_seq = 1
for el in numsequence:
    if len_seq(el, numsequence) > max_seq:
        max_seq = len_seq(el, numsequence)
        min_el = el
seq_boundary = []
seq_boundary.append(min_el)
seq_boundary.append(min_el + max_seq - 1)
print("Дана рандомная последовательность чисел:", numsequence)
#print(f"Длина максимальной возрастающей последовательности: {max_seq}")
print(f"Границы максимальной возрастающей последовательности: {seq_boundary}")