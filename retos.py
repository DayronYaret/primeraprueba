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
print("--------------------------------------------------")
print("The list with unique elements only")
print(myList)
######################################################################
#comprobacion de año bisiesto y cuantos dias tiene un mes

def isYearLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False  #


def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
            if isYearLeap(year) == True:
                return 29
            else:
                return 28



testYears = [1900,2000,2016,1987]      ##testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

#######################################################
#conversor l/100km a mpg(millas por galón);
mile = 1609.344 #m
gallon = 3.785411784 #l

def l100kmtompg(liters):
    mpg = 235.21/liters
    return mpg

def mpgtol100km(miles):
    l100km = 100*3.785411784/(1.609344*miles)
    return l100km

print(l100kmtompg(3.9)) ## 60.31143162393162
print(l100kmtompg(7.5)) ## 31.36194444444444
print(l100kmtompg(10.)) ## 23.52145833333333
print(mpgtol100km(60.3)) ## 3.9007393587617467
print(mpgtol100km(31.4)) ## 7.490910297239916
print(mpgtol100km(23.5)) ## 10.009131205673757
