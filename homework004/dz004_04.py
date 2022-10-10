# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Задайте натуральную степень k: '))
def g(x, n):
    if n == 0:
        return str(x)
    if n == 1:
        return str(x)+"x"
    stepen = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
    for i in str(n):
        result += stepen[int(i)]
        return result
def poly(k):
    result = []
    for i in range(k, -1, -1):
        koef = random.randint(0, 100)
        if koef != 0:
            result.append(g(koef, i))
    return "+".join(result)
with open('./homework004/file.txt', 'w', encoding="utf-8") as file:
        file.write(poly(k))