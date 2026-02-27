class Temperatura:
    """Classe per gestire temperature con conversioni automatiche"""
    
    ZERO_ASSOLUTO = -273.15  # Costante di classe
    
    def __init__(self, celsius=0):
        """
        Inizializza temperatura
        
        Args:
            celsius: temperatura in gradi Celsius
        """
        self.celsius = celsius  # Usa setter per validazione
    
    @property
    def celsius(self):
        """Getter per temperatura in Celsius"""
        return self.__celsius
    
    @celsius.setter
    def celsius(self, valore):
        """
        Setter per Celsius con validazione
        
        Args:
            valore: temperatura in Celsius
            
        Raises:
            ValueError: se temperatura sotto zero assoluto
        """
        if valore < self.ZERO_ASSOLUTO:
            raise ValueError(
                f"Temperatura non può essere inferiore a "
                f"{self.ZERO_ASSOLUTO}°C (zero assoluto)"
            )
        self.__celsius = valore
    
    @property
    def fahrenheit(self):
        """Calcola temperatura in Fahrenheit"""
        return self.__celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valore):
        """Imposta temperatura da Fahrenheit"""
        # Converte in Celsius e usa setter celsius (con validazione)
        self.celsius = (valore - 32) * 5/9
    
    @property
    def kelvin(self):
        """Calcola temperatura in Kelvin"""
        return self.__celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, valore):
        """Imposta temperatura da Kelvin"""
        # Converte in Celsius e usa setter celsius (con validazione)
        self.celsius = valore - 273.15
    
    def info(self):
        """Stampa temperatura in tutte le scale"""
        print(f"{self.celsius:.2f}°C = {self.fahrenheit:.2f}°F = {self.kelvin:.2f}K")


# Test
print("=== TEST TEMPERATURA ===\n")

t = Temperatura(25)
t.info()

print(f"\nImpostazione Fahrenheit a 100°F:")
t.fahrenheit = 100
print(f"Celsius: {t.celsius:.2f}")

print(f"\nImpostazione Kelvin a 300K:")
t.kelvin = 300
print(f"Celsius: {t.celsius:.2f}")

# Test validazione
print("\nTest validazione:")
try:
    t.celsius = -300
except ValueError as e:
    print(f"✓ Errore catturato: {e}")

# Test casi limite
print("\nZero assoluto:")
t.celsius = -273.15
t.info()