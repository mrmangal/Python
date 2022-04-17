import random


cpuMove = random.randint(0, 2)
userMove = input("\nPlease enter (r) rock, (p) paper, (s) scissor, or (x) to exit: ")
if (cpuMove == 0) & (userMove == "r"):
    print("It's a tie!")
elif (cpuMove == 0) & (userMove == "p"):
    print("You Win!")
elif (cpuMove == 0) & (userMove == "s"):
    print("Sorry, you lose!")
elif (cpuMove == 1) & (userMove == "r"):
    print("Sorry, you lose!")
elif (cpuMove == 1) & (userMove == "p"):
    print("It's a tie!")
elif (cpuMove == 1) & (userMove == "s"):
    print("You win!")
elif (cpuMove == 2) & (userMove == "r"):
    print("You win!")
elif (cpuMove == 2) & (userMove == "p"):
    print("Sorry, you lose!")
elif (cpuMove == 2) & (userMove == "s"):
    print("It's a tie!")
elif (userMove == "x"):
    exit(0)





