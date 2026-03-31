title = "Python ile Programlama Dersleri"

# 1- 'title' değişkeni içerisindeki karakter sayısı nedir?

print(len(title))

# 2- 'title' içerisindeki 'Python' kelimesini alın.

print(title[0:6])

# 3- 'title' değişkeninin ilk 5 ve son 5 karakterini alın.

print(title[0:6] )
print(title[-6:-1])

# 4- 'title' değişkenini tersten yazdırınız.

print(title[::-1])

# 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
#    Örnek: Çınar Turan isimli öğrencinin 1.notu 60, 2.notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

isim=input("İsim Giriniz:")
nott=int(input("Notunuzu Girin: "))
metin=f"{isim} isimli öğrencinin 1. notu: {nott}, 2.notu {nott} ve not ortalaması {nott} olarak hesaplanmıştır."
print(metin)
