#fonksiyonlar


def üsal(number, power):
    son="{} sayısının {} inci üssü {} sayısıdır"
    print(son.format(number, power,number**power))
    
def çarp(*sayı):
    son=1
    for i in sayı:
        son*=i
    print(son)

#sayı yerine args (standart kullanım)
def çarpı(*args):
    son=1
    for i in args:
        son*=i
    print("çarpım sonucu =",son)

çarpı(2,8,3,9)

#ascii

liste = ['elma', 'armut', 'erik']
temsil = ascii(liste)
print(temsil)
print(type(temsil))
print(temsil[0:2])
print(temsil[0:7])

#repr
print("şeker")
print("ascii dizisi=",ascii("şeker"))
print("repr dizisi=",repr("şeker"))

#bytes

print("cp 857 de € nin byte değeri",bytes('€', encoding='cp857', errors='xmlcharrefreplace'))
print("cp 1254 de € nin byte değeri",bytes('€', encoding='cp1254', errors='xmlcharrefreplace'))

print("65,10,12,11,66 dizisinin byte değeri",bytes([65, 10, 12, 11, 15, 66]))

a="Ali"
b=bytes(a,"ascii")
print (a,"nın ascii deki byte değeri",b,"dizisinin ilk elemanı", b[0],"dir")
print (b[0])

c=bytearray(a,"ascii")
print(c)
c[0]=ord("O")
print (c)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x == y])

#fibonacci
def fib1(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
#fibonacci
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#ternary veya üçlü karşılaştırma
x, y = 50, 25
small = x if x < y else y
print ("ternary small",small)
x,y,z=13,11,28
medium=x if (x>y and x<z) else y if (y>x and y<z) else z
print("üçlü medium",medium)


def çift(sayı):
    return sayı%2==0


çifte= lambda sayı: sayı % 2 == 0


l = [2, 5, 10, 23, 3, 6]
for i in l:print(i**2)
print([i**2 for i in l])
k=[i**2 for i in l]
print(k)
print(*map(lambda sayı: sayı ** 2, l))
#list, set, tuple aynı parametreler
print(*map(lambda x: x**2, [1,2,3,4,5]))
print(*map(lambda x: x**2, l))
print(*map(lambda x: x**2, (1,2,3,4,5)))
print(*map(lambda x: x**2, {1,2,3,4,5}))





def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(list(s))
        return azalt(s[1:])
    
def tersçevir(s):  
    if len(s) < 1:
        return s
    else:
        ilk,son=s[0],s[1:]
        #return tersçevir(s[1:])+s[0] veya
        return tersçevir(son)+ilk
        

    
# Primes < 1000        asal sayılar
from functools import reduce
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))


l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
print(len(l))
def düz_liste_yap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])

#mport time
toplam=0
sayılar=(6,7,8,9)
def topla(sayilar):
    if len(sayilar) < 1:
        return 0
    else:
        ilk, son = sayilar[0], sayilar[1:]
        print(ilk,son)
        #print(sayılar)
        print()
        return(topla(son))+ilk #aslında sadece (ilk)leri topluyor. 
        
print(topla(sayılar))        

#liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(topla(liste))

isimler = ['ahmet', 'can', 'mehmet', 'selin', 'abdullah', 'kezban']
print(max(isimler, key=len))
print(max(isimler))

def en_yüksek_rütbe(rütbe):
    rütbeler = {'er'        : 0,
                'onbaşı'    : 1,
                'çavuş'     : 2,
                'asteğmen'  : 3,
                'teğmen'    : 4,
                'üsteğmen'  : 5,
                'yüzbaşı'   : 6,
                'binbaşı'   : 7,
                'yarbay'    : 8,
                'albay'     : 9}

    return rütbeler[rütbe]

askerler = {'ahmet': 'onbaşı',
            'mehmet': 'teğmen',
            'ali': 'yüzbaşı',
            'cevat': 'albay',
            'berkay': 'üsteğmen',
            'mahmut': 'binbaşı'}

print(max(askerler.values(), key=en_yüksek_rütbe))

for k, v in askerler.items():
    if askerler[k] in max(askerler.values(), key=en_yüksek_rütbe):
        print(v, k)

for k, v in askerler.items():
    if askerler[k] == max(askerler.values(), key=en_yüksek_rütbe):
        print(v, k)


x = min(("Mike", "John", "Vicky"),key=len)
print(x)
a = (1, 5, 3, 9)
x = min(a)
print(f"{a} içindeki sayların en küçüğü {x} olur.".format(a,x))

lst1 = [1, 2, 3]
lst2 = [5, 15, 40, 25, 35, 45]
Minimum = min(lst1, lst2, key = len)
print("Minimum value : ", Minimum)

def str_length(s):
    return len(s)

lst = ['LAtra', 'abc', 'Solu']
x = min(lst)
print("normal min=",x) #normal min
print(min(lst, key=str_length)) #fonksiyona göre min
print(min(lst, key=len)) #bu daha kısa ve güzel

listem=[]
x= min(listem, default =20)
print("Minimum value : ",x)
print(listem)

isimler = ['ahmet', 'çiğdem', 'ışık', 'şebnem', 'zeynep', 'selin',"iskender","ismail","ismit","ismıt"]
print(sorted(isimler))
import locale
print(str(locale.getlocale()))
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
print(str(locale.getlocale()))
print(sorted(isimler, key=locale.strxfrm)) #türkçe sıralam yanlış i ı dan önce iskender ismailden önce.


print(sorted('afgdhkıi', key=locale.strxfrm))# i ı dan once geliyor, türkçe alfabeye ters
print(sorted([10, 9, 4, 14, 20])) #sayılar her zaman doğru sıralanır.

harfler = "abcçdefgğhıijklmnoöprsştuüvyz" #türkçe alfabe
çevrim = {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4,
          'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9,
          'ı': 10, 'i': 11, 'j': 12, 'k': 13,
          'l': 14, 'm': 15, 'n': 16, 'o': 17,
          'ö': 18, 'p': 19, 'r': 20, 's': 21,
          'ş': 22, 't': 23, 'u': 24, 'ü': 25,
          'v': 26, 'y': 27, 'z': 28}
        
#veya çevrim = {i: harfler.index(i) for i in harfler}

def sırala(kelime):
    return ([çevrim.get(kelime[i]) for i in range(len(kelime))])
#çevrim.get("ahmet"[1])=9 çevrim.get("ahmet"[0]=0)
#def sırala(kelime): #en iyi sıralam
#    return ([çevrim.get(kelime[i]) for i in range(len(kelime))])


print(*sorted(isimler, key=sırala), sep='\n') #doğru sıralama

elemanlar = [('ahmet',       33,    'karataş'),
             ('mehmet',      45,    'arpaçbahşiş'),
             ('sevda',       24,    'arsuz'),
             ('arzu',        40,    'siverek'),
             ('abdullah',    30,    'payas'),
             ('ilknur',      40,    'kilis'),
             ('abdurrezzak', 40,    'bolvadin')]

print(*sorted(elemanlar), sep='\n') #normal sıralama
print()
print()

def sırala(liste):
    return liste[1] # listenin 1.sütunu yaş

print(*sorted(elemanlar, key=sırala), sep='\n') #yaş sütununa göre sıralama
print()
print()

def sırala(liste):
    return (liste[1], liste[2]) #önce yaş sütununa,sonra memlekete göre sırala, yaşı aynı olanlar için

print(*sorted(elemanlar, key=sırala), sep='\n') #yaş ve memleket sütunlarına göre sıralama

#def sırala(kelime): #en iyi sıralam
#    return ([çevrim.get(kelime[i]) for i in range(len(kelime))])

a=["python"]
b="python"
print(a[::])
print(b[::])
print(a[:])
print(b[:])
print(a[0:3]) #[python"]
print(b[0:3]) #pyt
print(b[:-1]) #pytho
print(b[-1])  #n
print("ters",b[-1:-7:-1]) #nohtyp
print("ters",b[-1::-1])
print(b[-1:-6:-1]) #nohty
print(a[0][0]) #p
print(a[0]) #python

s="Python" # initial string
stringlength=len(s) # calculate length of the list
slicedString=s[stringlength::-1] # slicing ****tersi
print (slicedString) # print the reversed string

print(s[len(s)::-1]) #tersi
print(s[::-1]) #tersi 

s = "Python" # initial string
reversedString=[]
uzun = len(s) # calculate length of string and save in index
while uzun > 0: 
    reversedString += s[ uzun - 1 ] # save the value of str[index-1] in reverseString
    uzun = uzun - 1 # decrement index
print((reversedString)) # reversed string
print()
print()

s="Python" 
reversedstring=''.join(reversed(s))
print(reversedstring)

s = 'Python' #initial string
reversedstr=''.join(reversed(s)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversedstr) #print the reversed string

print("".join(reversed(s)))

#sum(iterable,start)
print(sum([1, 2, 3, 4, 5])) # sum values in a list
print(sum((1, 2, 3, 4, 5))) # sum values in a tuple
print(sum({1, 2, 3, 4, 5})) # sum values in a set
print(sum({1: "one", 2: "two", 3: "three"})) # sum values in a 
print(sum([10, 20, 30], 100))
cn=(4+3j, 7+5j, 8+3j)
print("sum of complex numbers:", sum(cn)),
#numpy nin num() fonksiyonu da basit dizilerde aynı 

print(type(s)) #type fonksiyonu
print(type(""))
print(type(()))
print(type([]))
print(type({}))
print(type(1))

#zip fonksiyonu
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
a3=(1,2,3,4,5)
print(list(zip(a1, a2,a3)))
print(list(zip("abcdef",range(5),"klmno")))
print(list     (zip    (a3, (map(lambda x: x**2, a3)),a1,a2  )     ))
print(list(zip("abcd","efgh")))
çevrimci=dict(zip((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29),("a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z")))
print(çevrimci)


print(list(vars()))
print(list(vars(list)))
print(list(vars(dict)))
print(list(vars(tuple)))
print(list(vars(set)))
print(list(vars(bytes)))