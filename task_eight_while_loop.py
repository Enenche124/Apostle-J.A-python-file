numbers = [4, 2, 31, 4, 5, 62, 11, 8, 9, 10]

def task_eight_while_loop(sum_of_numbers):

    sum = 0
    k = 0

    while k < len(numbers):

     sum = sum + numbers[k]

     k = k + 1

    return sum

print(task_eight_while_loop(numbers))