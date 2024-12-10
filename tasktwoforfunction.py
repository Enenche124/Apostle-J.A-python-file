def tasktwo_function(number):


  for prime in range(2, int(number ** 0.5) + 1):

   if number % prime == 0:

      return "False"
  else:

    return "True"



print(tasktwo_function(6))
print(tasktwo_function(8))