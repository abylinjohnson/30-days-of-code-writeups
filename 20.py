nr = input().split()
n = int(nr[0])
r = int(nr[1])
a = input().split()
arr = []
farr = []
for i in range(n):
    arr.append(int(a[i]))
arr = arr[r:] + arr[:r]
for i in range(n):
    print(arr[i],end=" ")