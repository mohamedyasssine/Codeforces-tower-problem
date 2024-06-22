t=int(input())
for i in range(t) :
    n=int(input())
    l=list(map(int,input().split()))
    resultat=l[0]
    l=sorted(l[1:])
    for j in l :
        if(j>resultat):
            resultat=(j+resultat+1)//2
    print(resultat)
