import re

from Email_esercitazione import Email

class EmailAvanzata(Email):
    """Email con validazione regex più robusta"""
    
    # Pattern RFC 5322 semplificato
    EMAIL_PATTERN = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    
    @property
    def indirizzo(self):
        return self._Email__indirizzo
    
    @indirizzo.setter
    def indirizzo(self, valore):
        if not self.EMAIL_PATTERN.match(valore):
            raise ValueError(
                f"Email '{valore}' non rispetta il formato valido"
            )
        self._Email__indirizzo = valore
    
    @property
    def dominio_principale(self):
        """Estrae dominio principale (senza subdomini)"""
        parti_dominio = self.dominio.split('.')
        if len(parti_dominio) >= 2:
            return '.'.join(parti_dominio[-2:])
        return self.dominio
    
    def e_provider(self, provider):
        """Verifica se l'email è di un provider specifico"""
        return provider.lower() in self.dominio.lower()


# Test avanzato
e2 = EmailAvanzata("test.user@mail.google.com")
print(f"\nDominio principale: {e2.dominio_principale}")
print(f"È Gmail? {e2.e_provider('gmail') or e2.e_provider('google')}")