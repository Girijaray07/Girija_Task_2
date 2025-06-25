class ToDo:
    def __init__(self) -> None:
        self.listTask = list()
        self.listStatus = list()
        
        self.taskSpace = 0
        self.statusSpace = 0
    def addTask(self):
        try:
            task = input("Enter Task to do: ")
            status = input("what's the Status: ")
            self.listTask.append(task)
            self.listStatus.append(status)

            self.taskSpace = max(self.taskSpace, len(task))
            self.statusSpace = max(self.statusSpace, len(status))
        except Exception as e:
            print(f"Error {e}")
    def removeTask(self):
        print(f"{int(self.taskSpace/2)*" "}Task    {int(self.taskSpace/2)*" "}|{int(self.statusSpace/2)*" "}Status")
        for i in range(len(self.listTask)):
            print(f"{i+1}. {self.listTask[i]} {(self.taskSpace - len(self.listTask[i])+3)*" "}|  {self.listStatus[i]}")
        
        try:
            select = int(int(input("Select the Number: ")))
            print(f"Removed Task: {self.listTask.pop(select-1)}")
            self.listStatus.pop(select-1)
        except Exception as e:
            print(f"Error: {e}")

    def updateTask(self):
        print(f"{int(self.taskSpace/2)*" "}Task   {int(self.taskSpace/2)*" "}|{int(self.statusSpace/2)*" "}Status")
        for i in range(len(self.listTask)):
            print(f"{i+1}. {self.listTask[i]} {(self.taskSpace - len(self.listTask[i])+3)*" "}|  {self.listStatus[i]}")
        
        try:
            select = int(int(input("Select the Number: ")))
            task = input("Enter Task to do: ")
            status = input("what's the Status: ")
            self.listTask.pop(select-1)
            self.listStatus.pop(select-1)
            self.listTask.insert(select-1, task)
            self.listStatus.insert(select-1, status)
        except Exception as e:
            print(f"Error: {e}")
        
        print("Task Updated.")
        
    def viewTasks(self):
        print(f"{int(self.taskSpace/2)*" "}Task   {int(self.taskSpace/2)*" "}|{int(self.statusSpace/2)*" "}Status")
        for i in range(len(self.listTask)):
            print(f"{i+1}. {self.listTask[i]} {(self.taskSpace - len(self.listTask[i])+3)*" "}|  {self.listStatus[i]}")
        

if __name__ == "__main__":
    print("          ***** Welcome to Python To-Do-List App *****          ")
    obj = ToDo()

    while True:
        print("\nSelect from Below Option: ")
        print("1. Add a Task.")
        print("2. Remove a Task.")
        print("3. Update a Task.")
        print("4. View all Tasks.")
        print("5. Exit.\n")
        
        try:
            choice = int(input("Enter your Choice: "))

            switchCase = {
                1: obj.addTask,
                2: obj.removeTask,
                3: obj.updateTask,
                4: obj.viewTasks,
                5: exit
            }

            switchCase.get(choice, lambda: print("Invalid Input..."))()
        except Exception as e:
            print(f"Error: {e}")