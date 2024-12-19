lists = [9, 23, 33, 14, 6, 61, 16, 8, 9, 10]

def task_four_array(odds):

   return odds % 2 != 0
  
odd_elements = list(filter(task_four_array, lists))

print( odd_elements)