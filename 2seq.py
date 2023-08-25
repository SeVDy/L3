# Получаем строку с значениями

str_num = input('Введите элементы списка через запятую: \n')

# Ищим разделитель и превращаем строку в список строк

if str_num.find('/') >= 0:
    list_str_num = str_num.split('/')
elif str_num.find(';') >= 0:
    list_str_num = str_num.split(';')
else:
    list_str_num = str_num.split(',')

# Конвертируем список строк в список интов

list_int_num = []

for i in list_str_num:
    list_int_num.append(int(i))

# Сортируем по возрастанию список интов

list_int_num.sort()

# Превращаем список интов в множество для удаления дубликатов и обратно в список

set_num = set(list_int_num)
list_int_num = list(set_num)

# Выводим список в консоль

print(list_int_num)
