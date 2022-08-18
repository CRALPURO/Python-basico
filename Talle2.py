# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#2

#Definición de librerias
import math as mt 

#Definición de varibales
Var_inicial = 0
Contador = 0
Var_trabajo = 0

#Definición de funciones 
def Eleva(x):
    return mt.pow(2,x)

#MAIN
Var_inicial = int(input("Diguite cual el numero maximo de elevación que desea: "))

while Contador <= Var_inicial:

    Var_trabajo = Var_trabajo + (1/Eleva(Contador))
    Contador = Contador + 1


print(Var_trabajo)


