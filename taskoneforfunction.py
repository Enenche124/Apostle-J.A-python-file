def taskone_function(number):

  for even in range(2, 200):

   if number % even == 0:

     return True

   else:

       return False


print(taskone_function(4))
print(taskone_function(5))