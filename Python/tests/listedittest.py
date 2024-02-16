list = [[0] * 6] * 6
counter = 1

for i in range(6):
    for j in range(6):
        print('everything is fine')
        print(list)
        list[i][j] = counter
        print('something changed')
        print(list)
        counter = counter +1
        
'''altList = [[1,2,3,4,5,6],[17,8,9,10,11,12],[13,14,15,16,17,18]]
for h in range(2):
    for l in range(2):
        list[h][l] = 7
        print(list)'''