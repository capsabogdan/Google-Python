
# 1. Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale.
# your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# your_function() va returna 0.
# your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def sum(*args, **kwargs):
    sum = 0
    for number in args:
        if(isinstance(number, int) or isinstance(number, float)):
            sum += number

    return sum

mySum = sum(1, 5, -3, 'abc', [12, 56, 'cad'])
# mySum = sum()
# mySum = sum(2, 4, 'abc', param_1=2)
print(mySum)


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# suma tuturor numerelor de la [0, n]
# suma numerelor pare de la [0, n]
# suma numerelor impare de la [0. n]


def recursiveSum(number):
    sum_all = 0
    sum_even = 0
    sum_odd = 0

    for number in [0,number]:
        sum_all += number
        if(number % 2) == 0:
            sum_even += number
    sum_even = sum_all - sum_even

    sums = [sum_all, sum_even, sum_odd]

    return sums


sums_3 = recursiveSum(2)
print(sums_3)