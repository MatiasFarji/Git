import random
from math import floor,ceil
def leer_numero(ini=0,fin=0,mensaje="El numero ingresado debe ser 0"):
    while True:
        try:
            numero=int(input(mensaje))
            if ini<=numero<=fin:
                return(numero)
                break
            else:
                pass
        except TypeError:
            print("Debe ingresar un numero")
        except ValueError:
            print("Debe ingresar un numero")

def generador():
    numeros=leer_numero(1,20,"Cuantos numeros quieres generar? [1-20]")
    modo=leer_numero(1,3,"Como quieres redondear?:\n1:Alza\n2:Baja\n3:Normal")
    lista_flotante=[]
    lista_int=[]
    for i in range(numeros):
        numero_flotante=random.uniform(0,101)
        lista_flotante.append(numero_flotante)
        if modo==1:
            numero_entero=ceil(numero_flotante)
        elif modo==2:
            numero_entero=floor(numero_flotante)
        else:
            numero_entero=round(numero_flotante)
        lista_int.append(numero_entero)
        
        print("Flotante {},Entero {}".format(numero_flotante,numero_entero))
    print(lista_int)
generador()
    