# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A = input().split()
for i in range(n):
    A[i]=int(A[i])
A.sort()

#calculamos la media

suma=0
for val in A:
    suma+=val
media=suma/n

#calculamos la mediana
if(n%2==1):
    mediana=A[n//2]
else:
    mediana=(A[n//2-1]+A[n//2])/2

#calculamos la moda
maxcount=0
moda=999999
for i in range(n):
    if maxcount<A.count(A[i]) or (maxcount==A.count(A[i]) and moda>A[i]):
        maxcount=A.count(A[i])
        moda=A[i]

print(media)
print(mediana)
print(moda)
