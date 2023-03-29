from io import open
def contador():
    while True: #En caso de ingresar un valor erroneo, se repite el loop
        modo=input("Ingrese inc si quiere aumentar 1 unidad, o dec si quiere reducir 1 unidad al contador")
        with open("contador.txt","a+") as fichero: #Se lee el fichero
            fichero.seek(0) #Se lee desde la linea 0 pues modo a arranca la lectura al final
            contador=fichero.readline()
            if contador==None: #Se detectan posibles errores en la lectura del mismo
                contador=0
            else:
                try:
                    contador=int(contador)
                except TypeError:
                    print("El valor en el fichero no es de tipo numero, se formateara a 0")
                    contador=0
                except ValueError:
                    print("El valor en el fichero no es de tipo numero, se formateara a 0")
                    contador=0
            #Aqui se termina la comprobacion de errores de lectura

            #Se determina si el argumento ingresado por el usuario es correcto
            if modo=="inc":
                contador+=1
                print(contador)
                break
            elif modo=="dec":
                if contador>0:
                    contador-=1
                    print(contador)
                    break
                else:
                    print("Contador en 0, no se puede reducir mas")
            else:
                print("Valor actual:",contador)
                print("El argumento ingresado debe ser inc para incrementar 1 unidad o dec para reducir una unidad")

    with open("contador.txt","w") as fichero: #Se suscribe el fichero
        fichero.write(str(contador))
contador()