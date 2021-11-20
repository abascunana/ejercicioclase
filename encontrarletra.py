 
def encontrar(palabra, letra): #esta función hace lo mismo que el list() pero en strings
    x = []
    e = palabra # "e" será igual a la palabra que se introduzca en listpal(input(..))
    for i in range(len(e)): # bucle que revisa la largaria de "palabra"
        x = x + [e[i]] #append de todas las letras en "palabra"
        if letra == e[i]:
            print("sí") 
        else: 
            print("no")
    return x  #el resultado final será x,por lo que se le hace un return
print(encontrar("hola","l"))
