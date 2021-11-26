

hakkında = open("ad1.txt")  #encoding="utf-8")

#harf = input("Sorgulamak istediğiniz harf: ")

sayı = 0

for karakter_dizisi in hakkında:
    print(repr(karakter_dizisi))
    print(len(repr(karakter_dizisi)))
#    for karakter in karakter_dizisi:
#        if harf == karakter:
    sayı += 1
    print("dosyada {} isim kayıtlı".format(sayı))


hakkında.close()


