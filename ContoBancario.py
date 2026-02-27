class ContoBancario:
    def __init__(self, titolare, saldo):
        self.titolare = titolare      # Pubblico
        self._numero_conto = "12345"  # Protected con _
        self.__pin = "1234"           # Private con _ _
   
    def info(self):
        print(f"Titolare: {self.titolare}")
        print(f"Numero: {self._numero_conto}")
        # PIN non mostrato

c = ContoBancario("Mario", 1000)
print(c.titolare)       # OK
print(c._numero_conto)  # Funziona ma sconsigliato
# print(c.__pin)        # AttributeError!

# Name mangling permette accesso (ma non farlo!)
print(c._ContoBancario__pin)  # "1234"