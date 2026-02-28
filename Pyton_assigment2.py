# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
lista_compra = ['Manzanas', 'Peras', 'Platanos', 'Sandia'] # List
alumnos = ('Patricia', 'Miguel', 'Antonio', 'Alba', 'Manuel') # Tuple
cantidad = 3 # Integer
nota = 2.5 # Float
precio = Decimal ('10.50') # Decimal
generos_literarios = {
    'dr' : 'Dark Romance',
    'df' : 'Dark Fantasy',
    'r' : 'Romance',
    'f' : 'Fantasy'} # Dictionary 

# Exercise 2: Round your float up.
import math
nota_redondeada = math.ceil(nota)

# Exercise 3: Get the square root of your float.
import math
raiz_cuadrada = math.sqrt(nota)

# Exercise 4: Select the first element from your dictionary.
primer_genero = generos_literarios ['dr']

# Exercise 5: Select the second element from your tuple.
mejor_alumno = alumnos [1]

# Exercise 6: Add an element to the end of your list.
lista_compra.extend(['Kiwi'])


# Exercise 7: Replace the first element in your list.
lista_compra [0] = 'Melocotones'

# Exercise 8: Sort your list alphabetically.
lista_compra.sort()

# Exercise 9: Use reassignment to add an element to your tuple.
alumnos = alumnos + ('Pilar',)

