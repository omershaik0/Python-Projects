# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇



#splitter = list(position)

#remover = [int(x) for x in splitter]


#for i in range(len(remover)):
    #remover[i] = remover[i] - 1


#map[remover[1]] [remover[0]] = 'x'


vertical = int(position[0])
horizontal = int(position[1])

map[horizontal - 1] [vertical - 1] = 'x'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
