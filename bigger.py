# -*- coding: utf-8 -*-

from alphavit import symvols, strings

t = open('result.txt', 'w')  # открываем (создаём) файл для вывода

text = input('Enter the text (you can use only a-z (A-Z), а-я (А-Я), 0-9 and any symbols on your keyboard):\n')
text = text.lower()  # одинаковый регистр

for i in range(strings):     # идём по строкам
    for char in text:           # идём по символам в введённом тексте
        if char in symvols:           # проверка на наличие символа в словаре
            for element in symvols[char][i]:      # идём по словарю
                if element != '':
                    t.write(char.upper())                 # делаем символ большим и выводим его в файл
                else:
                    t.write(' ')                          # пробел между СИМВОЛАМИ
            t.write(' ')
    t.write('\n')               # переходим на новую строку в strings

print('\nLook the result in text.txt :)')
