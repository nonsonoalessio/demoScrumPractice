import questionary

def add(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

def validInput(prompt, lastOut, division=False):
    while True:
        try:
            a = questionary.text(prompt).ask().replace(',', '.').lower()
            
            if a == "ans":
                return lastOut
            
            num = float(a)
            
            if division and num == 0:
                raise ValueError
            
            return num
        except ValueError:
            print("L'input non è valido, riprova.")

def operatorChoice():
    return questionary.select(
        "Scegli l'operazione da eseguire:",
        choices=[
            "Addizione",
            "Sottrazione",
            "Moltiplicazione",
            "Divisione",
            "Esci"
        ],
    ).ask()
    
def calculator():
    memory = []
    cycleCount = 0
    result = None
    while True:
        a = validInput(prompt="Inserisci il primo numero o scrivi 'ans' per usare l'ultimo risultato: " if cycleCount != 0 else "Inserisci il primo numero: ", lastOut=result)

        operator = operatorChoice()

        if operator == 'Esci':
            break

        if operator == 'Divisione':
            b = validInput(prompt="Inserisci il secondo numero o scrivi 'ans' per usare l'ultimo risultato: " if cycleCount != 0 else "Inserisci il secondo numero: ", division=True, lastOut=result)
        else:
            b = validInput(prompt="Inserisci il secondo numero o scrivi 'ans' per usare l'ultimo risultato: " if cycleCount != 0 else "Inserisci il secondo numero: ", lastOut=result)
        
        if operator == 'Addizione':
            result = add(a, b)
        elif operator == 'Divisione':
            result = division(a, b)
        elif operator == 'Moltiplicazione':
            result = multiplication(a, b)
        elif operator == 'Sottrazione':
            result = subtraction(a, b)
        else:
            print("Operazione non valida.")

        print(f"Il risultato è: {result}")
        memory.append(result)
        print(f"{result} salvato in memoria!\n")
        cycleCount += 1
            

if __name__ == '__main__':
    calculator()