import math

def closestPosNeg(list, element):
    closestPos = math.inf
    closestNeg = -math.inf
    for i in range(len(list)):
        if list[i] < element:
            if abs(list[i]-element) < abs(closestNeg-element):
                closestNeg = list[i]
        if list[i] > element:
            if abs(list[i]-element) < abs(closestPos-element):
                closestPos = list[i]
    close = [closestNeg,closestPos]
    return close

list = [1,2,3,4,5,6,7,7.5,8,9,10]
print(closestPosNeg(list,8))