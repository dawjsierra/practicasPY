""" OPERADORES ARITMETICOS """


print(3+4)
print(3-4)
print(10/2) #division
print(3/4)
print(10%2) #resto
print(10 // 3) #floor division, que se intente acercar el resultado sin hacer la division
print(2 ** 3) #dos elevado a 3

print("Hola" + "Python")
print("Hola" + "Python" + str( 5)) #combinar strings con numeros
print("Hola " *10) #multiplicar el numero de repeticion de palabra


my_float = 2.5*2
print("Hola "* int(my_float))



""" OPERADORES COMPARATIVOS """

""" print(3>4)
print(3<4)
print(3>=4)
print(3<=4)
print(3==4)
print(3!=4)
print(3 > 4 > 2) """

print("Hola">"Python")
print("Hola"<"Python")
print("Hola"<="Python")
print("Hola">="Python")
print("Hola"=="Python")
print("Hola"!="Python")
print("Hola">="Zola") #al tener el mismo num de caracteres, es una ordenacion alfabetica
print("aa">="aa") 
print("aaa">="aba") 
print(len("aaa")>= len("aba"))




""" OPERADORES LÓGICOS """
print(" ")
print(" ")
print(" ")
print(" ")

print(3>4 and "Hola">"Python")
print(3>4 or "Hola">"Python")
print(3>4 and "Hola"<"Python")
print(3>4 or "Hola"<"Python")
print(not(3>4)) #con el not le negamos toda la condicion. Es decir, la comparacion entraria en el not. "si no es 3 mayor que 4...", sale true
