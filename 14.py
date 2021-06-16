num = int(input())
for i in range(0,num+1):
    if i != 0:
        for j in range(0,num-i):
            print(" ",end="")
    for j in range(i):
        print(chr(97+j),end="")
    for j in range(i-1):
        print(chr(97+(i-j-2)),end="")
    if i !=0:
        print()