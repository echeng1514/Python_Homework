import time

lst = []
start = time.clock()
for i in range(2,1000000):
    if i == 2:
        lst.append(i)
        continue
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
ends = time.clock()
print(len(lst))
print('time is :%f s' % (start - ends))