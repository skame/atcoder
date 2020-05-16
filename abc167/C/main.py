#!/usr/bin/env python3

import numpy as np

N, M, X = list(map(int, input().split()))
C = np.zeros((N, M+1))
for i in range(1, N):
  C[i] = list(map(int, input().split()))
#a = list(map(int, input().split()))

