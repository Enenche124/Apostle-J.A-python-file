numbers = [44, 2, 30, 4, 5, 62, 71, 8, 9, 10]

def task_eight_for_loop(sum_of_numbers):

  for i in range(len(numbers)):

   if sum_of_numbers in numbers:

    return True

   else:


    return False

print(task_eight_for_loop(44))

print(task_eight_for_loop(45))



