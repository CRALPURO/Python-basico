# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#7

#Definición de librerias
import math as mt 

#Definición de varibales
valor_e = 0
limite = 100


#Main 

x = int(input("Diguiete la potencia de euler: "))

for n in range(limite):
    valor_e += mt.pow(x,n)/mt.factorial(n)

print("El valor de euler por funciones de python es:", mt.pow(mt.e,x))
print("El valor de euler por logica de taylor es:",valor_e)