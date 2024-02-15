num = input('input a number')
full = int(num)
while len(str(full)) > 1:
    newfull = 0
    strfull = str(full)
    for i in range(len(str(full))):
        newfull = newfull + int(strfull[i])
    full = newfull
    print(full)