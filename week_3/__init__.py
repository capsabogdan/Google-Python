def get_sum(*args):
    my_sum = 0
    for number in args:
        my_sum += number
    return my_sum


my_sum = get_sum(1, 2, 3)

print(my_sum)
