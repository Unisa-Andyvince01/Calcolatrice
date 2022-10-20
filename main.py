/*OPERAZIONI ARITMETICHE*/
def addizione(a, b):
    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError('Non sono stati inseriti numeri reali!')
    return a + b

def sottrazione(a, b):
    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError('Non sono stati inseriti numeri reali!')
    return a - b

def moltiplicazione(a, b):
    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError('Non sono stati inseriti numeri reali!')
    return a * b

def divisione(a, b):
    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError('Non sono stati inseriti numeri reali!')
    if(b == 0):
        raise ZeroDivisionError('Error: Il secondo termine inserito è uguale a 0')
    return a / b
