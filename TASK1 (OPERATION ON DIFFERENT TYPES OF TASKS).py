class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo.add_task(input("Enter task: "))
        elif choice == '2':
            todo.complete_task(int(input("Enter task number to mark as complete: ")) - 1)
        elif choice == '3':
            todo.view_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
