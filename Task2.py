# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def Function (N):
    result = 1
    print(result)
    for i in range(1, N, +1):
        result = result * (i + 1)
        print(result)
Function(4)