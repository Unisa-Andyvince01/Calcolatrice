/*OPERAZIONI ARITMETICHE*/
def addizione(*numbers):
    somma = 0
    for num in numbers:
        somma += num
    return somma

def sottrazione(*numbers):
    differenza = numbers[0]
    for num in numbers[1:]:
        differenza -= num
    return differenza

def moltiplicazione(*numbers):
    prodotto = 1
    for num in numbers:
        prodotto *= num
    return prodotto

def divisione(*numbers):
    divisione = numbers[0]
    for num in numbers[1:]:
        if(num == 0):
            raise ZeroDivisionError('Errrore: Il dividendo è uguale a 0!')
        divisione *= pow(num, -1)
    return divisione

def main():

    scelta=menu()
    while(scelta!=0):
        match scelta:
            case "1":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", addizione(a,b))
            case "2":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", sottrazione(a,b))
            case "3":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", moltiplicazione(a,b))
            case "4":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", divisione(a,b))
            case "5":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", potenza(a,b))
            case "6":
                a=input("Inserire il primo operando: ")
                b=input("Inserire il secondo operando: ")
                print("Risultato: ", logaritmo(a,b))   
            case "a":
                print("Cronologia Operazioni")
            case "b":
                print("Ans")
            case "0":
                print("Spegnimento Calcolatrice")

        scelta = menu()
