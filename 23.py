n = int(input())
a = input().split()
arr = []
f = 0
m = 0
mode = 0
for i in range(len(a)):
    arr.append(int(a[i]))
for i in range(len(arr)):
    f = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            f = f+1
    
    if f > m:
        m = f
        mode = a[i]
    elif f == m:
        if a[i]>mode:
            mode = a[i]
    
        
print(mode) 