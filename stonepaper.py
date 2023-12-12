import random
def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1

        return 1

comp=random.randint(0,2)
user=int(input("0 for stone , 1 for paper , 2 for scissor"))   

score=check(comp,user)
print("you :",user)
print("Computer :",comp)
if(score==0):
    print("its a draw")
elif (score==-1):
    print("You Loose")
else:
    print("you won")