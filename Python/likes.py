likes1 = []
likes2 = ['Zinedine']
likes3 = ['Noah','Tobias']
likes4 = ['Frederik','Daniel','Ricardo']
likes5 = ['Fabian','Laura','Ginie','Lars']

def cut(list):
    newList = []
    for i in range(len(list)-1):
        newList.append(list[i+1])
    return newList

def likesOut(likes):
    if len(likes) == 0:
        return 'Nobody has liked this post yet'
    if len(likes) == 1:
        out = 'This post was liked by ' + likes[0]
        return out
    if len(likes) >= 2 and len(likes) <= 3:
        out = 'This post was liked by '
        while len(likes) > 2:
            out = out + likes[0] + ', '
            likes = cut(likes)
        out = out + likes[0] + ' and ' + likes[1]
        return out
    if len(likes) >= 4:
        return 'This post was likes by multiple people you know'

print(likesOut(likes1))
print(likesOut(likes2))
print(likesOut(likes3))
print(likesOut(likes4))
print(likesOut(likes5))