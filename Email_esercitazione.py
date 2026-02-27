class Email:
    """Classe per gestire indirizzi email con validazione"""
    
    def __init__(self, indirizzo):
        """
        Inizializza email con validazione
        
        Args:
            indirizzo: indirizzo email
            
        Raises:
            ValueError: se formato email non valido
        """
        self.indirizzo = indirizzo  # Usa setter per validare
    
    @property
    def indirizzo(self):
        """Getter per indirizzo email"""
        return self.__indirizzo
    
    @indirizzo.setter
    def indirizzo(self, valore):
        """
        Setter con validazione formato email
        
        Args:
            valore: indirizzo email
            
        Raises:
            ValueError: se formato non valido
        """
        # Validazione base
        if '@' not in valore:
            raise ValueError("Email deve contenere '@'")
        
        if '.' not in valore:
            raise ValueError("Email deve contenere '.'")
        
        # Split e validazione parti
        parti = valore.split('@')
        if len(parti) != 2:
            raise ValueError("Email deve avere esattamente un '@'")
        
        username, dominio = parti
        
        if len(username) == 0:
            raise ValueError("Username non può essere vuoto")
        
        if len(dominio) == 0:
            raise ValueError("Dominio non può essere vuoto")
        
        if '.' not in dominio:
            raise ValueError("Dominio deve contenere '.'")
        
        self.__indirizzo = valore
    
    @property
    def username(self):
        """Estrae username (parte prima di @) - read-only"""
        return self.__indirizzo.split('@')[0]
    
    @property
    def dominio(self):
        """Estrae dominio (parte dopo @) - read-only"""
        return self.__indirizzo.split('@')[1]
    
    def cambia_dominio(self, nuovo_dominio):
        """
        Cambia dominio mantenendo username
        
        Args:
            nuovo_dominio: nuovo dominio (deve contenere '.')
            
        Raises:
            ValueError: se dominio non valido
        """
        if '.' not in nuovo_dominio:
            raise ValueError("Dominio deve contenere '.'")
        
        nuovo_indirizzo = f"{self.username}@{nuovo_dominio}"
        self.indirizzo = nuovo_indirizzo  # Usa setter per validare
    
    def __str__(self):
        """Rappresentazione stringa"""
        return self.__indirizzo


# Test
print("=== TEST EMAIL ===\n")

e1 = Email("mario.rossi@gmail.com")
print(f"Indirizzo completo: {e1}")
print(f"Username: {e1.username}")
print(f"Dominio: {e1.dominio}")

print("\nCambio dominio:")
e1.cambia_dominio("outlook.it")
print(f"Nuovo indirizzo: {e1}")

# Test validazione
print("\nTest validazione:")
test_invalidi = [
    "invalid",
    "no-at.com",
    "@nodomain.com",
    "nouser@",
    "double@@domain.com",
    "nodot@domain"
]

for email in test_invalidi:
    try:
        e_test = Email(email)
    except ValueError as e:
        print(f"✓ '{email}' rifiutata: {e}")