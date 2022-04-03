rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if select == 0:
    print(rock)
elif select == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: \n")

pic = random.randint(0, 2)
   
if pic == 0:
    print(rock)
elif pic == 1:
    print(paper)
else:
    print(scissors)

if select >= 3 or select < 0:
  print("You Typed a incorrect number, Please Try Again!")
elif select == 0 and pic == 1:
    print("You Lose")
elif select == 0 and pic == 2:
    print("You WIN!")
elif select == 0 and pic == 0:
    print("DRAW")
elif select == 1 and pic == 2:
    print("You Lose")
elif select == 1 and pic == 0:
    print("You WIN!")
elif select == 1 and pic == 1:
    print("DRAW")
elif select == 2 and pic == 0:
    print("You Lose")
elif select == 2 and pic == 1:
    print("You WIN!")
else:
    print("DRAW")



    

    


