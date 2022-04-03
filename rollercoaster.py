print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  
  if age < 12:
    bill = 5
    # print("Please pay 5$")
    
  elif age <= 18:
    bill = 7
    # print("Please pay 7$")
    
  else:
    bill = 15
    # print("Please pay 15$")
if age >= 45 or age <= 55:
  print("Have free ride!!!")
  bill = 0

  pics = str(input("Do you want to take PHOTOS? press y for YESS and n NOO "))
  if pics == str("y"):
    bill += 3
    print(f"Total bill to pay {bill}$ ")

  else:
    print(f"Total bill to Pay {bill}$")
    


else:
  print("You can't ride the rollercoaster")