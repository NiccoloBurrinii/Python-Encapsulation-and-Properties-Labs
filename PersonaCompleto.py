class Persona:
    def __init__(self, nome, eta):
        self._nome = nome
        self.eta = eta  # Usa setter
   
    @property
    def nome(self):
        return self._nome
   
    @property
    def eta(self):
        return self._eta
   
    @eta.setter
    def eta(self, valore):
        if not 0 <= valore <= 150:
            raise ValueError("Età non valida")
        self._eta = valore

p = Persona("Mario", 25)
print(p.nome)  # Mario
print(p.eta)   # 25

p.eta = 30     # OK
p.eta = 200  # ValueError!