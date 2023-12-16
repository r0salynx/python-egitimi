text = 'python bir proglamlama dilidir ve adını "piton" yılanından almaz'
text2 = "python bir programlama dilidir ve adını 'piton' yılanından almaz"

print(type(text), type(text2))


name = 'Fatmanur'
last_name = 'Dursun'
user = f'(name) (last_name)'
print(user)

is_active = True
print(is_active, type(is_active))

a = 5
b = "5"

print(type(a), type(b))

c = int(b)
print(type(b), type(c))

num1 = 5.09
print(int(num1))

is_active = True
is_superuser = 'True'
print(is_active, type(is_superuser))

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




user = {
    "name": "Fatmanur",
    "last_name": "Dursun"
}

