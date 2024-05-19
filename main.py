class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f'Task "{self.tasks[task_index]["task"]}" completed.')
        else:
            print('Invalid task index.')

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task["task"]}" removed.')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{index + 1}. {task['task']} - {status}")
        else:
            print("No tasks in the list.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
