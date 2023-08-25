# Вводим длинну списка

len_list = int(input('Введите количество элементов: \n'))

# Заполняем список элементами

list_num = []
for i in range(len_list):
    list_num.append(int(input(f'Введите {i+1} элемент \n')))
    i += 1

# Сортируем список по возрастанию

list_num.sort()

# Выводим список в консоль

print(f'Вывод: {list_num}\n')
