# LEZIONE 28 - ESERCITAZIONI
## Incapsulamento e Proprietà

**Modalità:** Individuale | **Durata:** 2 ore (60 min guidate + 60 min autonome)

---

## 📋 ESERCITAZIONI GUIDATE (60 minuti)

### Esercizio 1 - Classe Temperatura (20 minuti)

#### Descrizione
Creare una classe `Temperatura` che gestisce temperature con conversione automatica tra Celsius, Fahrenheit e Kelvin usando properties.

#### Requisiti

**Classe Temperatura:**
- `__init__(self, celsius=0)`
  - Inizializza temperatura in Celsius
  - Usa setter per validazione

- `@property celsius` (getter e setter)
  - Getter: restituisce temperatura in Celsius
  - Setter: valida che temperatura >= -273.15 (zero assoluto)
  - Attributo privato: `__celsius`

- `@property fahrenheit` (getter e setter)
  - Getter: converte e restituisce in Fahrenheit
  - Formula: F = C × 9/5 + 32
  - Setter: converte da Fahrenheit a Celsius

- `@property kelvin` (getter e setter)
  - Getter: converte e restituisce in Kelvin
  - Formula: K = C + 273.15
  - Setter: converte da Kelvin a Celsius

- `info(self)`
  - Stampa temperatura in tutte e tre le scale

#### Esempio di Utilizzo
```python
t = Temperatura(25)
t.info()  # 25.00°C = 77.00°F = 298.15K

t.fahrenheit = 100
print(f"Celsius: {t.celsius:.2f}")  # 37.78

t.kelvin = 300
print(f"Celsius: {t.celsius:.2f}")  # 26.85

# t.celsius = -300  # ValueError!
```

#### Output Atteso
```
25.00°C = 77.00°F = 298.15K
Celsius: 37.78
Celsius: 26.85
```

#### Hint
- Usa `self.__celsius` come storage interno
- Setter celsius valida: `if valore < -273.15: raise ValueError(...)`
- Conversioni:
  - F = C × 9/5 + 32
  - C = (F - 32) × 5/9
  - K = C + 273.15
  - C = K - 273.15

---

### Esercizio 2 - Classe Email (20 minuti)

#### Descrizione
Creare una classe `Email` che valida e gestisce indirizzi email con properties.

#### Requisiti

**Classe Email:**
- `__init__(self, indirizzo)`
  - Inizializza con indirizzo email validato

- `@property indirizzo` (getter e setter)
  - Getter: restituisce indirizzo
  - Setter: valida formato email
  - Validazione: deve contenere '@' e '.'
  - Deve avere caratteri prima e dopo '@'

- `@property username` (read-only)
  - Restituisce parte prima di '@'

- `@property dominio` (read-only)
  - Restituisce parte dopo '@'

- `cambia_dominio(self, nuovo_dominio)`
  - Cambia dominio mantenendo username
  - Valida che nuovo_dominio contenga '.'

#### Esempio di Utilizzo
```python
e1 = Email("mario.rossi@gmail.com")
print(f"Username: {e1.username}")   # mario.rossi
print(f"Dominio: {e1.dominio}")     # gmail.com

e1.cambia_dominio("outlook.it")
print(e1.indirizzo)  # mario.rossi@outlook.it

# e2 = Email("invalid")  # ValueError
# e1.indirizzo = "bad"   # ValueError
```

#### Output Atteso
```
Username: mario.rossi
Dominio: gmail.com
mario.rossi@outlook.it
```

#### Hint
- Validazione base: `'@' in email and '.' in email`
- Split: `username, dominio = email.split('@')`
- Validazione robusta: check lunghezza parti
- Properties read-only: solo `@property`, nessun setter

---

### Esercizio 3 - Classe Password (20 minuti)

#### Descrizione
Creare una classe `Password` che gestisce password con hashing e validazione complessità.

#### Requisiti

**Classe Password:**
- `__init__(self, password_in_chiaro)`
  - Valida complessità
  - Salva hash (non password in chiaro)

- `@property password` (solo setter, no getter!)
  - Setter: valida e genera nuovo hash
  - NO getter (password non recuperabile)

- `verifica(self, password_da_testare)`
  - Confronta hash di password_da_testare con hash salvato
  - Restituisce True/False

- `__valida_complessita(self, password)` (metodo privato)
  - Lunghezza >= 8 caratteri
  - Almeno una maiuscola
  - Almeno una minuscola
  - Almeno un numero
  - Restituisce True se valida, altrimenti raise ValueError

- `__genera_hash(self, password)` (metodo privato)
  - Usa hashlib.sha256 per hash
  - Restituisce hash esadecimale

#### Esempio di Utilizzo
```python
p = Password("MyP@ss123")
print(p.verifica("MyP@ss123"))  # True
print(p.verifica("wrong"))      # False

p.password = "NewP@ss456"  # Cambia password
print(p.verifica("MyP@ss123"))  # False
print(p.verifica("NewP@ss456")) # True

# p2 = Password("weak")  # ValueError: troppo corta
# p2 = Password("nodigits")  # ValueError: manca numero
```

#### Output Atteso
```
True
False
False
True
```

#### Hint Hash
```python
import hashlib

def genera_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

#### Hint Validazione
- Lunghezza: `len(password) >= 8`
- Maiuscole: `any(c.isupper() for c in password)`
- Minuscole: `any(c.islower() for c in password)`
- Numeri: `any(c.isdigit() for c in password)`

---

## 🎯 ESERCITAZIONI AUTONOME (60 minuti)

### Esercizio 4 - Classe Prodotto (20 minuti)

#### Descrizione
Creare una classe `Prodotto` per e-commerce con prezzo, sconto e calcolo automatico prezzo scontato.

#### Requisiti

**Classe Prodotto:**
- `__init__(self, nome, prezzo, sconto=0)`
  - nome, prezzo (validato > 0), sconto percentuale (0-100)

- `@property prezzo` (getter e setter)
  - Getter: restituisce prezzo base
  - Setter: valida che prezzo > 0

- `@property sconto` (getter e setter)
  - Getter: restituisce percentuale sconto
  - Setter: valida 0 <= sconto <= 100

- `@property prezzo_scontato` (read-only computed)
  - Calcola: prezzo × (1 - sconto/100)
  - Arrotonda a 2 decimali

- `@property risparmio` (read-only computed)
  - Calcola: prezzo - prezzo_scontato

- `applica_sconto_stagionale(self, percentuale_extra)`
  - Aumenta sconto attuale di percentuale_extra
  - Max 100% totale

#### Test
```python
p = Prodotto("Laptop", 1000, 10)
print(f"Prezzo: €{p.prezzo}")
print(f"Sconto: {p.sconto}%")
print(f"Prezzo scontato: €{p.prezzo_scontato}")
print(f"Risparmio: €{p.risparmio}")

p.applica_sconto_stagionale(5)  # +5% extra
print(f"Nuovo prezzo: €{p.prezzo_scontato}")
```

#### Output Atteso
```
Prezzo: €1000
Sconto: 10%
Prezzo scontato: €900.0
Risparmio: €100.0
Nuovo prezzo: €850.0
```

---

### Esercizio 5 - Classe Rettangolo (20 minuti)

#### Descrizione
Creare classe `Rettangolo` con validazione dimensioni e properties per area, perimetro e diagonale.

#### Requisiti

**Classe Rettangolo:**
- `__init__(self, base, altezza)`
  - Inizializza dimensioni (validate > 0)

- `@property base` e `@property altezza` (getter e setter)
  - Getter: restituiscono dimensioni
  - Setter: validano valore > 0

- `@property area` (read-only)
  - Calcola: base × altezza

- `@property perimetro` (read-only)
  - Calcola: 2 × (base + altezza)

- `@property diagonale` (read-only)
  - Calcola: √(base² + altezza²)
  - Usa math.sqrt()

- `@property e_quadrato` (read-only)
  - Restituisce True se base == altezza

- `scala(self, fattore)`
  - Moltiplica base e altezza per fattore
  - Valida fattore > 0

- `ruota(self)`
  - Scambia base e altezza

#### Test
```python
r = Rettangolo(5, 3)
print(f"Area: {r.area}")
print(f"Perimetro: {r.perimetro}")
print(f"Diagonale: {r.diagonale:.2f}")
print(f"È quadrato? {r.e_quadrato}")

r.scala(2)
print(f"Dopo scala(2) - Area: {r.area}")

r.ruota()
print(f"Dopo ruota - Base: {r.base}, Altezza: {r.altezza}")
```

#### Output Atteso
```
Area: 15
Perimetro: 16
Diagonale: 5.83
È quadrato? False
Dopo scala(2) - Area: 60
Dopo ruota - Base: 6, Altezza: 10
```

---

### Esercizio 6 - Challenge: BankAccountSecure (20 minuti)

#### Descrizione
Creare classe `BankAccountSecure` con PIN, transazioni protette e properties avanzate.

#### Requisiti

**Classe BankAccountSecure:**
- `__init__(self, titolare, pin, saldo_iniziale=0)`
  - Valida PIN (4 cifre)
  - Inizializza saldo (privato)
  - Lista transazioni vuota

- `@property saldo` (read-only)
  - Restituisce saldo corrente

- `@property ultimi_movimenti` (read-only)
  - Restituisce ultimi 5 movimenti

- `cambia_pin(self, vecchio_pin, nuovo_pin)`
  - Verifica vecchio PIN
  - Valida nuovo PIN (4 cifre)
  - Cambia PIN

- `deposita(self, importo, pin)`
  - Verifica PIN
  - Valida importo > 0
  - Aggiunge a saldo
  - Registra transazione

- `preleva(self, importo, pin)`
  - Verifica PIN
  - Verifica saldo sufficiente
  - Sottrae da saldo
  - Registra transazione

- `__verifica_pin(self, pin)` (privato)
  - Restituisce True se PIN corretto

- `__valida_pin(self, pin)` (privato)
  - Valida formato PIN (4 cifre)

- `__registra_transazione(self, tipo, importo)` (privato)
  - Aggiunge a lista transazioni
  - Formato: (timestamp, tipo, importo, saldo_dopo)

#### Test
```python
from datetime import datetime

conto = BankAccountSecure("Mario Rossi", "1234", 1000)
print(f"Saldo: €{conto.saldo}")

conto.deposita(500, "1234")
conto.preleva(200, "1234")
# conto.preleva(100, "0000")  # PIN errato

print(f"Saldo: €{conto.saldo}")

print("\nUltimi movimenti:")
for mov in conto.ultimi_movimenti:
    print(f"  {mov[1]}: €{mov[2]} → €{mov[3]}")

conto.cambia_pin("1234", "5678")
conto.deposita(100, "5678")  # Nuovo PIN
```

#### Output Atteso
```
Saldo: €1000
Saldo: €1300

Ultimi movimenti:
  deposito: €500 → €1500
  prelievo: €200 → €1300
```

#### Sfida Extra
- Aggiungere limite tentativi PIN (3 tentativi poi blocco)
- Aggiungere property `conto_bloccato` (read-only)
- Metodo `sblocca(self, codice_sblocco)` con codice speciale

---

## 📝 NOTE PER LO STUDENTE

### Concetti Chiave

1. **Attributi Privati**
   - `__attributo`: doppio underscore per privatizzare
   - Name mangling: Python rinomina in `_Classe__attributo`

2. **Properties**
   - `@property`: getter (accesso lettura)
   - `@attributo.setter`: setter (accesso scrittura)
   - Sintassi: `obj.attributo` invece di `obj.get_attributo()`

3. **Validazione**
   - Sempre nel setter
   - Usa setter anche in `__init__`
   - Raise ValueError con messaggio chiaro

4. **Read-Only Properties**
   - Solo `@property`, nessun setter
   - Per valori calcolati o immutabili

### Pattern Comune
```python
class Esempio:
    def __init__(self, valore):
        self.valore = valore  # Usa setter
    
    @property
    def valore(self):
        return self.__valore
    
    @valore.setter
    def valore(self, val):
        if val < 0:
            raise ValueError("Deve essere >= 0")
        self.__valore = val
```

### Errori da Evitare

1. **Ciclo infinito**
   ```python
   # SBAGLIATO
   @property
   def x(self):
       return self.x  # Chiama se stesso all'infinito!
   
   # CORRETTO
   @property
   def x(self):
       return self.__x  # Usa attributo privato
   ```

2. **Setter senza getter**
   ```python
   # SBAGLIATO
   @x.setter
   def x(self, val):  # Errore: @property deve venire prima
       self.__x = val
   ```

3. **Non validare in __init__**
   ```python
   # SBAGLIATO
   def __init__(self, x):
       self.__x = x  # Bypassa validazione!
   
   # CORRETTO
   def __init__(self, x):
       self.x = x  # Usa setter che valida
   ```

---

## ✅ CHECKLIST COMPLETAMENTO

- [ ] Attributi privati con __nome
- [ ] Properties con @property decorator
- [ ] Validazione in tutti i setter
- [ ] Read-only properties per valori calcolati
- [ ] Metodi privati con __ per helper
- [ ] Docstring per getter
- [ ] Test con valori validi e invalidi
- [ ] Gestione eccezioni con messaggi chiari

---

**Buon lavoro con l'incapsulamento! 🔒**
