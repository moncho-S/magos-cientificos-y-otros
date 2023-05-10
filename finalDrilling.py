
nombres = ["Harry Houdini", "Newton", "David Blaine",
           "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
magosGrandiosos = magos.copy()
cientificos = ["Newton", "Hawking", "Einstein"]
otros = nombres.copy()

for m in magos:
    for o in otros:
        if o == m:
            otros.remove(o)
            break
for c in cientificos:
    for o in otros:
        if o == c:
            otros.remove(o)
            break


def hacer_grandioso():
    for i in range(len(magosGrandiosos)):
        magosGrandiosos[i] = "El gran "+magosGrandiosos[i]


def imprimir_nombres():
    print("Nombres sin modificar: ", end='')
    for i in nombres:
        print(i, end=", ")
    print("\n")


def imprimir_todos():
    print("Magos: ", end="")
    for i in magosGrandiosos:
        print(i, end=", ")
    print("")

    print("Cientificos: ", end="")
    for i in cientificos:
        print(i, end=", ")
    print("")

    print("Otros: ", end="")
    for i in otros:
        print(i, end=", ")
    print("")


hacer_grandioso()
imprimir_nombres()
imprimir_todos()
