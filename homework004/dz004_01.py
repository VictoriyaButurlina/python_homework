# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math 
number=str(input())
print(round(math.pi, (abs(number.find('.') - len(number)) - 1)))

