#lambda ve sair ileri fonksiyonlar
#listelerdeki tekrarlanan ögelerden kurtularak yeni liste yapmak
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
print()


s="python"
ss=[i for i in s]
print(ss)
print([i for i in s])

çift_mi=lambda sayı:sayı%2==0
print(çift_mi(2))
l=(1,2,3,4,5)
print([i*i for i in l])
print([i*i for i in (1,2,3,4,5)])
print(*map(lambda sayı: sayı**2, l))
oniletopla=lambda x:x+10
print(oniletopla(8))

# ternary op.
d=[12,4,56,78,96,97,45,3,10]
ç=[]
for i in d:
    if i%2==0: 
        ç.append(i)
print("ç=",ç,sum(ç))


ss=str([i for i in s])
birleştir=(lambda gelen,birleştirici: birleştirici.join(gelen.split()))
sss=birleştir(ss,"")
print(sss)

x=lambda:"hello"
print(x())
print(type(x))
y=(lambda x,y:x*y)
print((lambda x,y:x*y)(5,7))
print(y(4,5))

kalan=lambda x: x%2
print(kalan(11))

high_order = lambda x, lmbfunc: x*lmbfunc(x)
print(high_order(10, lambda x : x*x))

print((lambda x, y=3, z=5: x*y*z)(7))
print((lambda x, y=3, z=5: x*y*z)(x=7))
print((lambda *args : sum(args)) (3,5,7))
print((lambda x,y,z : x*y*z)(3,5,7))

mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(filter(lambda x : (x%2==0), mylist))
print(list_new)

mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(map(lambda x : x%2, mylist))
print(list_new)

from functools import reduce
list1 = [1,2,3,4,5,6,7,8,9]
sum = reduce((lambda x,y: x+y), list1)
print(sum)

#recursive fonksiyonlar

def azalt(s):
    if len(s)<1:
        return(s)
    else:
        print(s)
        #print(list(s))
        return azalt(s[1:])  #azalt buradan tekrar çağrılıyor. s baştan sona doğru azaltılıyor.

print(azalt(s))

print(s)        


def azalty(s):
    if len(s)<1:
        return(s)
    else:
        print(s)
        #print(list(s))
        return azalty(s[:-1]) #azalt buradan tekrar çağrılıyor. s sondan başa doğru azaltılıyor.

print(azalty("erkan"))


#####ters çevirme
def ters_çevir(s):
    if len(s) < 1:
        return s
    else:
        ters_çevir(s[1:])
        print(s[0],end=",")

ters_çevir('istihza')

print()

def ters_çevir(s):
    if len(s) < 1:
        return s
    else:
        return ters_çevir(s[1:]) + s[0]

print(ters_çevir('istihza'))

print()

def ters_çevir(s):
    if not s:
        return s
    else:
        return s[-1] + ters_çevir(s[:-1])

print(ters_çevir('istihza'))

#ters çevir

ters=""
for i in "OsmanErkan":
    ters=i+ters
    print("tersi=",ters)
print("tersi=",ters)
#veya
print("OsmanErkan"[::-1])

print()

#sayaçlar
def sayaç(sayı, sınır):
    print(sayı)
    if sayı == sınır:
        return 'bitti!'
    else:
        return sayaç(sayı+1, sınır)
print(sayaç(0, 100))

def sayaç(sayı, sınır):
    print(sayı)
    if sayı == sınır:
        return 'bitti!'
    else:
        return sayaç(sayı-1, sınır)
print(sayaç(100, 0))

#düz liste yap
l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
def düz_liste_yap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
print(düz_liste_yap(l))

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def topla(sayilar):#veilen sayıları toplama
    if len(sayilar) < 1:
        return 0
    else:
        ilk, son = sayilar[0], sayilar[1:]
        return ilk+topla(son)
print(topla(liste))

def toplay(sayılar):
	if len(sayılar)<1:
		return 0
	a,b= sayılar[0],sayılar[1:]
	print(a,b)
	return a+toplay(b)
sayılar=range(11)
print(toplay(sayılar))



def rf(f): #recursive fibonacci
	if f<=1:
		return f
	else:
		return (rf(f-1)+rf(f-2)) #rf çağrılıyor.

for i in range(11):
    print(i,".kademe fibonacci sayısı=",rf(i))        

def fac(n):
    if n==1:
        return n
    else:
        return n*fac(n-1) #fac çağrılıyor.

print("5 faktöryel =",fac(5))

def rfac(n,a=1):
    if n==0:
        return a
    else:
        #return  rfac(n-1) *n    
        return rfac(n - 1, n * a) 
print(rfac(2))
print(rfac(2,2))

def ifac(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result

for i in range(5):
    print(i, "! =", ifac(i))

def fib(n):
    """ recursive version of the Fibonacci function """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)




class FibonacciLike:

    def __init__(self, i1=0, i2=1):
        self.memo = {0:i1, 1:i2}

    def __call__(self, n):
        if n not in self.memo: 
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)  
        return self.memo[n]
       

fib = FibonacciLike()
lucas = FibonacciLike(2, 1)

for i in range(1, 16):
    print(i, fib(i), lucas(i))


class kFibonacci:

    def __init__(self, k, initials, coefficients):
        self.memo = dict(zip(range(k), initials))
        self.coeffs = coefficients
        self.k = k

    def __call__(self, n):
        k = self.k
        if n not in self.memo: 
            result = 0
            for coeff, i in zip(self.coeffs, range(1, k+1)):
                result += coeff * self.__call__(n-i)
            self.memo[n] = result  
        return self.memo[n]
    
fib = kFibonacci(2, (0, 1), (1, 1))
lucas = kFibonacci(2, (2, 1), (1, 1))

for i in range(1, 16):
    print(i, fib(i), lucas(i))

P = kFibonacci(2, (1, 2), (2, 1)) #pell numbers
for i in range(10):
    print(i, P(i))

def nP(n):#new pell sayıları
    if n < 2:#We can create another interesting series by adding the sum of previous two Pell numbers between two Pell numbers P(i) and P(i+1).
        return P(n)
    else:
        i = n // 2 + 1
        if n % 2:  # n is odd
            return P(i)
        else:
            return P(i-1) + P(i-2)
            
for i in range(20):
    print(nP(i), end=", ")
print()

nP = kFibonacci(4, (1, 2, 3, 5), (0, 2, 0, 1))
for i in range(20):
    print(nP(i), end=", ")
print()


