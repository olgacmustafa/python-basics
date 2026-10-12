print("hosgeldiniz")
ad=input("adinizi giriniz: ")
matematik_notu=int(input("matematik notunuzu giriniz: "))
fizik_notu=int(input("fizik notunu giriniz: "))
kimya_notu=int(input("kimya notunu giriniz: "))

ortalama=(fizik_notu+kimya_notu+matematik_notu)/3

if(ortalama<=50):
    print("sinifta kaldiniz.")
if(50<ortalama and ortalama<=70): 
    print("harf notunuz = BA")
if(ortalama>70):
    print("harf notunuz = AA")    

if(matematik_notu>=kimya_notu and matematik_notu>=fizik_notu):
    max=matematik_notu    
elif(fizik_notu>=kimya_notu):
    max=fizik_notu
else:
    max=kimya_notu    

if(matematik_notu<=kimya_notu and matematik_notu<=fizik_notu):
    min=matematik_notu    
elif(fizik_notu<=kimya_notu):
    min=fizik_notu
else:
    min=kimya_notu    


print (f"en yüksek dersiniz={max}")
print (f"en düsük dersiniz={min}")            

