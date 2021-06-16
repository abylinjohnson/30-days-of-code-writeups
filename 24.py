n = int(input())
a = input().split()
arr = []
for i in range(n):
    arr.append(int(a[i]))
count = 0
result = count
for num in arr:
    count = (count + num) * num
    result = max(result, count)
print(result)   