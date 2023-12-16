gün = int(input("ayda kaç gün çalışıyorsunuz?: "))

gidiş = int(input("gidiş ücreti (TL): "))

dönüş = int(input("dönüş ücreti (TL): "))

result = gün * (gidiş + dönüş)

print("aylık yol ücretiniz: ", result, "TL")
