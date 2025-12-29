#Python program for Simple To-Do List
#Simple To-Do List Program

tasks = []  # List to store tasks

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        tasks.append(task)  # Add task to list
        print(f"Task '{task}' added.")
    elif choice == '2':
        if tasks:
            print("Current Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)  # Remove task by index
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to delete.")
    elif choice == '3':
        if tasks:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
             print(f"{i}. {task}")
        else:
            print("No tasks to show.")
    elif choice == '4':
        print("Exiting To-Do List program.")
        break
    else:
        print("Invalid choice, please try again.")