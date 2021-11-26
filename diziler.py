print("-"*30)

ad="Osman ERKAN"
yeniad=""
i=1
while i<=len(ad):
        print (ad[len(ad)-i])
        yeniad=yeniad+(ad[len(ad)-i])
        print(yeniad)
        i+=1

        
print("*"*50)

kelime=ad

print(kelime)

#aranacak=input("arayacağınız harf nedir?")
#try:kelime[::-1].index(aranacak)
#except ValueError: print("içinde",aranacak,"yok")
#else: print("içinde",aranacak,"var")

print("tersi",*reversed(kelime))

print(sorted(kelime))

print("kelime uzunluğu",len(kelime))

print("ilk 3 karakter",kelime[0:3])

print("ilk karakter",kelime[0])

print("sondan ilk karakter", kelime[-1:])

print("sondan 3 karakter",kelime[-3:])

print("hepsi",kelime[::])

print("sondan 3 karakter",kelime[-3::])


def çarp():
     
        sonuç=1
        kontrol=[]
        
        while True:
                sayı=input("sayı girin q= son")
                if sayı=="q":
                        break
                kontrol.append(sayı)
                sonuç *=int(sayı)
        if len(kontrol)<2:
                print("en az 2 sayı firin")
        else:
                print (len(kontrol),"adet sayı girdiniz.","kontrol dizisi=",kontrol,"çarpımları=",sonuç)



def dosyayayaz():
        import time
        
        f = open("deneme.txt", "r")
        içerik=f.readlines()
        print(içerik)
        içerik.insert(1, "Osman ERKAN\n")
        time.sleep(30)
        
        g=open("deneme.txt","w")
        g.writelines(içerik)
        f.close()
        g.close()
        


def say_to_say(sayı):
        width=10
        for base in 'dXob':
            print('{0:{width}{base}}'.format(sayı, base=base, width=width), end=' ')


#Sözlük tipi örnekler

isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
sözlük={}
for i in isimler:
	sözlük[i]=len(i)
	
print(sözlük)


harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sıralama={}
for i in harfler:
        sıralama[i]=harfler.index(i)

print(sıralama)

for i in range(len(harfler)):
        sıralama[harfler[i]]=i

print(sıralama)


#kümeler set

import random

liste = [random.randint(0, 100) for i in range(100)]

yüzden_küçük_sayılar = [i for i in liste if i < 10]

print(yüzden_küçük_sayılar)

küme=set(yüzden_küçük_sayılar)

print(küme)

def parola():
      
        tr = "şçöğüıŞÇÖĞÜİ"

        parola = input("Sisteme giriş için bir parola belirleyin: ")

        if set(tr) & set(parola):
            print("Parolanızda Türkçe harfler kullanmayın!")

        else:
            print("Parolanız kabul edildi!")

def sbg():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)


import random

def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set()

    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))

    return sayılar

print("random sayılar:",sayı_üret(0, 100, 10))
