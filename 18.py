n = int(input())
lst = input().split()
arr = []
even = 0
odd = 0
for i in range(n):
    if int(lst[i])%2 == 0:
        even +=1
    else:
        odd +=1
print(even)
print(odd)