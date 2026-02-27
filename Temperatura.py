class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, valore):
        if valore < -273.15:
            raise ValueError("Temperatura sotto zero assoluto")
        self.__celsius = valore
    
    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valore):
        self.celsius = (valore - 32) * 5/9
    
    @property
    def kelvin(self):
        return self.__celsius + 273.15

t = Temperatura(25)
print(f"C: {t.celsius}, F: {t.fahrenheit:.1f}, K: {t.kelvin:.1f}")

t.fahrenheit = 100  # Imposta tramite Fahrenheit
print(f"C: {t.celsius:.1f}")  # Aggiornato!
