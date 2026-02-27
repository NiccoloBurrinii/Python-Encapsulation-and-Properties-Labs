from datetime import datetime, timedelta

from Prodotto_esercitazione import Prodotto

class ProdottoAvanzato(Prodotto):
    """Prodotto con sconti multipli e validità"""
    
    CATEGORIE_VALIDE = ["Elettronica", "Abbigliamento", "Casa", "Sport"]
    
    def __init__(self, nome, prezzo, categoria, sconto=0):
        if categoria not in self.CATEGORIE_VALIDE:
            raise ValueError(f"Categoria deve essere una tra: {self.CATEGORIE_VALIDE}")
        
        self.categoria = categoria
        self.__sconti_attivi = []  # Lista (descrizione, %, scadenza)
        super().__init__(nome, prezzo, sconto)
    
    def aggiungi_sconto_temporaneo(self, descrizione, percentuale, giorni_validita=7):
        """Aggiunge sconto con scadenza"""
        scadenza = datetime.now() + timedelta(days=giorni_validita)
        self.__sconti_attivi.append((descrizione, percentuale, scadenza))
        self.__aggiorna_sconto_totale()
    
    def __aggiorna_sconto_totale(self):
        """Ricalcola sconto totale da sconti attivi"""
        # Rimuovi sconti scaduti
        ora = datetime.now()
        self.__sconti_attivi = [
            s for s in self.__sconti_attivi if s[2] > ora
        ]
        
        # Somma percentuali
        totale = sum(s[1] for s in self.__sconti_attivi)
        self.sconto = min(totale, 100)
    
    def mostra_sconti_attivi(self):
        """Visualizza dettaglio sconti"""
        if not self.__sconti_attivi:
            print("Nessuno sconto attivo")
            return
        
        print(f"Sconti attivi su {self.nome}:")
        for desc, perc, scad in self.__sconti_attivi:
            giorni_rimasti = (scad - datetime.now()).days
            print(f"  • {desc}: -{perc}% (scade tra {giorni_rimasti} giorni)")


# Test avanzato
p_adv = ProdottoAvanzato("Smart TV", 500, "Elettronica")
p_adv.aggiungi_sconto_temporaneo("Black Friday", 20, 3)
p_adv.aggiungi_sconto_temporaneo("Coupon VIP", 10, 7)
p_adv.mostra_sconti_attivi()
print(f"Prezzo finale: €{p_adv.prezzo_scontato}")
