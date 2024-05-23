def my_special_sum_v1(*args):
    my_sum = 5
    for arg in args:
        my_sum = my_sum + 10 * arg - 3
    return my_sum

