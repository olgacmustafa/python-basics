# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz. 
liste=["Toyota","Bmw","Reanult","Mercedes"]

# 2- Liste kaç elemanlıdır?

print(len(liste))
# 3- Listenin ilk ve son elemanı nedir?
print("ilk eleman: "+liste[0]+" son eleman:"+liste[-1])
# 4- "Renault" markasını "Togg" ile güncelleyiniz.
liste[2]="Togg"
# 5- "Togg" listenin bir elemanı mıdır?
print("Togg" in liste)
# 6- Listenin ilk 2 elemanını alınız.
print(liste[:2])
# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
liste=liste+["Ford","Citroen"]

# 8- Listenin son elemanını siliniz.
del liste[-1]

# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenciler=[["yigit","bilgi",2010,70,80,90],["ada","bilgi",2011,70,70,80],["çınar","turan",2017,60,60,90]]
# 10- Öğrencilerin yaşlarını hesaplayınız.
yas1=2026-ogrenciler[0][2]
yas2=2026-ogrenciler[1][2]
yas3=2026-ogrenciler[2][2]


# 11- Öğrencilerin not ortalamalarını hesaplayınız.

ortalama1=(ogrenciler[0][3]+ogrenciler[0][4]+ogrenciler[0][5])/3
ortalama2=(ogrenciler[1][3]+ogrenciler[1][4]+ogrenciler[1][5])/3
ortalama3=(ogrenciler[2][3]+ogrenciler[2][4]+ogrenciler[2][5])/3

print(yas1)
print(ortalama1)