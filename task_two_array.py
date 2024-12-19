lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def task_two_array(reverse_lists):

 reverse_lists.sort(reverse=True)

 return reverse_lists

print(task_two_array(lists))



def smalli(smaller):
 smallest = lists[0]
 for i in range(len(lists)):

   if lists[i] < smallest:

     smallest = lists[i]

 return smallest

print(smalli(lists))




