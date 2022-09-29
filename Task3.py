# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
def function (N):
    sum = 0
    for i in range(0, N, +1):
        sum = sum + (1+(1/N))**N
    print(sum)
function(4)