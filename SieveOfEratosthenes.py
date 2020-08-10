n=int(input())
l=[]
for i in range(0,n+1):
    l.append(True)
p=2
while(p*p<=n):
    if(l[p]==True):
        num=p
        for j in range(p*p,n+1):
            if(j%p==0):
                l[j]=False
    p+=1
for i in range(2,n+1):
    if(l[i]==True):
        print(i,end=' ')
