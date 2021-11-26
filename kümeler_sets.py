#kümeler-set()
k=set()
print(k)
print(type(k))
küme = set(["elma", "armut", "kebap"])
print(küme)
liste=(["elma", "armut", "kebap"])
print(liste)
küme=set(liste)
print(küme)
demet = ("elma", "armut", "kebap")
küme=set(demet)
print(küme)
kardiz = "Python Programlama Dili için Türkçe Kaynak"
küme=set(kardiz)
print(küme)
n="10"
küme=set(n)
print(küme)
bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
"dağıtım": "Ubuntu GNU/Linux"}
print(type(bilgi))
küme=set(bilgi)#sadece  keylerden bir küme 
print(küme)
küme=set(bilgi.items())#keylerden ve valueslerden küme
print(küme)
#ya da
liste = [(anahtar, değer) for anahtar, değer in bilgi.items()]
küme=set(liste)
print(küme)
kardiz = "Python Programlama Dili"
küme=set(kardiz)
print(küme)#her eleman sadece 1 tane olabilir

liste = ["elma", "armut", "elma", "kebap", "şeker", "armut",
"çilek", "ağaç", "şeker", "kebap", "şeker"]
print(set(liste))

liste = ["elma", "armut", "elma", "kiraz",
"çilek", "kiraz", "elma", "kebap"]
def kaunt():
    for i in set(liste):
        print("{} listede {} adet geçiyor".format(i,liste.count(i)) )
kaunt()


import random
liste = [random.randint(0, 1000) for i in range(1000)]
print(len(liste))     #1000

yüzden_küçük_sayılar = [i for i in liste if i < 100]
print(yüzden_küçük_sayılar)
yks=set(yüzden_küçük_sayılar)
print(yks)

ondan_küçük_sayılar=[i for i in liste if i<10]
print(ondan_küçük_sayılar)
oks=set(ondan_küçük_sayılar)
print(oks)

küme=set(liste)
print(len(küme))      #listedeki birden fazla olanlar ayıklanır, bir tanesi kalır.

küme=set()
l=(1,2,3)
küme.add(l)
print(küme)
l=46
küme.add(l)
print(küme)
l = 'Jacques Derrida'
küme.add(l)
print(küme)

k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])
print(k1.difference(k2))
print(k2.difference(k1))
print(k1-k2)
print(k2-k1)

(k1.difference_update(k2))
print(k1) #k1 den ortak olanlar çıkarılarak yeniden oluşturuldu.
print(k2) #k2 aynı kaldı.

hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
hayvanlar.discard("kedi") #"kedi" çıkarıldı.
print(hayvanlar)
hayvanlar.discard("yılan") # içerikte "yılan" yok ama , program hata vermez.
hayvanlar.remove("köpek")
print(hayvanlar)
#hayvanlar.remove("fare") # KeyError: 'fare' hatası oluşur.

k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.intersection(k2))
print(k1&k2)    #  işareti
print(k2.intersection(k1))
print(k1.intersection(k2)==k2.intersection(k1))

"""
tr = "şçöğüıŞÇÖĞÜİ"
parola = input("Sisteme giriş için bir parola belirleyin: ")
if set(tr)&set(parola):
    print("Parolanızda Türkçe harfler kullanmayın!")
"""

tr = "şçöğüıŞÇÖĞÜİ"
parola = "çilek"
print(set(tr)&set(parola))
parola = "kalem"
print(set(tr)&set(parola))

k1.intersection_update(k2)
print("yeni k1 artk {}".format(k1))
print("k2 aynı kaldı {}".format(k2))
print(k1.isdisjoint(k2)) #ortak küme boş mu? False, çünkü {1,3} ortak

a = set([1, 3, 5])
b = set([2, 4, 6])
print(a.isdisjoint(b)) #ortak küme boş mu? evet, True

a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b))       #a b nin alt kümesi mi? evet True
print(b.issuperset(a))     #b a yı kapsar mı? evet True

a = set([2, 4, 6, 8])
b = set([1, 3, 5, 7])
a.union(b)                       #yeni a ve b ile a ve b  aynı, a ve b  üzerine etkisiz
print("yeni a = {} yeni b= {} ".format(a,b))    #yeni a ve b ile a ve b  aynı, a ve b  üzerine etkisiz

c=a.union(b) #veya c=a|b    | işareti
print("birleşim kümesi c= {}". format(c))


kümey = set(["elma", "armut", "kebap"])
yenik = [1, 2, 3]
kümey.update(yenik) #kümey ve yenik den yeni kümey oluştur.
print(kümey)
meyva=set(["elma"])
kümey.update(meyva)  # kümey de "elma" zaten var, bu işlemin etkisi yok.
print(kümey)

a = set([1, 2, 5])
b = set([1, 4, 5])
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b)) #farkların birleşim kümesi
print(a.difference(b)|b.difference(a)) #farkların birleşim kümesi
print(a-b|b-a)


a = set([2, 4, 6, 8])
b = set([1,2, 3, 5,6, 7])
print(a.symmetric_difference(b))
a.symmetric_difference_update(b)
print(a)

a = set(["elma", "armut", "kebap"])
print(a.pop())#a.pop() a dan rastgele bir eleman siliyor
print(a)

dondurulmuş = frozenset(["elma", "armut", "ayva"]) #dondurulmuş üzerinde değişiklik yapılamayan setler
#metotları= copy,difference,intersection,isdisjoint,issubset,issuperset,symmetric_difference,union




#metotlar:
#add
#clear
#copy
#difference
#difference_update
#discard
#intersection
#intersection_update
#isdisjoint
#issubset
#issuperset
#pop
#remove
#symmetric_difference
#symmetric_difference_update
#union
#update






