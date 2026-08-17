Record={
         "student1":"Name=Shyam,class=10,Bookname=Trust issue",
         "student2":"Name=Raman,class=8,Bookname=Tit for tat",
         "student3":"Name=Shyam,class=11,Bookname=You can",
         "student4":"Name=Pratik,class=6,Bookname=Far away world",
}  

Available_Books=["Trust issue","You Can","Far away world","Tit for tat"]
Book_id={
          "Trust issue":"T123",
          "You can":"Y456",
          "Far away world":"F233",
          "Tit for tat":"T666"
}

print("________Library Managment_______")
running=True
while True:
    print("1.Show_Record")
    print("2.Available_Books")
    print("3.Book_id")
    print("4.New_Borrower")
    print("5.Book_return")
    print("6.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        print(Record)
    elif choice==2:
        print(Available_Books)
    elif choice==3:
        print(Book_id)
    elif choice==4:
        name=input ("Enter student name:")
        Class=int(input("Enter student class:"))
        Bookname=input("Enter name of the book:")
        Record["Student5"]="Name=",name  
        Record["Student5"]="Class=",Class
        Record["Student5"]="Bookname=",Bookname  
        print(Record)
    elif choice==5:
        key = input("Enter key to remove: ")

        if key in Record:
         Record.pop(key)
        print("Item removed successfully")


    elif choice==6:
        break    
    



        
                 
        





