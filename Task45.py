# Найти сумму чисел списка стоящих на нечетной позиции
temp_list = list(map(int, input('Введите желаемые значения через пробел: ').split()))
res = sum(list(filter(lambda x: not x % 2,temp_list)))
print(res)