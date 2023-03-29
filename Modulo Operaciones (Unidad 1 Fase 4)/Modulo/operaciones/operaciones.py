def suma(numero_1,numero_2):
    try:
        return (numero_1+numero_2)
    except TypeError:
        print("Los valores ingresados deben ser numeros")

def resta(numero_1,numero_2):
    try:
        return (numero_1-numero_2)
    except TypeError:
        return("Los valores ingresados deben ser numeros")

def producto(numero_1,numero_2):
    try:
        return (numero_1*numero_2)
    except TypeError:
        return("Los valores ingresados deben ser numeros")

def division(numero_1,numero_2):
    try:
        return (numero_1/numero_2)
    except TypeError:
        return("Los valores ingresados deben ser numeros")
    except ZeroDivisionError:
        return("El segundo valor no puede ser 0!")