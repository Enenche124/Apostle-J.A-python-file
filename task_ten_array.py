lists_one = ["a", "b", "c"]
lists_two = [1, 2, 3]
def task_ten_array(lists_one, lists_two):

   result = []

   while lists_one or lists_two:

     if lists_one:

       result.append(lists_one.pop(0))

     if lists_two:

       result.append(lists_two.pop(0))

   return result



print(task_ten_array(lists_one, lists_two))