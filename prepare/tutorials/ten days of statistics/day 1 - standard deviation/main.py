# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
X=[int(x) for x in input().split()]

media=sum(X)/n
X=[(x-media)**2 for x in X]
#desviacion=(sum(Y)/n)**(1/2)
print(round((sum(X)/n)**(1/2),1))
