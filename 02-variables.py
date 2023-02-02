#variables

my_variable = 'My String variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)


#concatenación de variables en un print
print(my_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable )

#alguna funciones del sistema
print(len(my_variable))


#definir variables en una linea
name, surname, alias, age = "Javier", "Sierra", "Xavi", 35
print('Nombre: ', name, " Apellido: ", surname, " Alias: ", alias, " Edad", age)



#inputs
name = input("Cual es tu nombre?")
age = input ('Cuantos años tienes?')

print(name)
print(age)

#forzamos tipado
address: str = "mi direccion"
address = 32
print(address)