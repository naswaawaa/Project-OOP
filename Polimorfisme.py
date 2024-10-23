class Hewan:
    def suara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")
    
class Kucing(Hewan):
    def suara(self):
        return "MIAWWWWWW"

class Sapi(Hewan):
    def suara(self):
        return "MOOOOOOO"
    
    def cetak_suara(Hewan):
        print(Hewan.suara())
        
hewan1 = Kucing()
hewan2 = Sapi()