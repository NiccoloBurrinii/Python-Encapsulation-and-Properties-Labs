class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio  # Usa setter
   
    @property
    def raggio(self):
        return self.__raggio
   
    @raggio.setter
    def raggio(self, valore):
        if valore <= 0:
            raise ValueError("Raggio deve essere positivo")
        self.__raggio = valore
   
    @property
    def area(self):
        import math
        return math.pi * self.__raggio ** 2
   
    @property
    def circonferenza(self):
        import math
        return 2 * math.pi * self.__raggio

c = Cerchio(5)
print(f"Area: {c.area:.2f}")
print(f"Circonferenza: {c.circonferenza:.2f}")

c.raggio = 10  # Validato automaticamente
print(f"Nuova area: {c.area:.2f}")