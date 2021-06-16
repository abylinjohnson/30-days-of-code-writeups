n = int(input())
lst = input().split()
arr = []
sum = 0
for i in range(n):
    if int(lst[i]) not in arr:
        arr.append(int(lst[i]))
        sum = sum + int(lst[i])
print(sum)