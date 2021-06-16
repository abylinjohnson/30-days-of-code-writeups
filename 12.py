num = int(input())

for i in range(num):
    for j in range((num*2)):
        if j <= num+i and  j >= num-i:
            print("*",end="")
        elif j == 0:
            print("",end="")
        else:
            print(" ",end="")
    print("\n",end="")