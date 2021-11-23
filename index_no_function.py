def indexse(palabra): #esta función hace lo mismo que el index()
    x = ["hola","holo","colo","84"]
    for i in range(len(x)): # bucle que revisa la largaria de lista x
        if x[i] == palabra: #si lista x(se tiene que cambiar) contiene el elemento "palabra",printea la posción
           print("elemento localizado en posición",i)
        else:
            print("no localizado")
    print(x) #print x para comprobar
indexse("83")
