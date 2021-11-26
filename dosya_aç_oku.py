d1 = open("ad1.txt") # dosyayı açıyoruz
d1_satırlar = d1.readlines()   # satırları okuyoruz

d2 = open("ad2.txt")
d2_satırlar = d2.readlines()

for i in d2_satırlar:
    if not i in d1_satırlar:
        print(i)

d1.close()
d2.close()

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("Sorgulamak istediğiniz harf: ")

sayı = ''

for s in metin:
    if harf == s:
        sayı += harf

print(len(sayı))

