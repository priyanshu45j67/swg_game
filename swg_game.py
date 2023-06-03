#snake water gun game
import random
def check(user,com):
    if(user==com):
        return 0
    elif(user==1 and com==0):
        return -1
    elif(user==2 and com==1):
        return -1
    elif(user==0 and com==2):
        return -1
    
    return 1


print("start game\n")
term=int(input("Enter the no. of turn in game\n"))
count=0
for i in range(term):
 com=random.randint(0,2)
 user=int (input("press 0 for snake\n press 1 for water\n press 2 for gun\n "))
 score=check(user,com)
 print("user choice: ",user)
 print("computer choice: ",com)
 if(score==0):
    print("draw!!")
 elif(score==1):
    print("***you win***")
    count=count+1
 elif(score==-1):
    print("you loose!!")
print(f"you win {count} times")  
