from Rettangolo_esercitazione import Rettangolo
class Punto:
    """Classe helper per coordinate"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class RettangoloConPosizione(Rettangolo):
    """Rettangolo con posizione e orientamento"""
    
    def __init__(self, base, altezza, x=0, y=0, angolo=0):
        super().__init__(base, altezza)
        self.centro = Punto(x, y)
        self.angolo = angolo  # Gradi di rotazione
    
    def trasla(self, dx, dy):
        """Trasla rettangolo"""
        self.centro.x += dx
        self.centro.y += dy
    
    def ruota_angolo(self, gradi):
        """Ruota di N gradi"""
        self.angolo = (self.angolo + gradi) % 360
        
        # Se ruota di 90° o 270°, scambia dimensioni
        if gradi % 180 == 90:
            self.ruota()
    
    @property
    def vertici(self):
        """Calcola coordinate dei 4 vertici"""
        # Semplificato: assume angolo 0
        x, y = self.centro.x, self.centro.y
        b, h = self.base, self.altezza
        
        return [
            Punto(x - b/2, y - h/2),  # Basso sinistra
            Punto(x + b/2, y - h/2),  # Basso destra
            Punto(x + b/2, y + h/2),  # Alto destra
            Punto(x - b/2, y + h/2),  # Alto sinistra
        ]
    
    def contiene(self, punto):
        """Verifica se punto è dentro rettangolo"""
        x, y = self.centro.x, self.centro.y
        b, h = self.base, self.altezza
        
        return (abs(punto.x - x) <= b/2 and 
                abs(punto.y - y) <= h/2)


# Test con posizione
r_pos = RettangoloConPosizione(10, 6, x=5, y=5)
print(f"Centro: {r_pos.centro}")
print(f"Vertici:")
for v in r_pos.vertici:
    print(f"  {v}")

p_test = Punto(7, 6)
print(f"\nPunto {p_test} dentro rettangolo? {r_pos.contiene(p_test)}")
