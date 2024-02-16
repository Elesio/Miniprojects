def closest(list, element):
    close = list[0]
    for i in range(len(list)):
        if abs(list[i]-element) < abs(close-element):
            close = list[i]
    return close

vlist = [0,5,10,15,20]
el = 7.501
print(closest(vlist,el))