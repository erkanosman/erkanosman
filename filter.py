##filter(fonksiyon, (liste, demet veya dizi)) fonksiyon None da olabilir.
seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
liste=list(result)
print(liste)

result = filter(lambda x: not(x % 2 != 0), seq)
liste=list(result)
print(liste)
#yada
result = filter(lambda x: x % 2 == 0, seq)
liste=list(result)
print(liste)

bbs=filter(lambda x: (x>=5 ), seq )
print(type(bbs))
liste=list(bbs)
print(liste)

# random list
random_list = [1, 'a', 0, False, True, '0']  #true olanlar 1,"a",True,"0" 
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)

#filtered_iterator = filter((x if False), random_list)  #True ve False konulamaz hata TypeError
#filtered_list = list(filtered_iterator)
#print(filtered_list)

