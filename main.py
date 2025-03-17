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
    if a > 0:
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

def memorySelector(memory, prompt):
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
                return memorySelector(memory, prompt)
            
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
            "Addizione", "Sottrazione", "Moltiplicazione", "Divisione", "Trigonometria, Potenza, Radice Quadrata e Logaritmi", "Cronologia Operazioni", "Aiuto", "Esci"
        ]).ask()

def calculator():
    memory = []
    cycleCount = 0
    result = None
    while True:
        operator = operatorChoice()

        while operator == 'Aiuto':
            show_help()
            operator = operatorChoice()
            
        if operator == 'Trigonometria, Potenza, Radice Quadrata e Logaritmi':
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
            
            print(printExpression(a, b, operator, result))
            
        print(f"Il risultato è: {result}")
        memory.insert(0, result)
        print(f"{result} salvato in memoria!\n")
        cycleCount += 1

if __name__ == '__main__':
    calculator()