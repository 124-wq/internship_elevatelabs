print("To Do List")
print("enter 1 to add a task")
print("enter 2 for viewing the list")
print("enter 3 to delete a task")
print("enter 4 to exit")

tasks=[]
while(True):
    choice = int(input("enter your choice: "))
    if choice ==1:

        task = str(input("enter a task:"))
        with open('to_do_list.txt', 'a') as file:
            file.write(str(task) + '\n')
            tasks.append(task)
    elif choice ==2:
        with open("to_do_list.txt",'r') as file:
            content = file.read()
            print(content)
    elif choice ==3:
        remove = int(input("enter the task to delete:"))
        tasks.pop(remove-1)

        with open("to_do_list.txt",'w') as file:
            for t in tasks:
                file.write(str(t) + '\n')
            
        print("task deleted")

    elif choice ==4:
        break

