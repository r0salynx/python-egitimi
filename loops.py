#while ve loop döngüleri:
#"while" loop, "break" statement, "continue" statement
#"for" loop, "break" statement, "continue" statement, nested loop (birden fazla - sıralı döngü)


colors = ["red", "blue", "pink", "black"]
fav = []
unfav = []

for color in colors:
   if color == "black":
       fav.append(color)
   else:
       unfav.append(color)

print("fav_colors", fav)
print("unfav_colors", unfav)



numbers = [1, 3, 5, 7, 9]
colors = ["red", "blue", "pink", "black"]

for number in numbers:
   for color in colors:
       print(number, color)


#  stop / start, stop / start, stop, step   #
for i in range(2, 7, 2):
   print(i)
