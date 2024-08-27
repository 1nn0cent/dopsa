num = int(input())
jun = [[input().endswith("5") for i in range(int(input()))] for j in range(num)]
print(["НЕТ", "ДА"][all(any(i) for i in jun)])