n = int(input())
lst = input().split()
arr = []
i = 1
for i in range(n):
    if int(lst[i]) not in arr:
        arr.append(int(lst[i]))
arr = sorted(arr)

print(arr[-2])