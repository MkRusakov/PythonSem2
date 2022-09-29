# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).
import random
ran = range(1, 10)
numbers = list(ran)
print(numbers)
for i in range(len(numbers)-1, 0, -1):
    j = random.randint(0, i + 1)
    numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)