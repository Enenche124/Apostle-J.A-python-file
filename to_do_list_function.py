
def display_menu():
    return "1. Add a task \n 2. View tasks \n 3. Mark task as complete \n 4. Delete a task \n 5. Exit"
    
def add_tasks(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("\n Task added! \n")

def view_tasks(tasks, completeds):
    for i in range(len(tasks)):
        if i + 1 in completeds:
            print(f"\n {i + 1}. [x] {tasks[i]} \n")
        else:
            print(f"\n {i + 1}. [] {tasks[i]} \n")

def mark_task_complete(completeds):
    while(True):
       try:
          completed = int(input("Which task do you want to mark as completed task?: "))
          completeds.append(completed)
          break
       except ValueError:
            print("Invalid, kindly enter number")



def delete_task(tasks, deletes):
    delete = int(input("Which task do you want to delete?: "))
    del tasks[delete - 1]



def main():
    tasks = []
    completeds = []
    deletes = []
    print("\n To-Do list Manager \n")
    while True:
        menu = display_menu()
        print(menu)
        while(True):
          try:
            choice = int(input("Enter your choice: "))
            break
          except ValueError:
             print(" ")
          
        if choice <= 0 or choice > 5:
          print("\n Invalid input, kindly enter the right input")
          continue
        
        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks, completeds)
        elif choice == 3:
            mark_task_complete(completeds)
        elif choice == 4:
            delete_task(tasks, deletes)
        elif choice == 5:
            print("Exiting the app. Goodbye!")
            break

if __name__ == "__main__":
    main()


