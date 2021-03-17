import random
print("Rules of Game:")
print("rock vs papers:PAPERS WINS")
print("papers vs scissors:SCISSORS WINS")
print("rock vs scissors:ROCK WINS")

def win_lose(a,b):
    if (a=="Rock" and b=="papers") or (a=="papers" and b=="Rock"):
        print("papers wins!!!!")
    elif (a=="papers" and b=="scissors") or (a=="scissors" and b=="papers"):
        print("scissors wins!!!!")
    elif (a=="Rock" and b=="scissors") or (a=="scissors" and b=="Rock"):
        print("Rock wins!!!!")
    elif (a==b):
        print("Match tie")


choice="y"
while (choice=="y"):
    choice=input(str("Want to play(y for yes ,n for no)"))
    if choice=="y":
        l1=["Rock","papers","scissors"]
        print("Rock")
        print("Papers")
        print("scissors")
        choice2=input(str("Enter your choice:"))
        x=random.randint(0,2)
        print("Your action:",choice2)
        print("computer action:",l1[x])
        win_lose(choice2,l1[x])
    else:
        break




