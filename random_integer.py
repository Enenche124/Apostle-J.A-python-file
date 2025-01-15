import random 
random_number = random.randint(2, 100)
random_number2 = random.randint(2, 100)
print(random_number, random_number2)
user_input = int(input("Enter the sum of the integers: "))
sum = random_number + random_number2


def compareling(user_input):
 if(user_input == sum):
    return "True"
 elif(user_input != sum): 
    return "False"
print(compareling(user_input));    

