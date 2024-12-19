lists = [22, 3, 43, 14, 66, 61, 26, 8, 9, 12]

def task_five_array(evens):

   return evens % 2 == 0
  
even_elements = list(filter(task_five_array, lists))

print( even_elements)