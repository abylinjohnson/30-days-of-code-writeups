num = int(input())
k = (num+num)-1
l=0
for i in range(0,num+1):
    for j in range(l):
        print(" ",end="")
    for j in range(0,k):
        print("*",end="")
    print()
    l = l + 1
    k = k -2