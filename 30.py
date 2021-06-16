m=[]
s = 0
num = int(input())
for i in range(num):
    r=input().split()
    m.append(r)
for i in range(num):
    for j in range(num):
        if i==j or i+j==num-1:
            s += int(m[i][j])
print(s)