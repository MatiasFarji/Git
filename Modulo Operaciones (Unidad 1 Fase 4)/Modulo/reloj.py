from datetime import datetime #Importa la funcion para administrar el formato de Fecha y Hora
from os import system #Importa la funcion para limpiar la terminal/linea de comandos
from time import sleep #Importa funcion para detener la ejecucion determinados segundos

hora=datetime.now()
print("La hora actual es {}".format(hora.strftime("%H : %M : %S"))) #Muestra la hora en formato 24hs con division de :
sleep(5) #Detiene la ejecucion por 5 segundos
system("cls") #Limpia la terminal