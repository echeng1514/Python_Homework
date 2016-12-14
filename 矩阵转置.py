# lst = [(3,4,5),(6,7,8),(0,1,2)]
print('plz input list :')
lst = []
for line in iter(input,'ends'):
    line1 = line.split(',')
    lst.append(line1)
for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
        print(lst[i][j],end=' ')
    print()
print()
for i in range(0,len(lst[i])):
    for j in range(0,len(lst)):
        print(lst[j][i],end=' ')
    print()


