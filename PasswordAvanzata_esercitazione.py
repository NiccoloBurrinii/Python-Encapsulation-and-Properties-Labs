import hashlib
import secrets
from datetime import datetime


class PasswordAvanzata:
    """Password con salt e storia cambi"""
    
    MAX_STORIA = 5  # Ultime 5 password
    
    def __init__(self, password_in_chiaro):
        self.__storia_hash = []  # Lista hash password precedenti
        self.password = password_in_chiaro
    
    @property
    def password(self):
        raise AttributeError("Password non può essere letta")
    
    @password.setter
    def password(self, nuova_password):
        self.__valida_complessita(nuova_password)
        
        # Genera salt univoco
        salt = secrets.token_hex(16)
        hash_con_salt = self.__genera_hash_con_salt(nuova_password, salt)
        
        # Check non sia una delle ultime N password
        for vecchio_hash, vecchio_salt, _ in self.__storia_hash:
            if self.__genera_hash_con_salt(nuova_password, vecchio_salt) == vecchio_hash:
                raise ValueError("Non puoi riusare una password recente")
        
        # Salva in storia
        self.__storia_hash.append(
            (hash_con_salt, salt, datetime.now())
        )
        
        # Mantieni solo ultime MAX_STORIA
        if len(self.__storia_hash) > self.MAX_STORIA:
            self.__storia_hash.pop(0)
        
        self.__hash_corrente = hash_con_salt
        self.__salt_corrente = salt
    
    def verifica(self, password_da_testare):
        hash_test = self.__genera_hash_con_salt(
            password_da_testare, 
            self.__salt_corrente
        )
        return hash_test == self.__hash_corrente
    
    def __valida_complessita(self, password):
        """Validazione come prima"""
        if len(password) < 8:
            raise ValueError("Password troppo corta")
        if not any(c.isupper() for c in password):
            raise ValueError("Serve almeno una maiuscola")
        if not any(c.islower() for c in password):
            raise ValueError("Serve almeno una minuscola")
        if not any(c.isdigit() for c in password):
            raise ValueError("Serve almeno un numero")
    
    def __genera_hash_con_salt(self, password, salt):
        """Genera hash con salt"""
        salted = (password + salt).encode()
        return hashlib.sha256(salted).hexdigest()
    
    @property
    def numero_cambi(self):
        """Numero di volte che password è stata cambiata"""
        return len(self.__storia_hash)
    
    @property
    def data_ultimo_cambio(self):
        """Data ultimo cambio password"""
        if self.__storia_hash:
            return self.__storia_hash[-1][2]
        return None


# Test avanzato
p2 = PasswordAvanzata("First123")
print(f"Cambi password: {p2.numero_cambi}")

p2.password = "Second456"
p2.password = "Third789"

try:
    p2.password = "First123"  # Riuso password
except ValueError as e:
    print(f"✓ Riuso bloccato: {e}")

print(f"Ultimo cambio: {p2.data_ultimo_cambio}")