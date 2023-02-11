""" STRINGS """

my_string = "mi string"
my_other_string = 'Mi Otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_escape_string = "\tEste es un string \n escapado"
print(my_escape_string)



# FORMATEO

name, surname, age = 'Javier', 'Sierra', 25


print("mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #el porcentaje hace que el primer texto que le pase formateado a esta cadena de texto
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))
#print("mi nombre es %s %s y mi edad es %d" %(name, surname, "ey"))  error en la cadena porque espera un integer
print(f"mi nombre es {name} {surname} y mi edad es {age}") # INFERENCIA DE DATOS



# DESEMPAQUETADO DE CARACTERES

language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)



# DIVISION

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[0:6:2] # coge el rango de caracter 0 a caracter 6 y evita los saltos de 2 (Python -> Pto)
print(language_slice)

language_slice = language[0:6:3] # coge el rango de caracter 0 a caracter 6 y evita el 2 (Python -> Pto)
print(language_slice)

language_slice = language[-2]
print(language_slice)



# REVERSE

reversed_language = language[::-1]
print(reversed_language) #nohtyP

reversed_language = language[::-2]
print(reversed_language) #nhy

reversed_language = language[::-3]
print(reversed_language) #nt



# FUNCIONES DEL SISTEMA

print(language.capitalize()) # capitaliza cadenas
print(language.upper()) #todo mayuscula
print(language.count("t")) # cuantas t tiene python
print(language.isnumeric()) # es numero?
print("1".isnumeric()) # es numero?
print(language.lower()) # todas minusculas
print(language.upper().isupper()) # te transforma la cadena a mayusculas y despues comprueba si es toda mayuscula
print(language.upper().islower()) # transforma a mayusculas y comprueba si es todo minusculas
print(language.startswith("py")) # ¿la cadena empieza por "py"?
print(language.upper().startswith("PY")) # genera la cadena en mayusculas y comprueba si empieza por