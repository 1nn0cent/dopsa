s = list(input().lower())
count = set()
for i in s:
    count.add(s.count(i))
print(max(count))