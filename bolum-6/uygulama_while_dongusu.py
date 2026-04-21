# 1-Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
print("Baslangic degerini giriniz ")
bas=int(input("->"))
print("Bitis degerini giriniz ")
son=int(input("->"))
i=bas
while i<=son:
    if i%2==0:
        print(i)
    i+=1        

# 2-(1-100) arasındaki sayıları azaln şekilde yazdırınız
i=100
while i>0:
    print(i)
    i-=1

# 3-Kullanıcıdan aldığınız 5 sayıyı ekrana sıralı bir şekilde yazdırınız 
i=0
liste=[0,0,0,0,0]
while i<5:
    liste[i]=int(input(f"{i+1}. sayiyi giriniz :"))
    i+=1
liste.sort(reverse=True)
print(liste)

# 4-Klavyeden boşluk girildiği sürece kullanıcıdan bilgi istenmeye devam eden sorgu
username=input("Kullanici adini giriniz :")
while  " " in username:
    print("Bosluk birakilmaz")
    username=input("Kullanici adini giriniz :")
print("basarili:",username)    