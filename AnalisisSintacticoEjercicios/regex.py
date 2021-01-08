import re

opcion = 0
while opcion != 6:

    print("\nSelecion un Opcion")
    print("1.-Sentencia de asignacion")
    print("2.-Operaciones aritmeticas basicas")
    print("3.-Expresiones booleanas basicas")
    print("4.-Formulas complejas")
    print("5.-Estructura de control")
    print("6.-PARA SALIR")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(=)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(\+)|(-)|(\*)|(/)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 3:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(!=|>=|<=|==|<|>)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(//|%)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(?i)(\W|^)(if|while|for|or|and|xor|print|else|elif|is|in|not|break|pass|continue)(\W|$)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print("GRACIAS POR HABER USADO EL PROGRAMA")