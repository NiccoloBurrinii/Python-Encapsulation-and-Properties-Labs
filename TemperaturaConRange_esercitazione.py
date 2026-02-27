from Temperatura  import Temperatura

class TemperaturaConRange(Temperatura):
    """Temperatura con range min/max configurabili"""
    
    def __init__(self, celsius=0, min_temp=-273.15, max_temp=1000):
        self.min_temp = min_temp
        self.max_temp = max_temp
        super().__init__(celsius)
    
    @property
    def celsius(self):
        return self._Temperatura__celsius
    
    @celsius.setter
    def celsius(self, valore):
        if valore < self.min_temp:
            raise ValueError(f"Temperatura sotto il minimo ({self.min_temp}°C)")
        if valore > self.max_temp:
            raise ValueError(f"Temperatura sopra il massimo ({self.max_temp}°C)")
        self._Temperatura__celsius = valore


# Test range
t2 = TemperaturaConRange(25, min_temp=0, max_temp=100)
try:
    t2.celsius = 150
except ValueError as e:
    print(f"Validazione range: {e}")