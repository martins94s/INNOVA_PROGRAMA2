###---------------------------------------------1,2---------------------------------------------------
numero=int(input("ingrese un numero: "))

if numero == 10:
    print("Usted a ganado")
elif numero <=10:
    print("¡Falto un poco, seguí participando!")
elif numero >=10:
    print("¡Te pasaste, a seguir intentando!")

#------------------------------------------------3---------------------------------------------------

semana=input("ingrese un dia de la semama: ")
if semana == "lunes" :
    print("buen comienzo de semana")
elif semana== "martes":
    print("martes")
elif semana== "miercoles":
    print("miercoles")
elif semana == "jueves":
    print("jueves")
elif semana == "viernes":
    print("buen finde")
elif semana == "sabado" or "domingo":
    print("disfrute el finde")
#----------------------------------------------4----------------------------------------------------------

letra = input("Ingrese una letra: ")
if letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print("Es vocal")
else:
    print("No es vocal")

#----------------------------------------EJERCICIOS ESTRUCTURAS REPETITIVAS--------------------------------

'''
Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
hasta que se ingrese -1.
'''
num = 0
suma= 0
while num != -1:
    num = int(input("ingrese un numero "))
    if num != -1 :
        suma += num
print("la suma es igual a : ",suma)

'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que
0, menores que 0 e iguales a 0.
'''
cantidad = int(input("Ingrese la cantidad de números a introducir: "))
mayores = 0
menores = 0
iguales = 0
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
print("Cantidad de números mayores que 0:", mayores)
print("Cantidad de números menores que 0:", menores)
print("Cantidad de números iguales a 0:", iguales)

'''
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
contrario, el programa termina cuando se introduce un cero.
'''
while True:
    caracter = input("Ingrese un caracter: ")
    if caracter == "0":
        break
    elif caracter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("VOCAL")
    else:
        print("NO VOCAL")

'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos.
'''
suma = 0
cantidad = 0
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    suma += numero
    cantidad += 1
media = suma / cantidad
print("La suma de los números es:", suma)
print("La media de los números es:", media)