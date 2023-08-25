# Получаем строку с значениями

str_num1 = input('Введите элементы 1 списка: \n')
str_num2 = input('Введите элементы 2 списка: \n')

# Превращаем строку в список строк

list_str_num1 = str_num1.split(',')
list_str_num2 = str_num2.split(',')

# Убираем элементы содержащиеся во 2 списке из 1

gen_list_str_num = []     # Список для формирования результата
k = 0

for i in list_str_num1:
    for j in list_str_num2:
        if i == j:
            k = 0
            break
        else:
            k = 1
    if k:
        gen_list_str_num.append(int(i))

# Выводим результат

print(f'Результат: {gen_list_str_num}')
