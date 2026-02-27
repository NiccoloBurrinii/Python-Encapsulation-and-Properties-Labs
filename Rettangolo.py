class Rettangolo:
    def __init__(self, base, altezza):
        self._base = base
        self._altezza = altezza
   
    @property
    def base(self):
        """Getter per base"""
        return self._base
   
    @base.setter
    def base(self, valore):
        """Setter con validazione"""
        if valore <= 0:
            raise ValueError("Base deve essere positiva")
        self._base = valore

r = Rettangolo(5, 3)
print(r.base)   # 5 (chiama getter)

r.base = 10     # Chiama setter con validazione
r.base = -2   # ValueError!