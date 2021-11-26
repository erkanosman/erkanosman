



class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    @classmethod
    def personel_sayısını_görüntüle(cls):
        print(len(cls.personel))

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)


#alternatives constructors
liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(ölçüt=None, değer=None):
    for li in liste:
        if not ölçüt and not değer:
            print(*li, sep=', ')

        elif ölçüt == 'isbn':
            if değer == li[0]:
                print(*li, sep=', ')

        elif ölçüt == 'yazar':
            if değer == li[1]:
                print(*li, sep=', ')

        elif ölçüt == 'eser':
            if değer == li[2]:
                print(*li, sep=', ')

        elif ölçüt == 'yayınevi':
            if değer == li[3]:
                print(*li, sep=', ')

#ya da
def sorgula(ölçüt=None, değer=None):
    d = {'isbn'     : [li for li in liste if değer == li[0]],
         'yazar'    : [li for li in liste if değer == li[1]],
         'eser'     : [li for li in liste if değer == li[2]],
         'yayınevi' : [li for li in liste if değer == li[3]]}

    for öğe in d.get(ölçüt, liste):
        print(*öğe, sep = ', ')

def bul(değer, sıra):
    return [li for li in liste if değer == li[sıra]]

#ya da
def sorgula(ölçüt=None, değer=None):
    d = {'isbn'     : bul(değer, 0),
         'yazar'    : bul(değer, 1),
         'eser'     : bul(değer, 2),
         'yayınevi' : bul(değer, 3)}

    for öğe in d.get(ölçüt, liste):
        print(*öğe, sep = ', ')

class Sorgu():
    def __init__(self):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

    def bul(self, değer, sıra):
        return [li for li in self.liste if değer == li[sıra]]

    def sorgula(self, ölçüt=None, değer=None):
        d = {'isbn'     : self.bul(değer, 0),
             'yazar'    : self.bul(değer, 1),
             'eser'     : self.bul(değer, 2),
             'yayınevi' : self.bul(değer, 3)}

        for öğe in d.get(ölçüt, self.liste):
            print(*öğe, sep = ', ')


class Sorgu():
    def __init__(self, değer=None, sıra=None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra]]

        for i in l:
            print(*i, sep=', ')

    @classmethod
    def isbnden(cls, isbn):
        cls(isbn, 0)

    @classmethod
    def yazardan(cls, yazar):
        cls(yazar, 1)

    @classmethod
    def eserden(cls, eser):
        cls(eser, 2)

    @classmethod
    def yayınevinden(cls, yayınevi):
        cls(yayınevi, 3)


class Giriş():
    def __init__(self, mesaj='Müşteri numaranız: '):
        cevap = input(mesaj)
        print('Hoşgeldiniz!')

    @classmethod
    def paroladan(cls):
        mesaj = 'Lütfen parolanızı giriniz: '
        cls(mesaj)

    @classmethod
    def tcknden(cls):
        mesaj = 'Lütfen TC kimlik numaranızı giriniz: '
        cls(mesaj)

#cls kelimesi Python açısından bir zorunluluk değildir. 
#Yani yukarıdaki sınıfı mesela şöyle de yazabilirdik:

class Giriş():
    def __init__(self, mesaj='Müşteri numaranız: '):
        cevap = input(mesaj)
        print('Hoşgeldiniz!')

    @classmethod
    def paroladan(snf):
        mesaj = 'Lütfen parolanızı giriniz: '
        snf(mesaj)

    @classmethod
    def tcknden(snf):
        mesaj = 'Lütfen TC kimlik numaranızı giriniz: '
        snf(mesaj)