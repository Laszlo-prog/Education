import random
#def lista_maximum(lista):
    #max = lista[0]
    #for elem in lista:
        #if elem > max:
            #max = elem
    #return max

def lista_minim(lista):
    min = lista[0]
    for elem in lista:
        if elem < min:
            min = elem
    return min

def main():
    print("=======Hello===")
    szamok = []
    for i in range(64):
        szamok.append(random.randint(1, 100))
        print(szamok)
        #print(lista_maximum(szamok))
        print("==================")
        print(lista_minim(szamok))




if __name__ == "__main__":
    main()