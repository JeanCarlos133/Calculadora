def suma(n1, n2):
    resultado = n1 + n2
    return f"El resultado es: {resultado}"

def resta(n1, n2):
    resultado = n1 - n2
    return f"El resultado es: {resultado}"


def multiplicacion(n1, n2):
    resultado = n1 * n2
    return f"El resultado es: {resultado}"


def division(n1, n2):
    resultado = n1 / n2
    return f"El resultado es: {resultado}"

def elevacion(n1, n2):
    resultado = n1 ** n2
    return f"El resultado es: {resultado}"

def porciento(porciento, n1):
    resultado = (porciento / 100) * n1
    return f"El {porciento}% de {n1} es: {resultado}"

while True:


    print("opciones \n"
    "1. Suma \n" 
    "2. Resta \n" 
    "3. Multiplicacion \n" 
    "4. Division \n"
    "5. Elevacion \n" 
    "6. Porciento \n"
    "Q. Para salir")

    opcion = input("Digite el numero de su opcion: ").upper()

    if opcion == "1":
        n1 = int(input("Primer numero: "))
        n2 = int(input("Segundo numero: "))
        print(suma(n1, n2))

    elif opcion == "2":
        n1 = int(input("Primer numero: "))
        n2 = int(input("Segundo numero: "))
        print(resta(n1, n2))

    elif opcion == "3":
        n1 = int(input("Primer numero: "))
        n2 = int(input("Segundo numero: "))
        print(multiplicacion(n1, n2))

    elif opcion == "4":
        n1 = int(input("Primer numero: "))
        n2 = int(input("Segundo numero: "))
        print(division(n1, n2))

    elif opcion == "5":
        n1 = int(input("Primer numero: "))
        n2 = int(input("Segundo numero: "))
        print(elevacion(n1, n2))

    elif opcion == "6":
        n_porciento = int(input("Introduzca el porciento: "))
        n1 = int(input("Primer numero: "))
        print(porciento(n_porciento, n1))

    elif opcion == "Q":
        print("Saliendo del programa...")
        break
        
    else:
        print("El digito introducido no es correcto, intentelo nuevamente")

print("El programa ha finalizado")

