#listas
a = [1, 3.9, "Hola que tal"] #Esto es una lista de elementos, a diferencia del array, no tienen un tipo especifico
print(a)
b=a
b[2] = "Soy buenisimo"
print(b)
b.append("Mae mia willy, que era mas simple") #append es para añadir un nuevo elemento a la lista
print(b)
b[-1] = b[0] #El indice negativo es contando a partir desde el final, en la linea cambio el ultimo elemento por el primero
print(b)
#slicing, coger varios elementos
print(b[0:2]) #coge desde el 0 hasta la posicion 2 sin incluir (coge posicion 0 y 1)
print(b[::-1]) #recorre del revevs
print(b[0::2]) #coge los elementos cada 2 posiciones como en matlab
#rotacion de elementos
b.append(416)
print(b)
temp = b[0]
b[0] = b[-1]
b[-1] = temp
print(b)
c = [1, "Anto", [2, "mesa"]]
print(c[-1][1]) # asi se coge el elemento de una lista dentro de otra lista
#las tuplas se hacen de la misma forma que una lista, pero en lugar de [] se utiliza () para a creacuib. La diferencia
#de las listas y las tuplas es que las tuplas son constantes y usan menos memoria

#diccionario
diccionario = {"Anto": "El antenas",
"Mesa": "El bloque cadena",
"Dayron": "El camaras"}
print(diccionario)
print(diccionario["Mesa"])
diccionario["Mesa"] = "el cadena bloque"
print(diccionario)
#Los diccionarios no pueden hacer slicing, coger varios elementos a la vea
