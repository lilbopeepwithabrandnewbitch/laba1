import random
count = 0
def calculate_row_sum(row):
    row_sum = 0
    for element in row:
        row_sum += element
    return row_sum

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: ")) # (задание 3)

# Инициализация двумерного массива случайными числами от 1 до 100 (задание 2,4)
array = []
for i in range(rows):
    row = []
    for i in range(cols):
        b = random.randint(0,1)
        if b:
            row.append(random.randint(1, 100))
        else:
            row.append(0)
    array.append(row)

# Вывод исходного двумерного массива
print("Исходный двумерный массив:")
for row in array:
    print(row)

for row in array:
    for element in row:
        if element > 0:
            count += 1

    print("Количество ненулевых элементов в строке", row, ":", count)
    count = 0
# Вычисление суммы значений в каждой строке и вывод результатов (задание 4)
row_sums = []
for i in range(len(array)):
    row_sum = calculate_row_sum(array[i])
    row_sums.append(row_sum)
    print("Сумма значений в строке", i + 1, ":", row_sum)

# Вычисление и вывод разности между максимальным и минимальным элементом массива (задание 1)
max_element = array[0][0]
min_element = array[0][0]
for row in array:
    for element in row:
        if element > max_element:
            max_element = element
        if element < min_element:
            min_element = element

difference = max_element - min_element

print(f"Разница между максимальным - {max_element} и минимальным - {min_element} элементами массива:", difference)
