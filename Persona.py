class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.set_eta(eta)  # Usa setter per validare
   
    def get_nome(self):
        return self.__nome
   
    def get_eta(self):
        return self.__eta
   
    def set_eta(self, eta):
        if eta < 0 or eta > 150:
            raise ValueError("Età non valida")
        self.__eta = eta

p = Persona("Mario", 25)
print(p.get_eta())  # 25

p.set_eta(30)       # OK
p.set_eta(-5)     # ValueError!
p.set_eta(200)    # ValueError!