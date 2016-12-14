import math

x = 20
for n in range(0,x):
    for _ in range(0,x):
        print(end=' ')
    x-=1
    for m in range(0,n+1):
        c = int(math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))
        print(c,end='  ')
    print()
