def arfil(list):
    for i in range(1000):
        list.append(i+2)
    return list

def bynum(num,acnum):
    if num == 0:
        return True
    elif num < acnum:
        return False
    else:
        return bynum(num-acnum,acnum)

def remove(list,num):
    result = [1]
    cur = list[0]
    curlist = list
    counter = 0
    while counter < num:
        cur = curlist[0]
        counter = counter + 1
        count = 0
        new = []
        for i in range(len(curlist)):
            if bynum(count,cur) == False:
                new.append(curlist[i])
            count = count + 1
        curlist = new
        result.append(cur)
    return result

numlis = []
goal = int(input('What number?'))
print(remove(arfil(numlis),goal))