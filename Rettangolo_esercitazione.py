import math

class Rettangolo:
    """Classe rettangolo con properties geometriche"""
    
    def __init__(self, base, altezza):
        """Inizializza rettangolo con dimensioni validate"""
        self.base = base      # Usa setter
        self.altezza = altezza  # Usa setter
    
    @property
    def base(self):
        """Getter base"""
        return self.__base
    
    @base.setter
    def base(self, valore):
        """Setter base con validazione > 0"""
        if valore <= 0:
            raise ValueError("Base deve essere maggiore di zero")
        self.__base = valore
    
    @property
    def altezza(self):
        """Getter altezza"""
        return self.__altezza
    
    @altezza.setter
    def altezza(self, valore):
        """Setter altezza con validazione > 0"""
        if valore <= 0:
            raise ValueError("Altezza deve essere maggiore di zero")
        self.__altezza = valore
    
    @property
    def area(self):
        """Calcola area (read-only)"""
        return self.__base * self.__altezza
    
    @property
    def perimetro(self):
        """Calcola perimetro (read-only)"""
        return 2 * (self.__base + self.__altezza)
    
    @property
    def diagonale(self):
        """Calcola lunghezza diagonale (read-only)"""
        return math.sqrt(self.__base ** 2 + self.__altezza ** 2)
    
    @property
    def e_quadrato(self):
        """Verifica se è un quadrato (read-only)"""
        return self.__base == self.__altezza
    
    def scala(self, fattore):
        """
        Scala dimensioni per fattore
        
        Args:
            fattore: moltiplicatore (deve essere > 0)
        """
        if fattore <= 0:
            raise ValueError("Fattore di scala deve essere positivo")
        
        self.__base *= fattore
        self.__altezza *= fattore
    
    def ruota(self):
        """Ruota di 90°: scambia base e altezza"""
        self.__base, self.__altezza = self.__altezza, self.__base
    
    def __str__(self):
        """Rappresentazione stringa"""
        tipo = "Quadrato" if self.e_quadrato else "Rettangolo"
        return f"{tipo}({self.__base} × {self.__altezza})"


# Test
print("=== TEST RETTANGOLO ===\n")

r = Rettangolo(5, 3)
print(f"Rettangolo: {r}")
print(f"Area: {r.area}")
print(f"Perimetro: {r.perimetro}")
print(f"Diagonale: {r.diagonale:.2f}")
print(f"È quadrato? {r.e_quadrato}")

print(f"\nDopo scala(2):")
r.scala(2)
print(f"{r}")
print(f"Area: {r.area}")

print(f"\nDopo ruota():")
r.ruota()
print(f"{r}")
print(f"Base: {r.base}, Altezza: {r.altezza}")

# Test quadrato
print("\n--- Test Quadrato ---")
q = Rettangolo(4, 4)
print(f"{q}")
print(f"È quadrato? {q.e_quadrato}")
print(f"Diagonale: {q.diagonale:.2f}")

# Test validazione
print("\nTest validazione:")
try:
    r_invalido = Rettangolo(-5, 3)
except ValueError as e:
    print(f"✓ Dimensione negativa rifiutata: {e}")

try:
    r.scala(-2)
except ValueError as e:
    print(f"✓ Fattore negativo rifiutato: {e}")