n = int(input())
sum = 0
for i in range(0,n):
    x = int(input())
    sum = sum+x*(-1)**(i)
print(sum)