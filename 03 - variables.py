#!/usr/bin/python3

#Strings
cadena = 'Hola mundo!'

print (cadena)          # Imprime la cadena completa
print (cadena[0])       # Imprime el primer caracter de la cadena
print (cadena[2:5])     # Imprime los caracteres desde el tercero hasta el quinto
print (cadena[2:])	    # Imprime la cadena empezando desde el 3er caracter
print (cadena * 2)      # Imprime la cadena 2 veces
print (cadena + "TEST") # Imprime la cadea concatenada.

#Listas

lista = [ 'abcd', 786 , 2.23, 'esteban', 70.2 ]
listaPequena = [123, 'esteban']

print (lista)                # Imprime la lista cmpleta
print (lista[0])              # Imprime el primer elemento de la lista
print (lista[1:3])            # Imprime los elemento entre el segundo y el tercero
print (lista[2:])             # Imprime los elementos empezando desde el tercero
print (listaPequena * 2)      # Imprime la lista 2 veces
print (lista + listaPequena)  # Imprime 2 tuplas concatenadas

#Tuplas (una forma de coleccion o lista)

tupla = ( 'abcd', 786 , 2.23, 'esteban', 70.2  )
tuplapequena = (123, 'esteban')

print (tupla)           # Imprime la lista completa
print (tupla[0])        # Imprime el primer elemento de la lista
print (tupla[1:3])      # Imprime los elemento entre el segundo y el tercero
print (tupla[2:])    # 	# Imprime los elementos empezando desde el tercero
print (tuplapequena * 2)   # Imprime la lista 2 veces
print (tupla + tuplapequena) # Imprime 2 tuplas concatenadas


tupla2 = ( 'abcd', 786 , 2.23, 'esteban', 70.2  )
lista2 = [ 'abcd', 786 , 2.23, 'esteban', 70.2  ]
#tuple[2] = 1000    # Sintaxis invalidas con las tuplas, las tuplas no se pueden actualizar.
lista2[2] = 1000    # Sintaxis valida con listas

print (tupla2)
print (lista2)

#Diccionarios: Como los hash tables, las key pueden ser cualquier tipo de dato 
#pero por lo general se ocupan numeros o caracteres

dict = {}
dict['uno'] = "Valor uno"
dict[2]     = "Valor 2"

pequenodiccionario = {'nombre': 'Esteban','codigo':6734, 'area': 'programacion'}


print (dict['uno'])       # Imprime el valor para la llave 'uno'
print (dict[2])           # Imprime el valor para la llave '2'
print (pequenodiccionario)          # Imprime el diccionario completo
print (pequenodiccionario.keys())   # Imprime solo las llaves
print (pequenodiccionario.values()) # Imprime solo los valores