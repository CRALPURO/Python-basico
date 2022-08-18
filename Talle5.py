# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#3

#Definición de variables

Var_inicial = 0
Contador = 1
Var_trabajo = 0
Var_iteraciones = 0
entero = 0


#MAIN

entero = input("Diguite el numero hasta el cual desea sumar: ")

try:

    Var_iteraciones = int(entero)
    while Contador <= Var_iteraciones:
        
        Var_trabajo = Var_trabajo + 1 

        if Var_trabajo % 4 != 0:           # Si numero no es multiplo de 4 suma   
            Var_inicial = Var_inicial + Var_trabajo 
        
        Contador = Contador + 1

    print(Var_inicial)

except ValueError:

    print('No es un valor entero')