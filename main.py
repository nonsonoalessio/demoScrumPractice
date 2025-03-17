import questionary
import math

def add(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def power(a, b):
    return a ** b
def sqrt(a):
    if(a > 0):
        return math.sqrt(a)
def log(a):
    return math.log(a)
def log10(a):
    return math.log10(a)
def sin(a, radians):
    return math.sin(a if radians else math.radians(a))
def cos(a, radians):
    return math.cos(a if radians else math.radians(a))
def tan(a, radians):
    return math.tan(a if radians else math.radians(a))
def asin(a, radians):
    return math.degrees(math.asin(a)) if not radians else math.asin(a)
def acos(a, radians):
    return math.degrees(math.acos(a)) if not radians else math.acos(a)
def atan(a, radians):
     return math.degrees(math.atan(a)) if not radians else math.atan(a)

def memorySelector(memory):
    memoryStrings = [str(i) for i in memory]
    choice = questionary.select(
        "Scegli il numero da usare:",
        choices=memoryStrings,
    ).ask()
    i = memoryStrings.index(choice)
    return memory[i]

def validInput(prompt, memory, division=False):
    while True:
        try:
            a = questionary.text(prompt).ask().replace(',', '.').lower()
            
            if a == "ans":
                return memory[-1]
            elif a == "mem":
                return memorySelector(memory)
            
            num = float(a)
            
            if division and num == 0:
                raise ValueError
            
            return num
        except ValueError:
            print("L'input non è valido, riprova.")
            
def operatorChoice():
    return questionary.select(
        "Scegli un'operazione:",
        choices=[
            "Addizione", "Sottrazione", "Moltiplicazione", "Divisione", "Trigonometria", "Aiuto", "Esci"]).ask()


def trigonometry(memory, cycleCount):
    rad = True if questionary.select(
       "Misura degli angoli:",
       choices=["Gradi", "Radianti"]
    ).ask() == "Radianti" else False

    operation = questionary.select(
        "Scegli un'operazione:",
        choices=[
            "Potenza", "Radice Quadrata", "Logaritmo Naturale", "Logaritmo base 10", "Seno", "Coseno", "Tangente", "Arcoseno", "Arcocoseno", "Arcotangente", "Esci"]).ask()
    
    if operation == "Potenza":
        a = validInput(prompt="Inserisci la base, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci la base: ", memory=memory)
        b = validInput(prompt="Inserisci l'esponente, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci l'esponente: ", memory=memory)
        return power(a, b)
    elif operation == "Radice Quadrata":
        a = validInput("Inserisci il radicando, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il radicando: ", memory=memory)
        return sqrt(a)
    elif operation == "Logaritmo Naturale":
        a = validInput("Inserisci il numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il numero: ", memory=memory)
        return log(a)
    elif operation == "Logaritmo base 10":
        a = validInput("Inserisci il numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il numero: ", memory=memory)
        return log10(a)
    elif operation == "Seno":
        a = validInput("Inserisci l'angolo, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci l'angolo: ", memory=memory)
        return sin(a, rad)
    elif operation == "Coseno": 
        a = validInput("Inserisci l'angolo, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci l'angolo: ", memory=memory)
        return cos(a, rad)
    elif operation == "Tangente":
        a = validInput("Inserisci l'angolo, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci l'angolo: ", memory=memory)
        return tan(a, rad)
    elif operation == "Arcoseno":
        a = validInput("Inserisci il numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il numero: ", memory=memory)
        return asin(a, rad)
    elif operation == "Arcocoseno":
        a = validInput("Inserisci il numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il numero: ", memory=memory)
        return acos(a, rad)
    else:
        a = validInput("Inserisci il numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il numero: ", memory=memory)
        return atan(a, rad)
        
    
def show_help():
    help_text = {
        "operazioni_base": {
            "titolo": "OPERAZIONI ARITMETICHE DI BASE",
            "contenuto": [
                "Addizione (+): Somma due numeri",
                "Sottrazione (-): Sottrae il secondo numero dal primo",
                "Moltiplicazione (*): Moltiplica due numeri",
                "Divisione (/): Divide il primo numero per il secondo"
            ],
            "esempi": [
                "Addizione: 5 + 3 = 8",
                "Sottrazione: 10 - 4 = 6",
                "Moltiplicazione: 6 * 7 = 42",
                "Divisione: 20 / 5 = 4"
            ]
        },
        "operazioni_avanzate": {
            "titolo": "OPERAZIONI MATEMATICHE AVANZATE",
            "contenuto": [
                "Potenza (^): Eleva il primo numero alla potenza del secondo",
                "Radice Quadrata (√): Calcola la radice quadrata di un numero",
                "Logaritmo Naturale (ln): Calcola il logaritmo naturale (base e) di un numero",
                "Logaritmo in Base 10 (log10): Calcola il logaritmo in base 10 di un numero"
            ],
            "esempi": [
                "Potenza: 2 ^ 3 = 8",
                "Radice Quadrata: √16 = 4",
                "Logaritmo Naturale: ln(2.71828) ≈ 1",
                "Logaritmo Base 10: log10(100) = 2"
            ]
        },
        "funzioni_trigonometriche": {
            "titolo": "FUNZIONI TRIGONOMETRICHE",
            "contenuto": [
                "Seno (sin): Calcola il seno di un angolo",
                "Coseno (cos): Calcola il coseno di un angolo",
                "Tangente (tan): Calcola la tangente di un angolo",
                "Arcoseno (asin): Calcola l'arcoseno di un valore",
                "Arcocoseno (acos): Calcola l'arcocoseno di un valore",
                "Arcotangente (atan): Calcola l'arcotangente di un valore",
                "Modalità angoli: Puoi scegliere tra gradi o radianti"
            ],
            "esempi": [
                "Seno: sin(30°) = 0.5",
                "Coseno: cos(60°) = 0.5",
                "Tangente: tan(45°) = 1",
                "Arcoseno: asin(0.5) = 30°",
                "Arcocoseno: acos(0.5) = 60°",
                "Arcotangente: atan(1) = 45°"
            ]
        },
        "funzioni_memoria": {
            "titolo": "FUNZIONI DI MEMORIA",
            "contenuto": [
                "Tutti i risultati vengono automaticamente salvati in memoria durante l'esecuzione",
                "ANS: Usa il risultato precedente come input (digita 'ans' quando ti viene chiesto un numero)",
                "MEM: Accedi a qualsiasi risultato precedente dalla memoria (digita 'mem' quando ti viene chiesto un numero)"
            ],
            "esempi": [
                "Calcolo 5 + 3 = 8, poi uso 'ans' come primo numero per 'ans' * 2 = 16",
                "Accedi a risultati precedenti digitando 'mem' e selezionando dalla lista"
            ]
        },
        "comandi": {
            "titolo": "COMANDI SPECIALI",
            "contenuto": [
                "help: Mostra questo menu di aiuto (può essere digitato in qualsiasi momento)",
                "ans: Usa l'ultimo risultato come input",
                "mem: Accedi alla lista di tutti i risultati precedenti",
                "Cambia Modalità: Passa da gradi a radianti e viceversa per le funzioni trigonometriche"
            ]
        }
    }
    
    print("\n===== GUIDA CALCOLATRICE =====\n")
    
    for categoria, info in help_text.items():
        print(f"\n--- {info['titolo']} ---")
        for voce in info['contenuto']:
            print(f"· {voce}")
        if "esempi" in info:
            print("\nEsempi:")
            for esempio in info['esempi']:
                print(f"  {esempio}")
        
    for categoria, info in help_text.items():
        print(f"\n--- {info['titolo']} ---")
        for voce in info['contenuto']:
            print(f"· {voce}")
        if "esempi" in info:
            print("\nEsempi:")
            for esempio in info['esempi']:
                print(f"  {esempio}")

    print("\n\n")
    
def printExpression(a, b, operator, result):
    if(operator == 'Addizione'):
        print(f"{a} + {b} = {result}")
    elif(operator == 'Sottrazione'):
        print(f"{a} - {b} = {result}")
    elif(operator == 'Moltiplicazione'):
        print(f"{a} * {b} = {result}")
    else:
        print(f"{a} : {b} = {result}")

def calculator():
    memory = []
    cycleCount = 0
    result = None
    while True:
        operator = operatorChoice()

        while(operator == 'Aiuto'):
            show_help()
            operator = operatorChoice()
            
        if operator == 'Trigonometria':
            result = trigonometry(memory, cycleCount)
        
        else: 
            if operator == 'Esci':
                break

            a = validInput(prompt="Inserisci il primo numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il primo numero: ", memory=memory)
            
            if operator == 'Divisione':
                b = validInput(prompt="Inserisci il secondo numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il secondo numero: ", division=True, memory=memory)
            else:
                b = validInput(prompt="Inserisci il secondo numero, scrivi 'ans' per usare l'ultimo risultato o 'mem' per prelevare i numeri dalla memoria: " if cycleCount != 0 else "Inserisci il secondo numero: ", memory=memory)
            
            if operator == 'Addizione':
                result = add(a, b)
            elif operator == 'Divisione':
                result = division(a, b)
            elif operator == 'Moltiplicazione':
                result = multiplication(a, b)
            else:
                result = subtraction(a, b)
            
            printExpression(a, b, operator, result)

        print(f"Il risultato è: {result}")

        memory.insert(0, result)
        print(f"{result} salvato in memoria!\n")
        cycleCount += 1
            
        
if __name__ == '__main__':
    calculator()