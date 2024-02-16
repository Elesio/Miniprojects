'''
function y = vdP(Rs, Rv, Rh)
    y = exp(-pi * Rv ./ Rs) + exp(-pi * Rh ./ Rs) - 1;
end
'''
a = [1,3,2,8,7]
b = [5,3,9,1,4]
c = [6,2,8,9,3]

import math

def multList(Honkai,Genshin):
    StarRail = []
    for i in range(len(Honkai)):
        SRNum = Honkai[i] * Genshin
        StarRail.append(SRNum)
    return StarRail

def difList(first, second):
    third = []
    for i in range(len(first)):
        if type(first[0]) == list:
            thirdNum = first[i][0] / second[i][0]
        else:
            thirdNum = first[i] / second[i]
        third.append(thirdNum)
    return third

def expList(list):
    result = []
    for i in range(len(list)):
        resultnum = math.exp(list[i])
        result.append(resultnum)
    return result

def addList(stick,coal):
    torch = []
    for i in range(len(stick)):
        torchNum = stick[i] + coal[i]
        torch.append(torchNum)
    return torch

def adList(stick,coal):
    torch = []
    for i in range(len(stick)):
        torchNum = stick[i] + coal
        torch.append(torchNum)
    return torch



print(vdP(a,b,c))