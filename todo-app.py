tasks = []

while True:
    print("\n==== TO DO LIST ====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        task_number = int(input("Enter task number: "))
        if 0 < task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")