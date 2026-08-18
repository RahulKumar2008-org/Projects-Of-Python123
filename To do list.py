Task_book={
           



}

running=True
while running:
    print("1.Add new_task")
    print("2.View task")
    print("3.Remove the complete_task")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
   
    if choice==1:
        New_Task1=input("Enter new task")
        New_Task2=input("Enter new task")
        New_Task3=input("Enter new task")
        New_Task4=input("Enter new task")
        Task_book['Task1']="task1=",New_Task1
        Task_book['Task2']="task2=",New_Task2
        Task_book['Task3']="task3=",New_Task3
        Task_book['Task4']="task4=",New_Task4
      
    elif choice==2:
        print(Task_book)



    elif choice==3:
        key=(input('Enter key name:'))
        if key in Task_book:
            Task_book.pop(key)
            print("Task removed sucessfully")
        else:
            print("Invalid_Key")      

    elif choice==4:
        break

