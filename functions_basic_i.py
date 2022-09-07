#PREDICCIONES EN EL ARCHIVO EXCEL DIAGRAMAS T 

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 Original: 
"""
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
"""

# 2 editado para que funcione
def number_of_days_in_a_week_silicon_or_triangle():
    return 3
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle() + number_of_military_branches())


#3
def number_of_books_on_hold():
    return 5
    # return 10 
    # #sólo se toma en cuenta el primer return a menos que esté en un condicional bien anidado
print(number_of_books_on_hold())


#4
def number_of_fingers():
    return 5
    # print(10) 
    # luego del return no se sigue con el codigo de la función, se termina de ejecutar
print(number_of_fingers())


#5 original
"""
def number_of_great_lakes():
    print(7)
x = number_of_great_lakes()
print(x)
# Entrega None, ya que la función no esta retornando nada. La variable no esta recuperando nada de la funcion, recordar que el print no es retorno sólo impresion de consola.
"""

#5 Editado para que funcione
def number_of_great_lakes():
    return 7
x = number_of_great_lakes()
print(x)
# ahora si se imprime la x, ya que esta contiene el retorno de la funcion = 7

"""
#6 Original
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#salida: error NoneType, ya que las funciones sólo imprimen y no retornan
"""
#6 Modificado
def add(b,c):
    return(b+c) 
    #se cambió el print por return
print(add(1,2) + add(2,3)) # salida 8


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Se agrega lo siguiente para corroborar el tipo de dato que se retorna
print(type(concatenate(2,5))) #<class 'str'> el resultado es tipo str


#8
# Ejemplo de tener más de un return pero bien anidados en un condicional
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    #return 7
    #este return no esta siendo considerado ya que se han definido los dos return anidados, no esta haciendo nada ne la función. 
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    #return 3
    #este return no es considerado, igual que el caso anterior
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10
def addition(b,c):
    return b+c
    # return 10
    # este return no se considera, ya que hay uno antes que el
print(addition(3,5))


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

print ("se cabo el ejercicio 11")
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar() # aca si se pusiera el print(foobar()) se imprimiria dos veces el 300
print(b)

print ("se cabo el ejercicio 12")

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

print ("se cabo el ejercicio 13")

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

print ("se cabo el ejercicio 14")

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# revisar estos ultimos dos, son más complejos ya que el orden se complica.
