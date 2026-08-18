import random
running=True
while running:
 user_guess=int(input("Enter your number:"))

 computer_guess=random.randint(1,10)
 print(computer_guess)


 if user_guess == computer_guess:
          print("You guess right")
 elif user_guess != computer_guess:
        print("GUess is not right")
       
    
        
        