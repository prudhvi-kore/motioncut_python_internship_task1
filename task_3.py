class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.description} (Due: {task.due_date}, Priority: {task.priority}, Status: {status})")

    def mark_task_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            self.completed_tasks.append(task)
            self.tasks.pop(task_index - 1)

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)

    def display_completed_tasks(self):
        print("\n--- Completed Tasks ---")
        for i, task in enumerate(self.completed_tasks, start=1):
            print(f"{i}. {task.description} (Due: {task.due_date}, Priority: {task.priority})")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Display Completed Tasks")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (High/Medium/Low, optional): ")
            task = Task(description, due_date, priority)
            to_do_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            to_do_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            to_do_list.mark_task_as_completed(task_index)

        elif choice == '4':
            task_index = int(input("Enter the task number to update: "))
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date (optional): ")
            new_priority = input("Enter new priority (High/Medium/Low, optional): ")
            to_do_list.update_task(task_index, new_description, new_due_date, new_priority)
            print("Task updated successfully!")

        elif choice == '5':
            task_index = int(input("Enter the task number to remove: "))
            to_do_list.remove_task(task_index)
            print("Task removed successfully!")

        elif choice == '6':
            to_do_list.display_completed_tasks()

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
