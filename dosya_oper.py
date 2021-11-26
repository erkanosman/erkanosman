

f= open("C:\\Users\\oerkan\\AppData\\Local\\Programs\\Python\\Python37\\fihrist.txt")
print(f.read())
print(f.tell())
print(f.seek(0))
f.close()

f= open("C:\\Users\\oerkan\\AppData\\Local\\Programs\\Python\\Python37\\fihrist.txt","a")
f.write("\nosman erkan tel: 000000000")
f.close()

f=open("C:\\Users\\oerkan\\AppData\\Local\\Programs\\Python\\Python37\\fihrist.txt","r+")
veri = f.read()
f.seek(0) #Dosyayı başa sarıyoruz
f.write("\nleyla leyla : 222222333444"+veri)
f.close()


f=open("C:\\Users\\oerkan\\AppData\\Local\\Programs\\Python\\Python37\\fihrist.txt","r+")
veri=f.readlines()
print(type(veri))
veri.insert(10, "\n onucuya ekleme : 0322 234 45 45\n")
f.seek(0)
f.writelines(veri)
f.close()
print(f.closed)

