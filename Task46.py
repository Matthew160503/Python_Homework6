# #  Найти произведение пар чисел списка(парой считаем первый и последний, 
# #  второй предпоследний и тд)

temp_list = list(map(int, input('Введите желаемые значения через пробел: ').split()))
print(temp_list)
reverse_temp_list = sorted(temp_list, reverse = True)
def func(x):
    if len(x) % 2 == 0:
        return int(len(x)/2)
    else:
        return int(len(x)/2 + 1)
result =[temp_list[i] * reverse_temp_list[i] for i in range(func(temp_list))]
print(result)