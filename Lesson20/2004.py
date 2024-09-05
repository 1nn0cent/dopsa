import sys
lines = lambda line: line.strip().startswith('#')
count = sum(1 for line in sys.stdin if lines(line))
print(count)
