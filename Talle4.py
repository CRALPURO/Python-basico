# ------------------------------------------     Taller Metodos numericos   --------------------------------------------------------------#
#4

#Definición de varibales
Dividiendo = 0
Divisor = 0

#MAIN
Dividiendo = int(input("Diguite el dividiendo: "))
Divisor = int(input("Diguite el divisor: "))

if Divisor == 0:
    print('ERROR EL DIVISOR ES 0')
else: 
    x = Dividiendo / Divisor
    print(x)