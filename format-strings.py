# FORMATO EN NUESTRAS STRINGS
# Como Python no nos permite concatenar de manera directa variables del tipo INT con las del tipo STR.
# Podemos hacerlo mediante el método FORMAT().

age = 35 # Creo la variable con mi dato int
name = "Koche" # Creo la variable con mi dato str
hi = "My name is " + name + ". I'm {} years old." # Creo una variable donde pueda almacenar la concatenación de las anteriores.
print(hi.format(age)) # Mostrará "My name is Koche. I'm 35 years old".

# Notar en la línea 7 que la variable str puede concatenarse con el simbolo "+".
# Pero la variable numérica debe ser reemplazada por las llaves en blanco.
# Donde luego el método FORMAT() indica que valor irá ahí dentro.


# En este caso veremos como concaternar dos variables númericas (o más) a un valor str.

weight = 80 # Creo mi variable 'int'
height = 1.75 # Creo mi variable 'float'
note = "My weight is {} kilograms and my height is {} meters." # Creo una variable con el valor 'str' y las llaves donde irán mis variables 'int' y 'float'.
print(note.format(weight,height)) # Mostrará "My weight is 80 kilograms and my height is 1.75 meters"

# En la línea 19 hemos indicado mediante {llaves} las posiciones que ocuparan nuestras variables no alfanuméricas.
# En la línea 20 mediante el método FORMAT() indicamos las variables a rellenar, según el orden en que queremos que se apliquen.
