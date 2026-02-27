class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
   
    @property
    def area(self):
        """Area calcolata dinamicamente"""
        return self.base * self.altezza
   
    @property
    def perimetro(self):
        """Perimetro calcolato"""
        return 2 * (self.base + self.altezza)

r = Rettangolo(5, 3)
print(r.area)       # 15 (calcolato)
print(r.perimetro)  # 16 (calcolato)

r.base = 10
print(r.area)       # 30 (aggiornato automaticamente!)

r.area = 100      # AttributeError (read-only)