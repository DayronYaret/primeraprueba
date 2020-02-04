#condicionales
primerIf = "Mesa y sus libros"
if primerIf == "Mesa y sus libros":
    print("este if no tiene sentido")

segundoIf = "este tiene un else"
if segundoIf == "este tiene un else":
    print("ciertamente")
else:
    print("toma else")
tercerIf = 416
if tercerIf <100:
    print("el numero es menor a 100")
elif tercerIf > 100:
    print("el numero es mayor a 100")
else:
    print("el numero es 100 o ni siquiera es un numero")

#bucles
edad = 0
while edad <18:
    edad = edad + 1
    print("Ahora mismo tienes " + str(edad))

print("habla contigo mismo, para salir escriba venga puto")
while True:
    entrada = input()
    if entrada == "venga puto":
        break
    else:
        print(entrada)
#TODO pagina 33 de 160