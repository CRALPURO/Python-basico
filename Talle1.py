# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#1

#Definición de librerias
import math as mt 

#Definición de listas
Lista_1 = []

#Definición de varibales
Var_inicial = 0
Contador = 0
Var_trabajo = 0

#Definición de funciones 
def Eleva(x):
    return mt.pow(x,2)

#MAIN
Var_inicial = int(input("Diguite cuales son los primeros x numeros que desea elevar al cuadrado: "))

while Contador <= Var_inicial:

    Var_trabajo = Contador
    Lista_1.append(Eleva(Var_trabajo))
    Contador = Contador + 1

print(Lista_1)






    





