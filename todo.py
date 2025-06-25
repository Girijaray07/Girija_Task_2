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
            select = int(int(input("Which task you want to remove: ")))
            print(f"Removed Task: {self.listTask.pop(select-1)}")
            self.listStatus.pop(select-1)
        except Exception as e:
            print(f"Error: {e}")
            
    def updateTask(self):
        print(f"{int(self.taskSpace/2)*" "}Task   {int(self.taskSpace/2)*" "}|{int(self.statusSpace/2)*" "}Status")
        for i in range(len(self.listTask)):
            print(f"{i+1}. {self.listTask[i]} {(self.taskSpace - len(self.listTask[i])+3)*" "}|  {self.listStatus[i]}")
        
        try:
            select = int(int(input("Which task you want to update: ")))
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
        if (self.listTask):
            print(f"{int(self.taskSpace/2)*" "}Task   {int(self.taskSpace/2)*" "}|{int(self.statusSpace/2)*" "}Status")
            for i in range(len(self.listTask)):
                print(f"{i+1}. {self.listTask[i]} {(self.taskSpace - len(self.listTask[i])+3)*" "}|  {self.listStatus[i]}")
        else:
            print("No Tasks have been added.")
             
    def loadTasksFromFile(self):
        try:
            with open("Files/Tasks.txt", "r") as file:
                for line in file:
                    task, status = line.strip().split(" | ")
                    self.listTask.append(task)
                    self.listStatus.append(status)
                    self.taskSpace = max(self.taskSpace, len(task))
                    self.statusSpace = max(self.statusSpace, len(status))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    def saveTasksToFile(self):
        try:
            with open("Files/Tasks.txt", "w") as file:
                for task, status in zip(self.listTask, self.listStatus):
                    file.write(f"{task} | {status}\n")
            print("All Tasks are Saved. Exiting Now")
            exit()
        except Exception as e:
            print(f"Error saving tasks: {e}")
    

if __name__ == "__main__":
    print("          ***** Welcome to Python To-Do-List App *****          ")
    obj = ToDo()
    obj.loadTasksFromFile()

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
                5: obj.saveTasksToFile
            }

            switchCase.get(choice, lambda: print("Invalid Input..."))()
        except Exception as e:
            print(f"Error: {e}")