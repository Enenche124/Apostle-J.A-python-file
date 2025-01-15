user_input = 0
while user_input < 1000:
 user_input = int(input("Enter an integer number between 0 to 1000: "))
 num1 = user_input % 10
 numb1 = user_input // 10
 numb4 = numb1 % 10
 
 num2 = num1 % 10
 numb2 = numb1 // 10
 
 num3 = num2 % 10
 numb3 = numb2 // 10
 
 result = numb2 + num3 + numb4
 print(result)
 break

 