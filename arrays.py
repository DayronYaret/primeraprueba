a = [1, 3.9, "Hola que tal"] #Esto es una lista de elementos, a diferencia del array, no tienen un tipo especifico
print(a)
b=a
b[2] = "Soy buenisimo"
print(b)
b.append("Mae mia willy, que era mas simple")
print(b)
b[-1] = b[0] #El indice negativo es contando a partir desde el final, en la linea cambio el ultimo elemento por el primero
print(b)
#todo hacer una rotacion de elementos