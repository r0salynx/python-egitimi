import random

name = input("oyuncu adı:")
print("başarılar!", name)

kelimeler = ["elma", "muz", "kedi", "kuş", "bilgisayar", "modül", "python", "java", "mouse"], 
kelime = random.choice(kelimeler)
kalan_hak = 10

tahmin = input("bir harf tahmin et: ")
print(tahmin)
while kalan_hak > 0:
    if tahmin in kelime:
        print("doğru!")
    else:
       print("yanlış!")
       kalan_hak -= 1
print("kalan hakkınız: ", kalan_hak)

if kalan_hak == 0:
    print("kaybettiniz :(")


