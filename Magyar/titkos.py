import random


def titkos():
    gyufak = random.randint(40, 60)
    print(f"a jatek kezdete{gyufak} gyufa van a kupacban")

    while gyufak > 0:
        jatekos1 = int(input("1,2, vagy 3 gyufat veszel el: "))
        while jatekos1 < 1 or jatekos1 > 3:
            print("Nem jo!")
            jatekos1 = int(input("1, 2, 3 gyufat vesz el: "))
        gyufak -= jatekos1
        print(f"a jatekos elvet {jatekos1} gyufat, {gyufak} gyufa maradt.")
        if gyufak > 0:
            gep_huz = random.randint(1, 3)
            gyufak -= gep_huz
            print(f"a gep elvet egyet{gep_huz} gyufat{gyufak} gyufa maradt.")
            if gyufak <= 0:
                print("a gep vesztett.")
        else:
            print("a jatekos vesztett.") 
    print("a jateknak vege.")              

        
    









titkos()

