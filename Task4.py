# Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
def function (N, position1, position2):
    ran = range(-N, N+1)
    numbers = list(ran)
    print(numbers)
    increase = numbers[position1] * numbers[position2]
    print(increase)
function(5, 2, 7)