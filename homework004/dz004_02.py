# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input())
def simple_factor(n):
    i = 2
    new_lst = []
    while i*i <=n:
        while n %i ==0:
            new_lst.append(i)
            n = n/i
        i +=1
    if n>1:
        new_lst.append(n)
    return new_lst
print(simple_factor(n))
