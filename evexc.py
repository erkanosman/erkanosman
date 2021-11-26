d1 = """

Python'da ekrana çıktı verebilmek için print() adlı bir
fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:

>>> print("Merhaba Dünya")

Şimdi de aynı kodu siz yazın!

>>> """

girdi = input(d1)

exec(girdi)

d2 = """

Gördüğünüz gibi print() fonksiyonu, kendisine
parametre olarak verilen değerleri ekrana basıyor.

Böylece ilk dersimizi tamamlamış olduk. Şimdi bir
sonraki dersimize geçebiliriz."""

print(d2)
