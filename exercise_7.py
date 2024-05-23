list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
target_sum = 9

result = []
for num1 in list1:
    for num2 in list2:
        if num1 + num2 == target_sum:
            result.append((num1, num2))

print(result)
