def task():
    tasks = [] #emptylist
    print("--------WELCOME TO THE TASK MANAGEMENT APP------")
    total_tasks = int(input("Enter how many tasks you want to add = "))

    for i in range(1 , total_tasks+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's task are \n {tasks}")

    while True:
        operation = int(input("Enter \n 1-Add \n 2-Update\n 3-Delete \n 4-View \n 5-Exit/Stop \n"))

        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added sucessfully...")
        
        elif operation == 2:
            updated_task = input("Enter the task name that you want to update = ")
            if updated_task in tasks:
                up = input("Enter the new task \n")
                index = tasks.index(updated_task)
                tasks[index] = up
                print(f"Updated task {up}")

        elif operation == 3:
            del_task = input("Which task you want to delete = ")
            if del_task in tasks:
                index = tasks.index(del_task)
                del tasks[index]
                print(f"task {del_task} has been deleted successfully.... ")
        
        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input")

task()