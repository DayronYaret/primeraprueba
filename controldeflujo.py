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
    ##if edad % 2 == 0: con esto solo imprime el mensaje en numeros impares
      ##  continue
    print("Ahora mismo tienes " + str(edad))

print("habla contigo mismo, para salir escriba venga puto")
while True:
    entrada = input()
    if entrada == "venga puto":
        print("se terminó la conversación")
        break
    else:
        print(entrada)

secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)

"""range crea una lista con numeros desde el inicio que es 30 hasta 50 que es el final, el bucle consiste en hacer print al valor que toma i en cada iteracion del
for, pero acaba en 49, por lo que para llegar a 50 lo hago de forma manual"""
for i in range(30, 50):
    print(i)
    if i == 49:
        print("50")
