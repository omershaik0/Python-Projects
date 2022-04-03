# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI formula so that we can calculate easily "weight in kilograms divided by height in meters squared."

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

var1 = float(height) ** 2
var2 = int(weight)

print(int(var2 / var1))
