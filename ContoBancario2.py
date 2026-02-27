class ContoBancario:
    def __init__(self, titolare, saldo=0):
        self.titolare = titolare
        self.__saldo = saldo
   
    def __valida_importo(self, importo):
        """Metodo privato per validazione"""
        if importo <= 0:
            raise ValueError("Importo deve essere positivo")
   
    def deposita(self, importo):
        self.__valida_importo(importo)
        self.__saldo += importo
   
    def preleva(self, importo):
        self.__valida_importo(importo)
        if importo > self.__saldo:
            raise ValueError("Saldo insufficiente")
        self.__saldo -= importo

c = ContoBancario("Mario", 1000)
c.deposita(500)  # Usa __valida_importo internamente
c.__valida_importo(100)  # AttributeError!