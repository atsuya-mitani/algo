list = [304,5776,24,7,3,678,53,234]
disp = ""
for i in range(0,len(list)):
    disp = disp + str(list[i]) +" "
print("ソート前:",disp)

for i in range(len(list)-1,0,-1):
    for j in range(0,i):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)
