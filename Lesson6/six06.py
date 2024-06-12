M = int(input())
N = int(input())
answer = []
home = set()
for _ in range(M):
    book = input()
    home.add(book)
for _ in range(N):
    book = input()
    if book in home:
        answer.append('YES')
    else:
        answer.append('NO')
for books in answer:
    print(books)