import hashlib

class Password:
    """Classe per gestire password con hashing e validazione"""
    
    def __init__(self, password_in_chiaro):
        """
        Inizializza con password in chiaro
        
        Args:
            password_in_chiaro: password iniziale
            
        Raises:
            ValueError: se password non soddisfa requisiti
        """
        self.password = password_in_chiaro  # Usa setter
    
    @property
    def password(self):
        """
        NO getter per password (sicurezza)
        
        Raises:
            AttributeError: sempre (password non recuperabile)
        """
        raise AttributeError("Password non può essere letta (solo write-only)")
    
    @password.setter
    def password(self, nuova_password):
        """
        Setter per password con validazione e hashing
        
        Args:
            nuova_password: nuova password in chiaro
            
        Raises:
            ValueError: se password non valida
        """
        self.__valida_complessita(nuova_password)
        self.__hash_password = self.__genera_hash(nuova_password)
    
    def verifica(self, password_da_testare):
        """
        Verifica se password corrisponde a quella salvata
        
        Args:
            password_da_testare: password da verificare
            
        Returns:
            bool: True se corretta, False altrimenti
        """
        hash_test = self.__genera_hash(password_da_testare)
        return hash_test == self.__hash_password
    
    def __valida_complessita(self, password):
        """
        Valida complessità password (metodo privato)
        
        Args:
            password: password da validare
            
        Raises:
            ValueError: se non soddisfa requisiti
        """
        errori = []
        
        if len(password) < 8:
            errori.append("almeno 8 caratteri")
        
        if not any(c.isupper() for c in password):
            errori.append("almeno una maiuscola")
        
        if not any(c.islower() for c in password):
            errori.append("almeno una minuscola")
        
        if not any(c.isdigit() for c in password):
            errori.append("almeno un numero")
        
        if errori:
            raise ValueError(
                f"Password deve contenere: {', '.join(errori)}"
            )
    
    def __genera_hash(self, password):
        """
        Genera hash SHA-256 di una password (metodo privato)
        
        Args:
            password: password in chiaro
            
        Returns:
            str: hash esadecimale
        """
        return hashlib.sha256(password.encode()).hexdigest()


# Test
print("=== TEST PASSWORD ===\n")

p = Password("MyP@ss123")
print("Password creata")

print(f"Verifica 'MyP@ss123': {p.verifica('MyP@ss123')}")
print(f"Verifica 'wrong': {p.verifica('wrong')}")

print("\nCambio password:")
p.password = "NewP@ss456"
print(f"Verifica vecchia: {p.verifica('MyP@ss123')}")
print(f"Verifica nuova: {p.verifica('NewP@ss456')}")

# Test validazione
print("\nTest validazione:")
test_invalidi = [
    ("weak", "troppo corta"),
    ("nouppercase1", "senza maiuscole"),
    ("NOLOWERCASE1", "senza minuscole"),
    ("NoDigitsHere", "senza numeri")
]

for pwd, motivo in test_invalidi:
    try:
        p_test = Password(pwd)
    except ValueError as e:
        print(f"✓ '{pwd}' rifiutata ({motivo}): {e}")

# Test no-getter
print("\nTest accesso diretto:")
try:
    print(p.password)
except AttributeError as e:
    print(f"✓ Accesso negato: {e}")