inpt = input()
n, total = int(inpt[:4]),  int(inpt[4:])
errors = []
fact_total = 0

for i in range(n):
    inpt = input()
    price, amount, cost = int(inpt[:7]), int(inpt[8:12]), int(inpt[13:])  
    if price * amount != cost:
        errors.append(i+1)
    fact_total += price * amount
print(total - fact_total)
for k in errors:
    print(k, end=' ')