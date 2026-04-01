sayilar= [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

for x in sayilar:
    print(x)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

for x in sayilar:
    if(x%3==0):
        print(x)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

toplam=0
for x in sayilar:
    toplam+=x
print(toplam)    

urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)

for x in urunler:
    if(x.find("iphone")!=-1):
        print(x)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
adet=0
for x in urunler:
    if(x.find("samsung")!=-1):
        adet+=1
print(adet)        