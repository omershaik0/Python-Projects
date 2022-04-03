# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

converter1 = name1.lower()
converter2 = name2.lower()

counter1 = converter1.count("t") + converter1.count("r") + converter1.count("u") + converter1.count ("e") + converter2.count("t") + converter2.count("r") + converter2.count("u") + converter2.count("e")

counter2 = converter1.count("l") + converter1.count("o") + converter1.count("v") + converter1.count("e") + converter2.count("l") + converter2.count("o") + converter2.count("v") + converter2.count("e")

counter_result = int(str(counter1) + str(counter2))

if counter_result < 10 or counter_result > 90:
    print (f"Your score is {counter_result}, you go together like coke and mentos.")

elif counter_result >= 40 and counter_result <= 50:
    print(f"Your score is {counter_result}, you are alright together.")

else:
    print(f"Your score is {counter_result}.")



