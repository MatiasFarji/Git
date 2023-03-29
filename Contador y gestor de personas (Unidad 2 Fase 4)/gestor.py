from io import open
import pickle

class Personaje:
    def __init__(self,clase,vida,ataque,defensa,alcance):
       
                self.clase=clase
                self.vida=vida
                self.ataque=ataque
                self.defensa=defensa
                self.alcance=alcance

class Gestor:
    personajes=[]
    def __init__(self): #Importa los personajes del fichero
        with open("personajes.pckl","ab+") as fichero:
            fichero.seek(0)
            try:
                self.personajes=pickle.load(fichero)
            except:
                print("No hay personajes cargados")
    
    def guardar(self): #Sobreescribe fichero con todos los valores actuales
        with open("personajes.pckl","wb+") as fichero:
            pickle.dump(self.personajes,fichero)

    def mostrar(self): #Muestra string con todos los personajes
        print("Clase\t\tVida\t\tAtaque\t\tDefensa\t\tAlcance")
        for p in self.personajes:
            print("{}\t {}\t\t{}\t\t{}\t\t{}".format(p.clase,p.vida,p.ataque,p.defensa,p.alcance)) 
    def agregar(self,clase,vida,ataque,defensa,alcance):
         if type(clase)==str and type(vida)==int and type(ataque)==int and type(defensa)==int and type(alcance)==int:#Verifica que todos los argumentos tengan el formato correcto
            if vida>0 and ataque>0 and defensa>0 and alcance>0: #Verifica que todos los valores sean positivos
                for p in self.personajes: #Verifica si existe la clase, en caso contrario la crea
                    if p.clase==clase:
                        print("Ya existe esta clase")
                        break
                else:
                    personaje=Personaje(clase,vida,ataque,defensa,alcance)
                    self.personajes.append(personaje)
                    self.guardar()
            else:
                print("Los status deben ser mayores a 0")
         else:
            print("La clase debe ser de tipo str, los status tipo int")
                
                
        
    def eliminar(self,clase):#Funcion para eliminar personaje si existe
       
        if (type(clase)==str):
            for idx,p in reversed(list(enumerate(self.personajes))):
                if clase==p.clase:
                    del(self.personajes[idx])
                    self.guardar()
                    break
            else:
                print("No existe la clase informada")

#gestor=Gestor()

#gestor.agregar("Caballero",4,2,4,2)
#gestor.agregar("Guerrero",2,4,2,4)
#gestor.agregar("Arquero\t",2,4,1,8)
#gestor.mostrar()
