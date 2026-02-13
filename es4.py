class Dipendente():
    def __init__ (self, nome, codice, stipendio):
        self.nome = nome
        self.codice = codice
        self.__stipendio = stipendio

    @property 
    def get_stipendio(self):
        return self.__stipendio
    
    @get_stipendio.setter
    def set_stipendio(self, nuovo_stipendio):
        if nuovo_stipendio >= 0:
            self.__stipendio = nuovo_stipendio
        else:
            print("Lo stipendio non può essere negativo.")

    def calcola_stipendio(self):
        return self.get_stipendio()
    
    def info(self):
        print(f"Nome: {self.nome}, Codice: {self.codice}, Stipendio: {self.get_stipendio()}")

class Manager(Dipendente):
    def __init__(self, nome, codice, stipendio, bonus):
        super().__init__(nome, codice, stipendio)
        self.bonus = bonus

    def calcola_stipendio(self):
        return self.get_stipendio() + self.bonus
    
    def info(self):
        print(f"Nome: {self.nome}, Codice: {self.codice}, Stipendio: {self.get_stipendio()}, Bonus: {self.bonus}, Stipendio Totale: {self.calcola_stipendio()}")

class Sviluppatore(Dipendente):
    def __init__ (self, nome, codice, stipendio, linguaggi):
        super().__init__(nome, codice, stipendio)
        self.linguaggi = linguaggi

    def aggiungi_linguaggio(self, linguaggio):
        if linguaggio not in self.linguaggi:
            self.linguaggi.append(linguaggio)
        else:
            print(f"{linguaggio} è già presente nella lista dei linguaggi.")

    def calcola_stipendio(self):
        return super().calcola_stipendio()+ (100*len(self.linguaggi))
    
    def info(self):
        print(f"Nome: {self.nome}, Codice: {self.codice}, Stipendio: {self.get_stipendio()}, Linguaggi: {', '.join(self.linguaggi)}, Stipendio Totale: {self.calcola_stipendio()}")

class Stagista(Dipendente):
    def __init__ (self, nome, codice, ore_mensili, tariffa_oraria):
        super().__init__(nome, codice, 0)
        self.ore_mensili = ore_mensili
        self.tariffa_oraria = tariffa_oraria

    def calcola_stipendio(self):
        return self.ore_mensili * self.tariffa_oraria
    
    def info(self):
        print(f"Nome: {self.nome}, Codice: {self.codice}, Ore Mensili: {self.ore_mensili}, Tariffa Oraria: {self.tariffa_oraria}, Stipendio Totale: {self.calcola_stipendio()}")

# Esempio di utilizzo
dipendenti = [
    Manager("Alice", "M001", 3000, 500),
    Sviluppatore("Bob", "S001", 2500, ["Python", "Java"]),
    Stagista("Carlo", "ST001", 80, 15)
]

totale_stipendi = sum(d.calcola_stipendio() for d in dipendenti)

for d in dipendenti:
    print(f"{d.nome}: €{d.calcola_stipendio()}")

print(f"\nTotale stipendi: €{totale_stipendi}")