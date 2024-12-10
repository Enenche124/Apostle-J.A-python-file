def taskfive_function(integer_number):

 counter = 0

 for counting in range(1, integer_number + 1):
  
  if integer_number % counting ==  0:

   counter += 1

 return counter

    

print(taskfive_function(10))

