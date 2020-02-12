#primer reto: Dado el array, eliminar los elementos que se repiten utilizando in o in not
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Initial list")
print(myList)
i=1
k=1
for num0 in myList:
    print("El elemento actual es " + str(num0))
    print("El valor de i es " + str(i))
    while num0 in myList[k:]:
        print("El valor de k es " + str(k))
        if num0 == myList[k] and k<len(myList):
            del myList[k]
            print("Elemento borrado")
        else:
            k+=1
    i+=1
    k=i
    print(myList)

print("The list with unique elements only")
print(myList)
#########################################################################