msg = "welcome baby"
print (msg)

k=("kitap")
k=sorted(k)
print(k)


for i in (k):
     print("%15s" %i)

print("|%15s|" %"istihza")


for i in range(100):
     print("%%%s" %i,end=",")


for i in range(100):
     print("%s" %i,end="-")     


#for i in range(100):
#    print("%%s" % i)

print("\n","**%15s//" %"istihza")


book="engineering"
print("%s kitabının satış fiyatı %s liradır" %(book,"25"))


sayfa = """
<html>
    <head>
        <title> %(dil)s </title>
    </head>

    <body>
        <h1> %(dil)s </h1>
        <p>Web sitemize hoşgeldiniz! Konumuz: %(dil)s</p>
    </body>
</html>
"""

print(sayfa % {"dil": "Python Programlama Dili"})


kardiz = "istihza"

for sıra, karakter in enumerate(kardiz, 1):
    print("%s. karakter: %s" %(sıra, karakter))


miktar,ürün=25,"elma"
print("depoda %(miktar)s kilo %(ürün)s kaldı" %{"miktar":miktar,"ürün":ürün}) 
print("{} {}".format(miktar,ürün))

print("%d"%23)
print("%10d"%23)                                                   
print("%10.5d"%23)
print("%010d"%23)


for i in range(128):
     print("%s ==> %c" %(i, i))

for sıra, karakter in enumerate(dir(str)):
    if (sıra % 3) == 0:     #sıra modulus 3
        print("\n", end="") #her üçlüde bir yeni satır
    print("%-20s" %karakter, end="")

for i in range(20):
    print("%5d%5o%5X" %(i, i, i))

for i in range(20):
    print("%(deger)5d%(deger)5o%(deger)5X" %({"deger": i}))


ad="osman"
soyad="erkan"
print("benim adım {} soyadım {}".format(ad,soyad))

print("{:,.2f}".format(1234567890))

print("{:,.2f}".format(1234567890))

#print (f'Sayıların toplamı {int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: ")) } eder.')


liste_1 = ["Ali", "Veli", ["Ayşe",["ayşe1","ayşe2","ayşe3"], "Nazan", "Zeynep"], 34, 65, 33, 5.6]
for eleman in liste_1:
    print(f"{eleman} adlı öğenin veri tipi: {type(eleman)}")
print(liste_1[2][0])
print(liste_1[2][0][1])
print(liste_1[2][1][2][4])

comm=dir(str)
print(type(comm))
print(comm)


sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayılar:
    #print(range(i[0],i[1]))
    #print(range(*i))
    #print(*range(*i))

    print()
    print(*range(i[0],i[1]))



alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
alist=list(alfabe)
print(alist)
blist=list()
print(blist)
print(list())
print(f"boş liste {list()} gibidir")

print(list(range(0,len(liste_1),2)))

meyveler = ["elma", "armut", "çilek", "kiraz"]
meyveler.append("muz")
print(meyveler)
del meyveler[0]
print(meyveler)
meyveler[0]="pepino"
print(meyveler)
meyveler[0:len(meyveler)]="karpuz","kavun","üzüm","erik"
print(meyveler)
meyveler=meyveler+["kayısı"]
print(meyveler)


sayılar = 0
notlar = []
for i in range(5):
	veri=int(input(f"{i+1}.notu giriniz"))
	sayılar += veri
	notlar +=[veri]

print("girdiğiniz notlar",*notlar)
print("ortalama",sayılar/5)
