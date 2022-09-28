# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def SumOfNum (num):
    nums = str(num)
    result = 0
    for i in range(0, len(nums), +1):
        if nums[i].isdigit():
            result += int(nums[i])
    print(result)
SumOfNum(125.2)