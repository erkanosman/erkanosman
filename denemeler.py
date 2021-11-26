import math as m

def alan(çap):
    
    yarıçap=çap/2
    
    alan=m.pi*pow(yarıçap,2)
    a
    return alan
    
def choice(c):
    if c%2== 0:
        return"python"
    else:
        return"java"

print(f"Hello Python, tell me what I should learn. {choice(0)}")


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
            print(a, end=' ')
            a, b = b, a+b
    print()

def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result=append(a)    #result+[a] da olur.    # see below
         a, b = b, a+b
     return result

def ask(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)




tarih="02.02.2019"
gün="salı"
vakit="akşam"
print(tarih,gün,vakit,"buluşalım",end=".\n")


#asal sayılar
for n in range(2,10):
	for x in range(2,n):
		if n%x==0:
			print(n, "eşittir",x,"*",n//x)
			break
	else:
	 print(n,"asal")








#çift sayılar
a = 0

while a < 11:
    a += 1
    if a % 2 == 0:
        print(a)





#yaz

hakkında = open("tekst.txt", "a",encoding="utf-8")

karakter=""

while karakter != "q":

    karakter = input("yazmak istediğiniz karakter: ")

    print(karakter, file=hakkında)
 

hakkında.close()

#oku
hakkında = open("tekst.txt", encoding="utf-8")

harf = input("Sorgulamak istediğiniz harf: ")

sayı = 0

for karakter_dizisi in hakkında:
    for karakter in karakter_dizisi:
        if harf == karakter:
            sayı += 1
            print(karakter)
print(sayı)

hakkında.close()



