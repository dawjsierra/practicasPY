""" 
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""


horas=input("¿CUANTAS HORAS HAS TRABAJADO?")
horas = int(horas)

precio=input("¿CUANTO COBRAS POR HORA?")
precio = int(precio)

total=horas*precio

print("TE CORRESPONDEN",total,"EUROS")