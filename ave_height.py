# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum = 0
total = 0
for x in student_heights:
    sum += x

for v in student_heights:
    total += 1

final = round(sum / total)
print(final)
