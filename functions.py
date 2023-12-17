#def name(arguments):
#  statement
#  statement
#  return value
#indentations are a must!

#def: definitions
#name: function name, identifier
#arguments: a list of values passed to the function (optional)
#the two statements are the function's body
#return value: ends function call and sends data back to the program

#create and call a function:
def hello():
   print("hello world!")

hello()

def hello(x, y, z = None):
    print(f'hello' (x) (y) (z))

name = "Fatmanur"
last_name = "Dursun"
hello(name, last_name)

def toplama(x, y):
    return x + y

def hello():
    return "hello"


sonuc = toplama(3, 5)
print(sonuc)

sonuc2 = toplama(3, 5) + toplama(2, 4)
print(sonuc2)

def toplama_cikarma(x, y):
    return x + y, x - y

sonuc3 = toplama_cikarma(5, 3)
print(sonuc3) # (8, 2)

toplama, cikarma = toplama_cikarma(5, 3)
print(toplama) #8
print(cikarma) #2

def outer(a, b):
    def inner(c, d):
        return c + d
    
    return inner(a, b)

result = outer(2, 4)
print(result) #6



def cift_sayilar(sayilar):
    cift_sayilar = []

    for sayi in sayilar:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)

    return cift_sayilar

def cift_tek_sayilar(sayilar):
    cift_sayilar = []
    tek_sayilar = []

    for sayi in sayilar:

        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
        else:
            tek_sayilar.append(sayi)

    return cift_sayilar, tek_sayilar

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sonuc = cift_tek_sayilar(nums)
print(sonuc)

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y