# STRINGS EN PYTHON
# Las strings en Python son cadena de textos que se pueden almacenar en las variables.
# El tipo de dato que le corresponde a las strings es: str.
# Importante que la valor declarado en la variable, debe ir entre comillas, simple o doble.

name = "Koche" # La variable name, tiene le valor Koche.
print(type(name)) # Mostrará class 'str'
print(name) # Mostrará Koche

# Mediante la función len() podemos saber la cantidad de caracteres que contiene el valor de nuestra variable.
print(len(name)) # Mostrará 5

# Las strings son cadena de caracteres. Cada caracter representa una posición.
# En Python la primera posición equivale a 0
print(name[0]) # Mostrará la K de "Koche"

# Podemos crear un loop para cada caracter de nuestra string.
# Mediante la keyword 'for' podemos crear un loop donde imprimirá cada caracter, hasta completar el último.
for character in name: # Para cada caracter en la variable name que haga lo siguiente:
  print(character) # Mostrar cada caracter
