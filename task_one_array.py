lists = [23, 44, 66, 40, 777, 89, 12, 10]

def task_one_array(largest_element):

 largest = lists[0]

 for j in range(len(lists)):

    if largest_element[j] > largest:

     largest = largest_element[j]

 return largest

print(task_one_array(lists))