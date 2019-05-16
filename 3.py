#!/usr/bin/python3

#Strings
cadena = 'Hola mundo!'

print (cadena)          # Prints complete string
print (cadena[0])       # Prints first character of the string
print (cadena[2:5])     # Prints characters starting from 3rd to 5th
print (cadena[2:])	    # Prints string starting from 3rd character
print (cadena * 2)      # Prints string two times
print (cadena + "TEST") # Prints concatenated string

#Listas

lista = [ 'abcd', 786 , 2.23, 'esteban', 70.2 ]
listaPequena = [123, 'esteban']

print (lista)                # Prints complete list
print (lista[0])              # Prints first element of the list
print (lista[1:3])            # Prints elements starting from 2nd till 3rd 
print (lista[2:])             # Prints elements starting from 3rd element
print (listaPequena * 2)      # Prints list two times
print (lista + listaPequena)  # Prints concatenated lists

#Tuplas

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])    # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple, las tuplas no se pueden actualizar.
list[2] = 1000     # Valid syntax with list