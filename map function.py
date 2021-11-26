#map function
#map(function, iterable[, iterable1, iterable2,..., iterableN])
#function can be built-in functions, classes, methods, lambda functions, and user-defined functions.

l=[1, 16, 25, 16, 4, 81, 100]

def karesi(n):
    return n ** 2

print(list(map(karesi, l)))

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
liste=(list(int_nums))
print(liste)
print(str_nums) #orijinal list değişmez

numbers = [-2, -1, 0, 1, 2]
abs_v=list(map(abs,numbers)) ; print(abs_v) #dikkat ; var
float_v=list(map(float,numbers)) ; print(float_v)

words = ["Welcome", "to", "Real", "Python"]
len_v=list(map(len,words)) ; print(len_v)

kare_v=list(map(lambda x: x**2,l)); print(kare_v)

first_it = [1, 2, 3]  
second_it = [4, 5, 6, 7]
pow_v=list(map(pow,first_it,second_it));print(pow_v)#####    ilginç   ###7 boşta kaldı

print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))

print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))

string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize,string_it)))
print(list(map(str.lower,string_it)))
print(list(map(str.upper,string_it)))

with_spaces = ["processing ", "  strings", "with   ", " map   "]
print(list(map(str.strip, with_spaces)))# boşluklardan yani " " lardan kurtarıyoruz.

with_dots = ["processing..", "...strings", "with....", "..map.."]
print(list(map(lambda s: s.strip("."), with_dots)))#noktalardan kurtarıyoruz.



import re
def clean(word):
     return re.sub(r'[!?.:;,"()-]', "", word)

text = """Some people, when confronted with a problem, think
"I know, I'll use regular expressions."
Now they have two problems. Jamie Zawinski"""
words=text.split()
print(words)
print(list(map(clean,text)))

def rotate_chr(c): #şifreleme gibi
    rot_by = 15
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

print("".join(map(rotate_chr, "My secret message goes here.")))

def power(x):
    return x,x**2,x**3

print(list(map(power,l)))

import math
numbers = [1, 2, 3, 4, 5, 6, 7]
list(map(math.factorial, numbers))

def to_fahrenheit(c):
    return 9 / 5 * c + 32
def to_celsius(f):
    return (f - 32) * 5 / 9
cler=(10,15,20,25,30)
print(cler,set(map(to_fahrenheit,cler)))

print(list(map(float, ["12.3", "3.3", "-15.2"])))
print(list(map(int, ["12", "3", "-15"])))

def to_float(number):
    try:
         return float(number.replace(",", "."))
    except ValueError:
         return float("nan")

print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"])))         

import math

def positive_mi(num):
    return num>=0 #True veya False

def karekök(numbers):
    köklist=(map(math.sqrt,filter(positive_mi,numbers)))    
    return list(köklist)

print((karekök(numbers)))
#numbers=[1, 2, 3, 4, 5, 6, 7]
#[1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907]

print(karekök(([25, 9, 81, -16, 0])))#[5.0, 3.0, 9.0, 0.0]

import functools
import operator
import os
import os.path

files = os.listdir(os.path.expanduser("C:\\Users\\oerkan\\AppData\\Local\\Programs\\Python\\Python37"))

print(functools.reduce(operator.add, map(os.path.getsize, files)))
print(sum(map(os.path.getsize, files)))

from itertools import starmap
print(list(starmap(pow, [(2, 7), (4, 3)])))#2^7 ve 4^3
print(list(map(pow, (2, 7), (3,4), )))#2^3 ve 7^4 


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3=[7,8,9]
result = map(lambda x, y,z: x + y+z, numbers1, numbers2,numbers3)
print(list(result))

carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)

print(list(carts))


def ismin_ne():
    isim = input("ismin ne? ")
    if (n:=len(isim))>10:  #******dikkat  yeni tanımlama 
	    print(f"isim çok uzun {n} harf var")
        
    else:
	    return isim