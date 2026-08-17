Out_of=600

Student_Marks={


}

Report_card={
     
}

running=True
while running:
    print("1.Enter 6 subject marks___:")
    print("2.Enter marks for total marks and percentage___:")
    print("3.Grade")
    print("4.Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        student_name=input("Enter student name___:")
        Hindi=int(input("Enter marks of hindi___:"))
        Gk=int(input("Enter marks of Gk___:"))
        Ssst=int(input("Enter marks of Sst___:"))
        Science=int(input("Enter marks of Science___:"))
        English=int(input("Enter marks of English___:"))
        Maths=int(input("Enter marks of Maths___:"))

        Student_Marks["student_name"]="Student_name=",student_name
        Student_Marks["Hindi"]="Hindi=",Hindi
        Student_Marks["Gk"]="Hindi=",Gk
        Student_Marks["Ssst"]="Hindi=",Ssst
        Student_Marks["Science"]="Hindi=",Science
        Student_Marks["English"]="Hindi=",English
        Student_Marks["Maths"]="Hindi=",Maths
        print(Student_Marks)


    elif choice==2:
       total_marks=Hindi+Gk+Ssst+Science+English+Maths

       percentage=(total_marks/Out_of) * 100

       print(f"percentage:{percentage}%")

       print(total_marks)

    elif choice==3:
        if total_marks>=500:
             print("Great")
        elif total_marks<=500:
             print("Excellent")
        elif total_marks>=400:
             print("Very_Good")
        elif total_marks<=400:
             print("Good")
        elif total_marks>=300:
             print("Keep it up")
        elif total_marks<=300:
             print("Average")

    elif choice==4:
         break     
        


    

                                               


    

                                               