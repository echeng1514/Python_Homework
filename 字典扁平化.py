#扁平化字典，例如 {'a': {'b': 1}} 扁平化之后是 {'a.b': 1}

def dictconver(kw):
    print(kw)
    lst = []
    newdict = {}
    for k,v in kw.items():
        # print(k,v)
        for m,n in v.items():
            # print(m,n)
            st = k + '.' + m
            # print(st)
            # lst.append(st)
            newdict[st] = n
        print(newdict)


dictconver({'a': {'b': 1,'c' : 2,'d':3}})
