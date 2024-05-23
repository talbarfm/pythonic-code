def reverse_positive_number(num):
    reverse_number = 0
    while num != 0:
        digit = num % 10
        reverse_number = reverse_number * 10 + digit
        num //= 10
    return reverse_number


print(reverse_positive_number(123))
