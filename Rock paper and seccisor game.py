import random 
move=["rock","paper","seccisor"]
running= True
while True:
 user_move=input("Enter Move from rock paper seccisor:")

 computer_move=random.choice(move)

 if user_move==computer_move:
     print("You Win The Game")
 elif user_move != computer_move:
     print("You lose the game")    

     # when we made any rand words selcting programme in python its format is:---
     # import random
     # store_words=[]
     # while loop
     # For numbers select by computer=random.randint(numbers=1,4,8)
     # for words selected by computr =random.choice(words store variable)
     # user_input
     # computer_move=random.choice(store_word variable name)
     # conditional statemnts 