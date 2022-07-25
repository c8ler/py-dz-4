# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def ListOfNaturalProduct(num):
    list = []
    for i in range(2, num):
        division_result = num % i
        new = int(num / i)
        if division_result == 0 and CheckOfNatural(new):
            list.append(new)
    list.reverse()
    return list


def CheckOfNatural(num):
    check = True
    for i in range(2, num):
        if num % i == 0:
            check = False
            break
    return check


n = input("Задайте натуральное число N -> ")
try:
    n = int(n)
    list_of_natural_product = ListOfNaturalProduct(n)
    if not CheckOfNatural(n):
        print(list_of_natural_product)
    else:
        print('Число не имеет натуральных делителей!')
except:
    print('Нужно ввести целое число!')
