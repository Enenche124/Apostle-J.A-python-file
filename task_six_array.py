lists = [22, 3, 43, 14, 66, 61, 26, 8, 9, 12]

def task_six_array(running_total):

 running_total = []

 total = 0

 for running in lists:

  total = total + running
 
  running_total.append(total)
   
 return running_total

print(task_six_array(lists))
 