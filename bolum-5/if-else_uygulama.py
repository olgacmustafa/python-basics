# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

print("-----ARAÇ MASRAF HESAPLAMA UYGULAMASINA HOŞGELDİNİZ...-----")
print("1-)Benzin")
print("2-)Dizel")
print("3-)LPG")

yakit_turu=int(input("Yakıt türünüzü seçiniz (1,2,3) : "))
if((yakit_turu==1)or(yakit_turu==2)or(yakit_turu==3)):
     print("işleme devam ediliyor...")
else :
     print("Yanlış yakıt türü seçtiniz...")  
     exit()
gidilen_mesafe=int(input("Gideceğiniz toplam mesafe ne kadardır : "))

if(yakit_turu==1):
     toplam=39.35*gidilen_mesafe
     print("Toplam Masrafınız: ", toplam , "TL")
elif(yakit_turu==2):
     toplam=41.71*gidilen_mesafe
     print("Toplam Masrafınız: ", toplam ,"TL")
elif(yakit_turu==3):
     toplam=20.28*gidilen_mesafe
     print("Toplam Masrafınız: ", toplam ,"TL")

    
# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

print("NOT HESAPLAMA UYGULAMASINA HOŞGELDİNİZ..")
yazili_1=int(input("1. yazılı sınav notunuzu giriniz: "))
yazili_2=int(input("2. yazılı sınav notunuzu giriniz: "))
sozlu_1=int(input("sozlu sınav notunuzu giriniz: "))

ortalama=(yazili_1+yazili_2+sozlu_1)/3

if((ortalama>=0) and (ortalama<=24)):
    print("Harf notunuz: 0")
elif((ortalama>=25) and (ortalama<=44)):
    print("Harf notunuz: 1")
elif((ortalama>=45) and (ortalama<=54)):
    print("Harf notunuz: 2")
elif((ortalama>=55) and (ortalama<=69)):
    print("Harf notunuz: 3")
elif((ortalama>=70) and (ortalama<=84)):
    print("Harf notunuz: 4")            
elif((ortalama>=85) and (ortalama<=100)):
    print("Harf notunuz: 5")
else:
    print("Notlarınızı belirtilen aralıkta giriniz:(0-100)")

    




















