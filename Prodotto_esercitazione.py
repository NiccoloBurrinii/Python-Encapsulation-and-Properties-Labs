class Prodotto:
    """Classe per prodotto e-commerce con prezzo e sconto"""
    
    def __init__(self, nome, prezzo, sconto=0):
        """
        Inizializza prodotto
        
        Args:
            nome: nome prodotto
            prezzo: prezzo base (validato > 0)
            sconto: percentuale sconto 0-100 (default 0)
        """
        self.nome = nome
        self.prezzo = prezzo  # Usa setter per validare
        self.sconto = sconto  # Usa setter per validare
    
    @property
    def prezzo(self):
        """Getter prezzo base"""
        return self.__prezzo
    
    @prezzo.setter
    def prezzo(self, valore):
        """Setter prezzo con validazione"""
        if valore <= 0:
            raise ValueError("Prezzo deve essere maggiore di zero")
        self.__prezzo = valore
    
    @property
    def sconto(self):
        """Getter percentuale sconto"""
        return self.__sconto
    
    @sconto.setter
    def sconto(self, valore):
        """Setter sconto con validazione range"""
        if not 0 <= valore <= 100:
            raise ValueError("Sconto deve essere tra 0 e 100%")
        self.__sconto = valore
    
    @property
    def prezzo_scontato(self):
        """Calcola prezzo finale scontato (read-only)"""
        return round(self.__prezzo * (1 - self.__sconto / 100), 2)
    
    @property
    def risparmio(self):
        """Calcola risparmio rispetto a prezzo pieno (read-only)"""
        return round(self.__prezzo - self.prezzo_scontato, 2)
    
    def applica_sconto_stagionale(self, percentuale_extra):
        """
        Aggiunge sconto extra mantenendo max 100%
        
        Args:
            percentuale_extra: sconto aggiuntivo da sommare
        """
        nuovo_sconto = self.__sconto + percentuale_extra
        # Limita a 100%
        self.sconto = min(nuovo_sconto, 100)
    
    def __str__(self):
        """Rappresentazione stringa"""
        if self.__sconto > 0:
            return (f"{self.nome}: €{self.__prezzo:.2f} "
                   f"(-{self.__sconto}%) = €{self.prezzo_scontato:.2f}")
        return f"{self.nome}: €{self.__prezzo:.2f}"


# Test
print("=== TEST PRODOTTO ===\n")

p = Prodotto("Laptop", 1000, 10)
print(f"Prezzo base: €{p.prezzo}")
print(f"Sconto: {p.sconto}%")
print(f"Prezzo scontato: €{p.prezzo_scontato}")
print(f"Risparmio: €{p.risparmio}")

print(f"\nApplico sconto stagionale +5%:")
p.applica_sconto_stagionale(5)
print(f"Nuovo sconto: {p.sconto}%")
print(f"Nuovo prezzo: €{p.prezzo_scontato}")

# Test prodotto senza sconto
p2 = Prodotto("Mouse", 25)
print(f"\n{p2}")

# Test validazione
print("\nTest validazione:")
try:
    p3 = Prodotto("Test", -100)
except ValueError as e:
    print(f"✓ Prezzo negativo rifiutato: {e}")

try:
    p.sconto = 150
except ValueError as e:
    print(f"✓ Sconto > 100% rifiutato: {e}")
