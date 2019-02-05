import random
lista_epilogon=["up","upright","upleft","center","right","left","down","downright","downleft"]
seira1h=["   ","   ","   "]
seira2h=["   ","   ","   "]
seira3h=["   ","   ","   "]
while len(lista_epilogon)!=0:
        print("εχετε τις εξης επιλογες:" , lista_epilogon ,".Πληκτρολογηστε μια απ τις παραπανω τιμες για αναλογα με την θεση που θελετε να σημαδεψετε. Ο παικτης εχει το x και η μηχανη το o.","\n")
        temp=input(":")
        lista_epilogon.remove(temp)
        if temp=="up":
                seira1h[1]=" x "
        elif temp=="upleft":
                seira1h[0]=" x "
        elif temp=="upright":
                seira1h[2]=" x "
        elif temp=="center":
                seira2h[1]=" x "
        elif temp=="left":
                seira2h[0]=" x "
        elif temp=="right":
                seira2h[2]=" x "
        elif temp=="down":
                seira3h[1]=" x "
        elif temp=="downleft":
                seira3h[0]=" x "
        elif temp=="downright":
                seira3h[2]=" x "
        print("|".join(seira1h))
        print("-----------")
        print("|".join(seira2h))
        print("-----------")
        print("|".join(seira3h))
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        if seira1h[0]==" x " and seira1h[1]==" x " and seira1h[2]==" x ":
                print("Νικησατε!! ")
                break
        elif seira2h[0]==" x " and seira2h[1]==" x " and seira2h[2]==" x ":
                print("Νικησατε!! ")
                break
        elif seira3h[0]==" x " and seira3h[1]==" x " and seira3h[2]==" x ":
                print("Νικησατε!! ")
                break
        elif seira1h[0]==" x " and seira2h[1]==" x " and seira3h[2]==" x ":
                print("Νικησατε!! ")
                break
        elif seira1h[2]==" x " and seira2h[1]==" x " and seira3h[0]==" x ":
                print("Νικησατε!! ")
                break
        elif seira1h[0]==" x " and seira2h[0]==" x " and seira3h[0]==" x ":
                print("Νικησατε!! ")
                break
        elif seira1h[1]==" x " and seira2h[1]==" x " and seira3h[1]==" x ":
                print("Νικησατε!! ")
                break
        elif seira1h[2]==" x " and seira2h[2]==" x " and seira3h[2]==" x ":
                print("Νικησατε!! ")
                break
        temp2=random.choice(lista_epilogon)
        lista_epilogon.remove(temp2)
        if temp2=="up":
                seira1h[1]=" o "
        elif temp2=="upleft":
                seira1h[0]=" o "
        elif temp2=="upright":
                seira1h[2]=" o "
        elif temp2=="center":
                seira2h[1]=" o "
        elif temp2=="left":
                seira2h[0]=" o "
        elif temp2=="right":
                seira2h[2]=" o "
        elif temp2=="down":
                seira3h[1]=" o "
        elif temp2=="downleft":
                seira3h[0]=" o "
        elif temp2=="downright":
                seira3h[2]=" o "
        print("|".join(seira1h))
        print("-----------")
        print("|".join(seira2h))
        print("-----------")
        print("|".join(seira3h))
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        if seira1h[0]==" o " and seira1h[1]==" o " and seira1h[2]==" o ":
                print("Χασατε:(")
                break
        elif seira2h[0]==" o " and seira2h[1]==" o " and seira2h[2]==" o ":
                print("Χασατε:(")
                break
        elif seira3h[0]==" o " and seira3h[1]==" o " and seira3h[2]==" o ":
                print("Χασατε:(")
                break
        elif seira1h[0]==" o " and seira2h[1]==" o " and seira3h[2]==" o ":
                print("Χασατε:(")
                break
        elif seira1h[2]==" o " and seira2h[1]==" o " and seira3h[0]==" o ":
                print("Χασατε:(")
                break
        elif seira1h[0]==" o " and seira2h[0]==" o " and seira3h[0]==" o ":
                print("Χασατε:(")
                break
        elif seira1h[1]==" o " and seira2h[1]==" o " and seira3h[1]==" o ":
                print("Χασατε:(")
                break
        elif seira1h[2]==" o " and seira2h[2]==" o " and seira3h[2]==" o ":
                print("Χασατε:(")
                break
input("press enter to finish")

