n = int(input())
p = []
for i in range(n):
    s = input()
    p.append(s)
for i in range(n):
    r = p[i][::-1]
    if r == p[i]:
        print("YES")
    else:
        print("NO")