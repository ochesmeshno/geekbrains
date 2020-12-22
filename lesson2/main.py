print('####################################################')
print('################## Первое задание ##################')
new_list = ['one', 'two', 3, 'fire', 0, 1, -2.5]
list_len = len(new_list)
i = 0
while i < list_len:
    print(type(new_list[i]))
    i = i + 1
print('############## Конец первого задания ###############')
print('####################################################')

print('####################################################')
print('################## Второе задание ##################')

count = int(input('Введите количество элементов (от 4 до 10): '))
i = 0
ii = 0
list_of_values = []
if count >= 4:
    while i < count:
        new_value = input('Введите значение ' + str(i+1) + ': ')
        list_of_values.append(new_value)
        i = i + 1
else:
    print('Ошибка')

if count % 2 == 1:
    while ii < count-1:
        list_of_values[ii], list_of_values[ii+1] = list_of_values[ii+1], list_of_values[ii]
        ii = ii + 2
    ###
else:
    while ii != count:
        list_of_values[ii], list_of_values[ii+1] = list_of_values[ii+1], list_of_values[ii]
        ii = ii + 2
print(list_of_values)
print('############## Конец второго задания ###############')
print('####################################################')

print('####################################################')
print('################## Третье задание ##################')
mm = int(input('Введите номер месяца (от 1 до 12): '))
winter = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
          'Сентябрь', 'Октбярь', 'Ноябрь', 'Декабрь']
mm = mm - 1
if mm == 11:
    print(str(winter[mm]) + ' - это зима (через список)')
elif mm >= 0 and mm <= 1:
    print(str(winter[mm]) + ' - это зима (через список)')
elif mm >= 2 and mm <= 4:
    print(str(winter[mm]) + ' - это весна (через список)')
elif mm >= 5 and mm <= 7:
    print(str(winter[mm]) + ' - это лето (через список)')
elif mm >= 8 and mm <= 10:
    print(str(winter[mm]) + ' - это осень (через список)')

dict_of_m = {0: 'зима', 1: 'зима', 2: 'весна', 3: 'весна', 4: 'весна', 5: 'лето', 6: 'лето', 7: 'лето',
             8: 'осень', 9: 'осень', 10: 'осень', 11: 'зима'}
result = str(winter[mm]) + ' - это ' + str(dict_of_m[mm]) + ' (через словарь)'
print(result)
print('Результат из словаря: ')
print('############## Конец третьего задания ###############')
print('#####################################################')

print('####################################################')
print('################# Четвертое задание ################')

words = str(input('Введите некоторые слова: '))
words_list = words.split()
for i in range(len(words_list)):
    print(str(i) + '. ' + words_list[i][0:10])

print('############# Конец четвертого задания #############')
print('####################################################')

print('####################################################')
print('################### Пятое задание ##################')
print('####################################################')
print('Для остановки программы введите: stop')

some_num = 0
i = 0
nums_list = []
check = True
while check:
    i = i + 1
    if i % 5 == 0:
        print('Для остановки программы введите stop')
    some_num = input('Введите любое целое число: ')
    if some_num == 'stop':
        check = False
    if check == True:
        nums_list.append(int(some_num))
        nums_list = sorted(nums_list, reverse=True)
    print(nums_list)
print('############## Конец пятого задания ###############')
print('###################################################')