n = int(input())
lst = input().split()
arr = []
sum = 0
for i in range(n):
    arr.append(int(lst[n-i-1]))
       

for i in range(n):
    print(arr[i],end=" ")