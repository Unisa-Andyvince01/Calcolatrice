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
