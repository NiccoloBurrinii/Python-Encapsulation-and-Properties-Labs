from datetime import datetime

class BankAccountSecure:
    """Conto bancario sicuro con PIN e transazioni protette"""
    
    MAX_TENTATIVI_PIN = 3
    
    def __init__(self, titolare, pin, saldo_iniziale=0):
        """
        Inizializza conto sicuro
        
        Args:
            titolare: nome titolare
            pin: PIN a 4 cifre (string)
            saldo_iniziale: saldo iniziale (default 0)
        """
        self.titolare = titolare
        self.__valida_pin(pin)
        self.__pin = pin
        self.__saldo = saldo_iniziale
        self.__transazioni = []
        self.__tentativi_falliti = 0
        self.__bloccato = False
        
        # Registra apertura conto
        self.__registra_transazione("apertura", saldo_iniziale)
    
    @property
    def saldo(self):
        """Saldo corrente (read-only)"""
        return self.__saldo
    
    @property
    def ultimi_movimenti(self):
        """Restituisce ultimi 5 movimenti (read-only)"""
        return self.__transazioni[-5:]
    
    @property
    def conto_bloccato(self):
        """Verifica se conto è bloccato (read-only)"""
        return self.__bloccato
    
    def cambia_pin(self, vecchio_pin, nuovo_pin):
        """
        Cambia PIN verificando il vecchio
        
        Args:
            vecchio_pin: PIN attuale
            nuovo_pin: nuovo PIN
            
        Returns:
            bool: True se successo
        """
        if not self.__verifica_pin(vecchio_pin):
            print("PIN attuale errato")
            return False
        
        self.__valida_pin(nuovo_pin)
        self.__pin = nuovo_pin
        print("PIN cambiato con successo")
        return True
    
    def deposita(self, importo, pin):
        """
        Deposita denaro con verifica PIN
        
        Args:
            importo: importo da depositare
            pin: PIN per autorizzare
            
        Returns:
            bool: True se successo
        """
        if not self.__verifica_pin(pin):
            return False
        
        if importo <= 0:
            print("Importo deve essere positivo")
            return False
        
        self.__saldo += importo
        self.__registra_transazione("deposito", importo)
        print(f"Depositati €{importo:.2f}. Nuovo saldo: €{self.__saldo:.2f}")
        return True
    
    def preleva(self, importo, pin):
        """
        Preleva denaro con verifica PIN e saldo
        
        Args:
            importo: importo da prelevare
            pin: PIN per autorizzare
            
        Returns:
            bool: True se successo
        """
        if not self.__verifica_pin(pin):
            return False
        
        if importo <= 0:
            print("Importo deve essere positivo")
            return False
        
        if importo > self.__saldo:
            print(f"Saldo insufficiente (disponibili: €{self.__saldo:.2f})")
            return False
        
        self.__saldo -= importo
        self.__registra_transazione("prelievo", -importo)
        print(f"Prelevati €{importo:.2f}. Nuovo saldo: €{self.__saldo:.2f}")
        return True
    
    def __verifica_pin(self, pin):
        """
        Verifica PIN con limite tentativi (metodo privato)
        
        Args:
            pin: PIN da verificare
            
        Returns:
            bool: True se corretto
        """
        if self.__bloccato:
            print("❌ CONTO BLOCCATO per troppi tentativi errati")
            return False
        
        if pin == self.__pin:
            self.__tentativi_falliti = 0  # Reset contatore
            return True
        
        self.__tentativi_falliti += 1
        tentativi_rimasti = self.MAX_TENTATIVI_PIN - self.__tentativi_falliti
        
        if tentativi_rimasti > 0:
            print(f"PIN errato. Tentativi rimasti: {tentativi_rimasti}")
        else:
            self.__bloccato = True
            print("❌ CONTO BLOCCATO per troppi tentativi errati")
            print("   Contattare la banca per sblocco")
        
        return False
    
    def __valida_pin(self, pin):
        """
        Valida formato PIN (metodo privato)
        
        Args:
            pin: PIN da validare
            
        Raises:
            ValueError: se formato non valido
        """
        if not isinstance(pin, str):
            raise ValueError("PIN deve essere una stringa")
        
        if len(pin) != 4:
            raise ValueError("PIN deve essere di 4 cifre")
        
        if not pin.isdigit():
            raise ValueError("PIN deve contenere solo cifre")
    
    def __registra_transazione(self, tipo, importo):
        """
        Registra transazione (metodo privato)
        
        Args:
            tipo: tipo transazione (deposito, prelievo, ecc.)
            importo: importo (positivo o negativo)
        """
        transazione = (
            datetime.now(),
            tipo,
            importo,
            self.__saldo
        )
        self.__transazioni.append(transazione)
    
    def sblocca(self, codice_sblocco):
        """
        Sblocca conto con codice speciale
        
        Args:
            codice_sblocco: codice fornito dalla banca
            
        Returns:
            bool: True se sbloccato
        """
        # In produzione questo sarebbe un codice generato dalla banca
        CODICE_MASTER = "BANK9999"
        
        if codice_sblocco == CODICE_MASTER:
            self.__bloccato = False
            self.__tentativi_falliti = 0
            print("✓ Conto sbloccato")
            return True
        else:
            print("Codice sblocco non valido")
            return False
    
    def storico_completo(self):
        """Stampa storico completo transazioni"""
        if not self.__transazioni:
            print("Nessuna transazione")
            return
        
        print(f"\n{'='*70}")
        print(f"STORICO TRANSAZIONI - {self.titolare}".center(70))
        print('='*70)
        print(f"{'Data/Ora':<20} {'Tipo':<15} {'Importo':>15} {'Saldo':>15}")
        print('-'*70)
        
        for data, tipo, importo, saldo in self.__transazioni:
            data_str = data.strftime("%Y-%m-%d %H:%M:%S")
            segno = "+" if importo >= 0 else ""
            print(f"{data_str:<20} {tipo:<15} {segno}{importo:>14.2f} {saldo:>14.2f}")
        
        print('='*70)


# Test completo
print("=== TEST BANK ACCOUNT SECURE ===\n")

conto = BankAccountSecure("Mario Rossi", "1234", 1000)
print(f"Saldo iniziale: €{conto.saldo}\n")

# Operazioni normali
conto.deposita(500, "1234")
conto.preleva(200, "1234")

# Test PIN errato
print("\nTest PIN errati:")
conto.preleva(100, "0000")
conto.preleva(100, "9999")
conto.preleva(100, "5555")  # Terzo tentativo - blocca

# Prova operazione con conto bloccato
print("\nProva dopo blocco:")
conto.deposita(100, "1234")  # Rifiutato anche con PIN corretto

# Sblocco
print("\nSblocco:")
conto.sblocca("BANK9999")
conto.deposita(100, "1234")  # Ora funziona

# Storico
print("\nUltimi movimenti:")
for mov in conto.ultimi_movimenti:
    data, tipo, importo, saldo = mov
    print(f"  {tipo}: €{importo:.2f} → €{saldo:.2f}")

# Cambio PIN
print("\nCambio PIN:")
conto.cambia_pin("1234", "5678")
conto.deposita(50, "5678")  # Nuovo PIN funziona

# Storico completo
conto.storico_completo()
