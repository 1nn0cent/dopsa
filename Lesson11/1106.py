N = int(input())
print(', '.join([ i for i in [(input()) for _ in range(N)] if 'лук' not in i]))