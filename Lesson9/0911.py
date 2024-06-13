#call 911 T_T

white_list = []
for _ in range(int(input())):
    white_list.append(input())
search = []
for _ in range(int(input())):
    search.append(input())
for i in search:
    if i in white_list:
        print(i)
