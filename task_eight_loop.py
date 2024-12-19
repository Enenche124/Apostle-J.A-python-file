numbers = [44, 2, 30, 4, 5, 62, 71, 8, 9, 10]

def task_eight_for_loop(sum_of_numbers):
    sum = 0
    for i in range(len(numbers)):
      sum = sum + sum_of_numbers[i]

    return sum

print(task_eight_for_loop(numbers))