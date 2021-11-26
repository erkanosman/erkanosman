
sesli_harfler = 'aeıioöuüAEIİOÖÜU'
sayaç = 0

kelime = input('Bir kelime girin: ')

for harf in kelime:
        if harf in sesli_harfler:
            sayaç += 1

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, sayaç))



sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

for harf in kelime:
    if seslidir(harf):
        sayaç += 1

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, sayaç))


sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))




sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    print('sayaç değişkeninin değeri şu anda: ', sayaç)
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))



sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))





sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(n):
    for harf in kelime:
        if seslidir(harf):
            n += 1
    return n

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))




sayaç = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artır(sayaç, kelime)))

def çalıştır():
    kelime = kelime_sor()
    ekrana_bas(kelime)
#if __name__ == '__main__':#dikkat eğer bu bölümü ayrı bit prg olarak kaydeder ve import sayaç ile çağırırsak
çalıştır()

class HarfSayacı:#class
    def __init__(self):
        self.sesli_harfler = 'aeiıöouüAEİIÖOUÜ'
        self.sayaç = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç += 1
        return self.sayaç

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayısı = self.artır()
        print(mesaj.format(self.kelime, sesli_harf_sayısı))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

#if __name__ == '__main__':
sayaç = HarfSayacı()
sayaç.çalıştır()


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Rakun')
iter(rev)
for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
     print(char)


#yeni
class HarfSayacı:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuüAEIİOÖUÜ'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            if self.sessizdir(harf):
                self.sayaç_sessiz += 1
        return (self.sayaç_sesli, self.sayaç_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artır()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

#if __name__ == '__main__':
sayaç = HarfSayacı()
sayaç.çalıştır()

