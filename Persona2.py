class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
   
    @property
    def nome_completo(self):
        """Property read-only computed"""
        return f"{self.nome} {self.cognome}"

p = Persona("Mario", "Rossi")
print(p.nome_completo)  # Mario Rossi

p.nome = "Luigi"
print(p.nome_completo)  # Luigi Rossi (aggiornato)

p.nome_completo = "X"  # AttributeError!