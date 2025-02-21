from dateutil import parser
from datetime import datetime
import re


date_form  = "%Y-%m-%d"

dates = []
descriptions = []
amounts = []

total = 0
choice = 0

print("Welcome to Semicolon Expense Tracker App")
print("=========================================")


while(True):
  print("\n \n 1. Add an expense \n 2. View all expense \n 3. Clculate total expense \n 4. Exit")
  try:
     choice = int(input("Enter your choice between 1 to 4: "))
  except ValueError:
     print(" ")  
  
  if(choice < 1 or choice > 4):
     print("Invalid input, Select between 1 to 4: ")
     continue    
  if(choice == 1):
   try:         
     date = input("Enter the date (YYYY-MM-DD): ")      
     dates.append(date)
     datetime.strptime(date, date_form)
   except ValueError:
     print("Invalid date, Kindly, Enter a valid date")
     continue    
   try: 
     description = input("Enter the description: ")
     if re.match("^[a-zA-Z]+$", description):   
       descriptions.append(description) 
   except ValueError:
      print("Invalid, kindly enter the description")
      continue
   
   try:
     amount = float(input("Enter the amount: "))
     amounts.append(amount)
   except ValueError:
     print("Invalid amount, Kindly enter the amount")
     
     continue
     
     
   print("\n Expense add successfully")
     
       
  elif(choice == 2):
      print("Expenses: ")
      for i in range(len(dates)):
         print(f" {i + 1}. Date: { dates[i]}, Description: {descriptions[i]}, Amount: {amounts[i]}")
         total += amounts[i]
       
  elif(choice == 3):  
    print(f"Total Expenses: {total}")
    
  elif(choice ==  4):
      print("Exiting the app. Goodbye🤗 \n \n")
      break



