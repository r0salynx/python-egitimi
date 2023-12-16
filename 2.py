colors = ['red', 'blue', 'pink', 'black', None]
alphabet = ['A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z']
nums = [1, 2, 3, 4, 5]
compiled = ["C", "C++", "C#", "Java"]
interpreted = ["Python", "Perl", "Ruby"]
complex = ['red', 245, 56.89, ["C", "Python", "Ruby"], "black"]


colors.append("white")
#print(colors)

colors.remove("pink")
#print(colors)

colors.insert(2, "green")
#print(colors)

fav = colors.pop(0)
print(fav)
print(colors)