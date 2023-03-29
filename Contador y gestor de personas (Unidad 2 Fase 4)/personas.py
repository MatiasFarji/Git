from io import open
import pickle
personas=[]
campos=["id","nombre","apellido","nacimiento"]

with open("personas.txt","a+",encoding="utf-8") as fichero: #Se lee el fichero en formato utf-8 para leer bien tildes y caracteres especiales, si no existe se crea en blanco
    fichero.seek(0)
    for persona in fichero.readlines(): #Se leen todas las lineas en formato de lista, y se iteran
        persona=persona.split(";") #Se convierte en lista cada persona 
        persona_dict=dict()
        for indice,valor in enumerate(persona): #Se itera cada campo de la persona
            if indice==3:
                persona_dict[campos[indice]]=valor.replace("\n","") #Se remueve el salto de linea del ultimo campo (Si lo tiene)
            else:
                persona_dict[campos[indice]]=valor
        personas.append(persona_dict) #Se genera el diccionario final

print("{}\t{}\t{}\t{}".format(campos[0],campos[1],campos[2],campos[3]))
for persona in personas:
    print("{}\t{}\t{}\t\t{}".format(persona["id"],persona["nombre"],persona["apellido"],persona["nacimiento"]))

