import os

TASKS_FILE = "tasks.txt"
tasks = []


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\n=== Python CLI To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def clear_tasks():
    tasks.clear()
    save_tasks()
    print("All tasks cleared!")


def main():
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()