# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import numpy as np

n = int(input())
lst = np.random.randint(0, 10, n)
print(lst)
new_lst= list(set(lst)) 
print(new_lst) 