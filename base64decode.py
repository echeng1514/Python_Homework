

def base64decode(date):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    c = 0
    lst = []
    total= bytearray()
    result = str()
    for x in date:
        if x == '=':
            lst.append(0)
            continue
        lst.append(table.find(x))
    print(lst)
    for y in range(c,len(lst),4):
        ret = lst[y] << 18 | lst[y+1] << 12 | lst[y+2] << 6 | lst[y+3]
        total = (ret).to_bytes(3,'big')
        print(total)
        str1 = total.decode()
        print(str1)
        result += str1
        print(result)
    return print(result)



base64decode('YWJjYQ==')