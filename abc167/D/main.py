#!/usr/bin/python3

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
cur = 0
i = 0
loop = 0
list = []

while (i <= K):
  i = i+1
  cur = A[cur-1]
  if(loop == 0):
    if (cur in list):
#      loop = len(list)
#      print("loop", loop)
      loop = len(list) - list.index(cur)
      if (K > 100):
        K= K - ((K // loop))*loop
    list.append(cur)
#  print(cur)

print(cur)

