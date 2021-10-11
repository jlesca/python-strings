# MODIFICACIONES EN LAS VARIABLES STRINGS
# Una vez creada una variable que almacena un dato de tipo str, luego podemos realizar modificaciones sobre ella.
# Python nos permite realizarlo ejecutando algunas funciones.

# En este caso mediante el método UPPER() podemos convertir nuestros caractéres alpfanuméricos a MAYUSCULA.

name = "Koche" # Creo la variable y almaceno el valor Koche.
print(name.upper()) # Mostrará el mensaje 'KOCHE'.


# Del mismo modo con el método LOWER() podemos convertir nuestros caractéres alfanuméricos en MINUSCULA.

name = "KOCHE" # Creo la variable y almaceno el valor KOCHE (todo MAYUSCULA).
print(name.lower()) # Mostrará el mensaje 'koche'.


# Con el método REPLACE() podemos reemplazar un caractér especifico por otro.
# Los caractéres deberán indicarse entre "comillas", asignando el orginal separado por una coma y luego el que reemplazará.

print(name.replace("K", "C")) # Mostrará COCHE en lugar de KOCHE.


# Mediante el método SLIT()  podremos indicarle donde separar nuestra string.
# Se debe indicar entre comillas y Python dividirá nuestra str en dos.

name = "Koche" # Creo la variable con el valor Koche.
print(name.split("c")) # Esto mostrará ['Ko', 'he']


# En Python también podemos concatenar strings, ya sea entre variables o textos.

a = "I am " # Creo la variable con el primer str
b = "Koche" # Creo la variable con el segundo str
print(a + b) # Mostrará la concatenación entre ambas "I am " + "Koche"
