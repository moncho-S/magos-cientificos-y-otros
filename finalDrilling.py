
nombres = ["Harry Houdini", "Newton", "David Blaine",
           "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
magosGrandiosos = []
cientificos = ["Newton", "Hawking", "Einstein"]
otros = nombres.copy()

for m in magos:
    for o in otros:
        if o == m:
            otros.remove(o)  # remueve los
for c in cientificos:
    for o in otros:
        if o == c:
            otros.remove(o)


def hacer_grandioso():
    for i, m in enumerate(magos):
        magosGrandiosos.append("El gran "+m)


def imprimir_nombres():
    print("Nombres: ", end='')
    for i in nombres:
        print(i, end=", ")
    print()


hacer_grandioso()
imprimir_nombres()

print("Magos Grandiosos: ", end="")
for i in magosGrandiosos:
    print(i, end=", ")
print()

print("Cientificos: ", end="")
for i in cientificos:
    print(i, end=", ")
print()

print("Otros: ", end="")
for i in otros:
    print(i, end=", ")
print()
