def sum(n1, n2):
    resultado = n1 + n2
    return f"El resultado es: {resultado}"

def rest(n1, n2):
    resultado = n1 - n2
    return resultado


def mult(n1, n2):
    resultado = n1 * n2
    return resultado


def div(n1, n2):
    resultado = n1 / n2
    return resultado


print("opciones \n"
"1. suma \n" 
"2.resta \n" 
"3.multiplicacion \n" 
"4. divicion")

opcion = input("Digite el numero de su opcion: ")

if opcion == "1":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    print(sum(n1, n2))

elif opcion == "2":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    rest(n1, n2)

elif opcion == "3":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    mult(n1, n2)

elif opcion == "4":
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    div(n1, n2)


