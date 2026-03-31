a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?

sayi1=int(input("1. sayi girin: "))
sayi2=int(input("2. sayi girin: "))

carpim=sayi1*sayi2

toplam=a+b+(c[0]+c[1])

sonuc=carpim-toplam

print(sonuc)

# 2- c' nin b' ye kalansız bölümünü hesaplayınız.

sonuc=(c[0]+c[1])//b
print(sonuc)

# 3- (a,b,c) toplamının mod 7' si nedir?

toplam=a+b+(c[0]+c[1])
sonuc=toplam%7
print(sonuc)

# 4- b' nin a. kuvvetini hesaplayınız.

sonuc=b**a
print(sonuc)

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?

sonuc=c**3
print(sonuc)

# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?

sonuc=c[0]+c[1]+c[2]
print(sonuc)