class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyet = []
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyet.append(kabiliyet)

    def kabiliyet_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyet:
            print(kabiliyet)