no = int(input())
nums = input()
sum = 0
num = nums.split()
for n in range(no):
    sum = sum + int(num[n])
print(sum)