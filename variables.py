# -*- coding: utf-8 -*-
#

# Esto es un comentario mágico

# Esto es un Here-doc

"""
Esto es el heredoc
"""

mensaje = '''
Esto también es un comentario o heredoc
Esto es otra línea
'''

# Cadenas de carácteres (strings)

nombre = "Jean"
apellido = 'Soto' # Esta es la forma preferida

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)


print(len(nombre))

# Función

print(nombre.upper())
print(nombre.lower())
print(nombre.replace('J', 'Y'))

# Formateo de cadenas

mensaje_de_saludo = 'Hola soy %s mucho gusto' % nombre
print(mensaje_de_saludo)

nombre_dado = input('Dime tu nombre: ')
print(nombre_dado)
print("Tu nombre tiene %s letras" % len(nombre_dado))
