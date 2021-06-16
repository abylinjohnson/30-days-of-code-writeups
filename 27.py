mr = input().split()
m=[]
for i in range(int(mr[0])):
    mi = input().split()
    m.append(mi)
for i in range(int(mr[1])):
    for j in range(int(mr[0])):
        print(m[j][i],end=" ")
    print()
    