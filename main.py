import math

ans = None

def addizione(numbers):
    somma = 0
    for num in numbers:
        somma += float(num)
    return somma

def sottrazione(numbers):
    differenza = float(numbers[0])
    for num in numbers[1:]:
        differenza -= float(num)
    return differenza

def moltiplicazione(numbers):
    prodotto = 1
    for num in numbers:
        prodotto *= float(num)
    return prodotto

def divisione(numbers):
    divisione = float(numbers[0])
    for num in numbers[1:]:
        if(num.__contains__('0')):
            raise ZeroDivisionError('Errore: Il dividendo è uguale a 0!')
        divisione *= pow(float(num), -1)
    return divisione

def potenza(a, b):
    if(a.__contains__('0')):
        print('Warning: Il primo numero inserito è uguale a 0')
        return 0
    return pow(float(a), float(b))

def logaritmo(base, number):
    if(number.__contains__('0')):
        raise ArithmeticError('Errore: Il numero inserito è uguale a 0!')
    return math.log(float(number), int(base))

# Press the green button in the gutter to run the script.
def menu():

    print("CALCOLATRICE: OPERAZIONI DISPONIBILI")
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Potenza")
    print("6. Logaritmo")
    print("-------------------------")
    print("AZIONI DISPONIBILI")
    print("a. Cronologia Operazioni")
    print("b. Ans")
    print("0. Esci")

    print("-------------------------")
    scelta  = input("Scegli una operazione: ")
    return scelta

if __name__ == '__main__':

    memoria = dict()

    scelta=menu()
    while(scelta!=0):
        match scelta:
            case "1":
                list = tuple(input('Inserire gli operandi: ').split())
                ans = addizione(list)
                print("Risultato: ", ans)
                if(len(memoria) < 10):
                    memoria[ans] = 'Addizione'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Addizione'
            case "2":
                list = tuple(input('Inserire gli operandi: ').split())
                ans = sottrazione(list)
                print("Risultato: ", ans)
                if(len(memoria) < 10):
                    memoria[ans] = 'Sottrazione'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Sottrazione'
            case "3":
                list = tuple(input('Inserire gli operandi: ').split())
                ans = moltiplicazione(list)
                print("Risultato: ", ans)
                if(len(memoria) < 10):
                    memoria[ans] = 'Moltiplicazione'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Moltiplicazione'
            case "4":
                list = tuple(input('Inserire gli operandi: ').split())
                ans = divisione(list)
                print("Risultato: ", ans)
                print(len(memoria))
                if(len(memoria) < 10):
                    memoria[ans] = 'Divisione'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Divisione'
            case "5":
                a = input("Inserire il primo operando: ")
                b = input("Inserire il secondo operando: ")
                ans = potenza(a, b)
                print("Risultato: ", ans)
                print(len(memoria))
                if(len(memoria) < 10):
                    memoria[ans] = 'Potenza'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Potenza'
            case "6":
                a = input("Inserire la base del logaritmo: ")
                b = input("Inserire un numero: ")
                ans = logaritmo(a, b)
                print("Risultato: ", ans)
                print(len(memoria))
                if(len(memoria) < 10):
                    memoria[ans] = 'Logaritmo'
                else:
                    memoria.pop(next(iter(memoria)))
                    memoria[ans] = 'Logaritmo'
            case "a":
                print("Cronologia Operazioni")
                print(memoria)
            case "b":
                print('Ultimo risultato: ', ans)
            case "0":
                print("Spegnimento Calcolatrice")
                break

        scelta = menu()
