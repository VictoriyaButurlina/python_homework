# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

text1 = open('./homework004/file1.txt', 'w', encoding="utf-8")  # Создание первого файла с многочленом
text1.write('88x³+80x²+75x+10 = 0')
text1.close()

text2 = open('./homework004/file2.txt', 'w', encoding="utf-8")  # Создание второго файла с многочленом
text2.write('91x³+69x²+2x+74 = 0')
text2.close()

text_1 = open('./homework004/file1.txt', 'r', encoding="utf-8") # Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
line1 = text_1.read().split('+')
line1 = [i.lstrip() for i in line1]
text1.close()

text_2 = open('./homework004/file2.txt', 'r', encoding="utf-8") # Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
line2 = text_2.read().split('+')
line2 = [i.lstrip() for i in line2]
text2.close()

line1 = [int(i[0]) for i in line1]
line2 = [int(i[0]) for i in line2]

line3 = []
for i in range(3):                        # Суммирование коэффициентов многочлена
    line3.append(line1[i] + line2[i]) 

list = str(line3[0]) + 'x²' + '+' + str(line3[1]) + '+' + str(line3[2])  + '=0' # Создание окончательного текста многочлена


text3 = open('./homework004/file3.txt', 'w', encoding="utf-8")  # Запись полученного текста в файл
text3.write(list)
text3.close()