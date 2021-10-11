# CORTAR NUESTRAS STRINGS
# Python nos permite cortar nuestras strings de manera que podamos tomar las posiciones de los caracteres que deseemos.
# Para eso debemos indicar entre [corchetes] las posiciones de inicio y fin, separados por : (dos puntos).

name = "Koche" # Creo la variable con su valor Koche.
print(name[2:5]) # Mostrará la posición 2 hasta la anterior a la 5. En este caso será "che" de mi string "K0-o1-c2-h3-e4"

# Si no indicamos ninguna posición al final. Tomará hasta el último caracter por defecto.
print(name[2:]) # Mostrará los caracteres 'che'.

# De igual manera si tampoco indicamos el inicio, tomará por defecto la primera posición.
print(name[:3]) # Mostrará los caracteres 'Koc'
