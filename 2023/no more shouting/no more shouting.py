import sys

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    input = sys.stdin.readline().rstrip()
    lowercase_str = ''.join(c.lower() if c.isupper() else c for c in input)