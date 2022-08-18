# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#3

#Definición de variables

Var_inicial = 0
Contador = 1
Var_trabajo = 0


#MAIN

while Contador <= 100000:
    
    Var_trabajo = Var_trabajo + 1
    
    if Var_trabajo < 40000 or Var_trabajo > 50000: #Valida que no este en el rango y suma
        if Var_trabajo < 70000 or Var_trabajo > 80000: #Valida que no este en el rango y suma
            Var_inicial = Var_inicial + Var_trabajo 

    Contador = Contador + 1


print(Var_inicial)