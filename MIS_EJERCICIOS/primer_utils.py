import math
def area_cuadrado(lado):
    resultado= lado**2
    return resultado
def area_triangulo(base,altura):
    resultado = (base* altura)/2
    return resultado
def area_circulo(radio):
    resultado = (math.pi * radio)**2
    return resultado


def fibonacci(n):
    if n == 1 or n == 2:
        return  1  #No valdría una variable resultado y decirle al final de la función que devuelva resultado?
    return fibonacci(n -1) + fibonacci(n-2)

def creador_frases(*args):
    for i in args:
        frase = " ".join(args)
    return frase


def añadir_eliminar (lista, comando,elemento=None):
    lista_1= lista.split()
    lista_2 = lista_1.copy()
    for i in lista_1:
        if comando == "remove" and i == elemento:
            lista_2.remove(i)
        elif comando == "add":
            lista_2.append(elemento)
            break
    
        
    return lista_2



def dict_string(string_1):
    lista_vacia = []
    for i in string_1.lower():
        lista_vacia.append(i)
        lista_vacia.append (contador_letras(string_1,i))
    resultado = dict(zip(lista_vacia[::2],lista_vacia[1::2]))
    return resultado


def contador_letras(frase, letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador+=1
        
    return contador


def comparacion (numero_1,numero_2):
    if numero_1 == numero_2:
        resultado = print("Son iguales")
    elif numero_1 > numero_2:
        resultado = print(f"El numero {numero_1} es mayor que {numero_2}")
    elif numero_1< numero_2:
        resultado = print(f"El numero {numero_2} es mayor que {numero_1}")
    return resultado

def piramide(numero_filas):
    for i in range(numero_filas,0,-1):
         print(*list(range(i,0,-1)))
    return print(*list(range(i,0,-1)))


def dias_semana(numero):
    semana = ["Lunes","Martes", "Miercoles","Jueves","Viernes","Sabado","Domingo"]
    if numero> 7:
        resultado = print("error, el numero debe estar entre el 1 y el 7")
    for i in range(1,8):
        if i == numero:
            resultado = semana [i -1]
    return resultado