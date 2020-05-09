import sys

n = input()
l = list(map(int, input().split()))

loop = 0

while (1):
  for i in l:
    print('loop', loop)
    if i % (2 ** loop + 1) != 0:
      print(loop)
      sys.exit(0)
  loop = loop + 1