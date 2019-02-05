maxsum=0//athroisma pou den ipervainei 
mega = []
def maxDistance(lista,limit):
        global maxsum
        global mega
        lista.sort(reverse=True)
        for i in range(len(lista)):
                 mega.append(lista[i])
        for i in range(len(lista)):
                if lista[i]<=limit:
                        for j in range(len(lista)):
                                if i!=j:
                                        mega[i]=mega[i]+lista[j]
                                        if mega[i]>limit:
                                                mega[i]=mega[i]-lista[j]
        maxsum=max(mega)
        return maxsum
print ("Εισαγετε μια λιστα απο αποστασεις και υστερα αφου την καταχωρησετε ,καταχωρηστε εναν αριθμο ως οριο αθροισματος των προηγουμενων αποστασεων. Χωριστε τους αριθμους με κενα. ","\n")
lista=[float(x) for x in input("λιστα: ").split()]
limit=float(input("οριο: "))
maxDistance(lista,limit)
print (maxsum)
input("press enter to continue")
