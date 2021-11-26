#max, max
a=[12,25,35,2,4,12,99,5,6,5,6]
print(a); print(len(a));print(max(a))

yer=a.index(max(a))
print(yer)

howmany_max=a.count(max(a))
print(howmany_max)

for i in range(0,howmany_max):
    a.remove(max(a))

print(a)
print(len(a))
print(max(a))
yer=a.index(max(a)); 
print(yer)









