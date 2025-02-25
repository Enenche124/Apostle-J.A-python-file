from datetime import datetime


date_form = "%Y-%m-%d"
def display_menu():
    return "\n \n 1. Add an expense \n 2. View all expenses \n 3. Calculate total expense \n 4. Exit"

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice between 1 to 4: "))
            if choice < 1 or choice > 4:
                raise ValueError
            return choice
        except ValueError:
            print("\n Invalid input")



def get_date(dates):
    while(True):
       try:
          date = input("Enter the date (YYYY-MM-DD): ")
          dates.append(date)
          datetime.strptime(date, date_form)
          break
       except ValueError:
          print("Invalid date format, Kindly enter date (YYYY-MM-DD): ")
    
def get_description(descriptions):
   while(True):
     
         description = input("Enter the description: ")
         
         if description.strip():
            descriptions.append(description)
            return description
         else:
           print("Ivalid  description, Kindly enter description")
    
def get_amount(amounts):
    total = 0
    while(True):
       try:
         amount = int(input("Enter the amount: "))
                  
         if amount >= 1:
            amounts.append(amount)
            
            
            return amount
                           
       except ValueError:
           print("Enter a valid amount")
    
   
def view_expenses(dates, descriptions, amounts):
    total = 0
    expenses = "Expenses: \n"
    for i in range(len(dates)):
        
        expenses += f" {i + 1}. Date: {dates[i]}, Description: {descriptions[i]}, Amount: {amounts[i]}\n"
    
    return expenses

def calculate_total(total):
    return f"Total Expenses: {total}"

def main():
    dates = []
    descriptions = []
    amounts = []
    total = 0
    
    
    print("Welcome to Semicolon Expense Tracker App")
    print("=========================================")
    while True:
        print(display_menu())
        choice = get_user_choice()
        if choice == 1:
            get_date(dates)
            get_description(descriptions)
            get_amount(amounts)
        elif choice == 2:
            print(view_expenses(dates, descriptions, amounts))
            
            
        elif choice == 3:
            print(calculate_total(total))
        elif choice == 4:
            print("Exiting the app. Goodbye!")
            break

if __name__ == "__main__":
    main()
