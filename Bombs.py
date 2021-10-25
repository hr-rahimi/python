n,m = input("Please Enter Number Rows And Columns With Space Between : \n > ").split(' ')
print(n,m)
newlist = []
for i in range(0,int(n)):
    newlist.append([])
    for j in range(0, int(m)):
        newlist[i].append('0')
# print(newlist)
count = input("Please Enter Number Of Bombs : \n > ")
bombs = []
for x in range(0,int(count)):
    bombs.append(input())
print(bombs)


