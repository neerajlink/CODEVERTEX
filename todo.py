import sys

# Task list
tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"id": len(tasks) + 1, "task": task, "status": "Incomplete"})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "[X]" if task["status"] == "Complete" else "[ ]"
        print(f"{task['id']}. {status} {task['task']}")

def mark_task_complete():
    task_id = int(input("Enter the task ID to mark as complete: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Complete"
            print("Task marked as complete.")
            return
    print("Task not found.")

def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print("Task deleted successfully.")

def exit_application():
    print("Exiting application.")
    sys.exit()

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            exit_application()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

