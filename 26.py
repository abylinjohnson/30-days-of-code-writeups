d1=input().split()
m1=[]
for i in range(int(d1[0])):
    m=input().split()
    m1.append(m)

d2=input().split()
m2=[]
for i in range(int(d2[0])):
    m=input().split()
    m2.append(m)
    
for i in range(len(m1)):
    for j in range(len(m2[0])):
        result = 0
        for k in range(len(m2)):
            result+=int(m1[i][k])*int(m2[k][j])
        print(result,end=" ")
    print()