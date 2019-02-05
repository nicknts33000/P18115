primes = []
a=int(input("δωστε αρχη διαστηματος: "))
b=int(input("δωστε τελος διαστηματος: "))
d=int(input("δωστε θετικο ακεραιο: "))
found=0
for possiblePrime in range(a, b+1):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        primes.append(possiblePrime)
for i in range(0,len(primes)):
 for j in range(0,len(primes)):
  if i!=j and abs(primes[i]-primes[j])==d:
    print("το ζευγος αριθμων ειναι p=",primes[i]," και q=",primes[j])
    found=1
 if found==1:
     break
if found==0:
    print("δεν βρεθηκε το καταλληλο ζευγος αριμων")
input("πατηστε enter για να κλεισει το παραθυρο")




