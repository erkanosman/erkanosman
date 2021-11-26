





global toplam
toplam=0
sayılar=[6,7,8,9]
def topla(sayilar):
    global toplam
    if len(sayilar) < 1:
        return 0
    else:
        ilk, son = sayilar[0], sayilar[1:]
        print(ilk,son)
        toplam+=ilk
        print("toplam =",toplam)
        print("xxxxxxxx")
        return(ilk+topla(son))#aslında sadece (ilk)leri topluyor. 
        
#print(topla(sayılar))        
#print(toplam)

#liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(topla(liste))
range=range(1,11)
#print(list(range))
print(topla(range))

def yazıcı():
    def yaz(mesaj):
        print(mesaj)
    return yaz
y=yazıcı()
y("hello babe")

def kapsayıcı_fonk():
    non_local_değişken = 1

    def iç_fonk():
        non_local_değişken = 2
        print(non_local_değişken)
    return iç_fonk
dönen= kapsayıcı_fonk()
print(dönen())

a = 1
def fonk():
    global a
    a += 1
    print(a)

def kapsayıcı_fonk():
    non_local_değişken = 1
    def iç_fonk():
        nonlocal non_local_değişken
        non_local_değişken += 1
        print(non_local_değişken)
    return iç_fonk
dfl = kapsayıcı_fonk()

def yazıcı(mesaj):
    def yaz():
        nonlocal mesaj
        mesaj += " Dünya"
        print(mesaj)
    return yaz
yaz = yazıcı("Merhaba") #yaz()

def yazıcı(mesaj):
    def yaz():
        mesaj += " Dünya"
        print(mesaj)
    return yaz

y = yazıcı("Merhaba Dünya")
#y() hata çünkü mesaj önceden belirlenmiş
#UnboundLocalError: local variable 'mesaj' referenced before assignment

def sayıcı():
    sayı = 0
    def say():
        nonlocal sayı
        sayı += 1
        return sayı
    return say #say() değeri dönüyor
s=sayıcı()

def işlem_yap(sayı, bölen, *eklenenler):
    sonuç = sayı / bölen

    for i in eklenenler:
        sonuç += i
    return sonuç

def işlem_yapıcı(*eklenenler):
    ekle = 0
    for i in eklenenler:
        ekle += i

    def işlem(sayı, bölen):
        return sayı/bölen + ekle
    return işlem

iş1=işlem_yapıcı(1,4,5)
iş2=işlem_yapıcı(3,6,2)

def dks(dosya, karakter):

    def karakter_sayısı(karakter_dizisi):
        sayaç = 0
        for i in karakter_dizisi:
            if i == karakter:
                sayaç += 1
        return sayaç

    if type(dosya) == str:
        with open(dosya, "r") as f:
            return karakter_sayısı(f.read())
    else:
        return karakter_sayısı(dosya.read())

def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()

def factorial(number):
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")
    # Calculate the factorial of number
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)#recursive  fonksiyon
    return inner_factorial(number)

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power
iki=generate_power(2)
üç=generate_power(3)

sample = []
def mean():#ortalama
    #sample=[]
    def inner_mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return inner_mean
sm=mean()


def topla(*args):
	return sum(list(args))
