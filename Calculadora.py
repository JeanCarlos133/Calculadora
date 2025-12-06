def sum(n1, n2):
    resultado = n1 + n2
    return f"El resultado es: {resultado}"

def rest(n1, n2):
    resultado = n1 - n2
    return f"El resultado es: {resultado}"


def mult(n1, n2):
    resultado = n1 * n2
    return f"El resultado es: {resultado}"


def div(n1, n2):
    resultado = n1 / n2
    return f"El resultado es: {resultado}"

def elevacion(n1, n2):
    resultado = n1 ** n2
    return f"El resultado es: {resultado}"

def porciento(porciento, n1):
    resultado = (porciento / 100) * n1
    return f"El {porciento}% de {n1} es: {resultado}"


print("opciones \n"
"1. suma \n" 
"2.resta \n" 
"3.multiplicacion \n" 
"4. divicion \n"
"5. Elevacion \n" 
"6. Pociento")

opcion = input("Digite el numero de su opcion: ")

if opcion == "1":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(sum(n1, n2))

elif opcion == "2":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(rest(n1, n2))

elif opcion == "3":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(mult(n1, n2))

elif opcion == "4":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(div(n1, n2))

elif opcion == "5":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(elevacion(n1, n2))

elif opcion == "6":
    n_porciento = int(input("Introduzca el corciento: "))
    n1 = int(input("Primer numero: "))
    print(porciento(n_porciento, n1))
    

else:
    print("El digito introducido no es correcto, intentelo nuevamente")


