# Testing Grounds

class Task:
    def __init__(self, name, description, completed = False):
        self.name = name
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        task = Task(name, description)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")

        else:
            print("Tasks:")
            
            for idx, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{idx}. {task.name} - {task.description} ({status})")

    def mark_completed(self):
        self.view_tasks()
        try:
            task_idx = int(input("Enter the task number to mark as completed: ")) - 1
            
            if 0 <= task_idx < len(self.tasks):
                self.tasks[task_idx].completed = True
                print("Task marked as completed!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def main_menu():
    task_manager = TaskManager()

    while True:
        print("\nMain Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task_manager.add_task()

        elif choice == "2":
            task_manager.view_tasks()
            
        elif choice == "3":
            task_manager.mark_completed()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
