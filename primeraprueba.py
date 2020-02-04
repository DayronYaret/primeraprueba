import random
def generateRandom(upper): #si pones """ haces una especie de comentario a lo javadoc
    """

    :param upper: >=0
    :return: int
    """
    r = random.randint(1,upper)
    return r

def main(): #todo finish this function
    run = True
    num1 = generateRandom(39)
    num2 = generateRandom(416)
    result = num1 * num2
    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if ans.isdigit():
            if int(ans) == result:
                print("correct")
                run = False
            else:
                print("nah you slly sausage")

        else:
            print("answer must be a positive number")

#global vars esto sigue siedo una prueba
times = 10

for x in range(times):
    main()
