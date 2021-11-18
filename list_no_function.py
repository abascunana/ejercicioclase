def list(palabra): #esta función hace lo mismo que el list()
    x= [] #lista vacía en la que se concatenan las palabras
    e = palabra # "e" será igual a la palabra que se introduzca en list(input(..))
    for i in range(len(e)): # bucle que revisa la largaria de "palabra"
        x = x + [e[i]] #concatenación de todas las letras en "palabra"
    print(x) #print x para extraer la palabra ya diseccionada

list(input("introduce una palabra"))
