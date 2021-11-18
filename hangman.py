import random
num_intents = 0
fruta = ["pera", "uva","lima","kiwi","limon"]
seleccion = random.choice(fruta)
x= [] #lista vacía en la que se concatena el resultado

def listpal(palabra): #esta función hace lo mismo que el list()
    global x
    e = palabra # "e" será igual a la palabra que se introduzca en list(input(..))
    for i in range(len(e)): # bucle que revisa la largaria de "palabra"
        x = x + [e[i]] #concatenación de todas las letras en "palabra"
    return x

disec = listpal(seleccion)

print("Bienvenido al juego del ahorcado,tienes 6 intentos, recuerda, introducir más de una letra no funcionará")

i=0 # empezamos con 0 intentos

   #palo inicial del monigote, no cambia por lo que se deja siempre fuera de los ifs
print ("______")
print ("|        |")  
    
 
#cada if imprime el proceso del cuerpo del monigote dependiendo del número de intentos,desde el palo vacío hasta el cuerpo entero
if num_intents == 0:
        print ("|")
        print ("|")
        print ("|")
elif num_intents == 1:
        
            print ("|        O")
            print ("|")
            print ("|")
elif num_intents == 2:                  
    print ("|        O")
    print ("|         |")
    print ("|")
elif num_intents == 3:

    print ("|        O")
    print ("|       /|")
    print ("|")
elif num_intents == 4:

    print ("|        O")
    print ("|       /|\ ")
    print ("|")
elif num_intents == 5:

    print ("|        O")
    print ("|       /|\ ")
    print ("|       / ")
elif num_intents == 6:
                            
    print ("|        O")
    print ("|       /|\ ")
    print ("|       / \ ")
    

print ("|")
print ("|___")
#palo final del monigote, no cambia por lo que se deja siempre fuera
print((len(disec)) * "_")

 
