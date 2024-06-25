nums = input().split()
mk = input().split()
m = int(mk[0])
k = int(mk[1])
sum = 0
for i in range(m,k+1):
    sum += int(nums[i])**2
print(sum)