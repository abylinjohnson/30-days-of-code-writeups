d = input().split()
m1=[]
m2=[]
for i in range(int(d[0])):
    row=input().split()
    m1.append(row)
for i in range(int(d[0])):
    row=input().split()
    m2.append(row)
for i in range(int(d[0])):
    for j in range(int(d[1])):
       print(int(m1[i][j])+int(m2[i][j]),end=" ")
    print("")
