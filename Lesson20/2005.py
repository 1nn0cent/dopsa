import sys
print(any(["0" in i.split() for i in sys.stdin]))
