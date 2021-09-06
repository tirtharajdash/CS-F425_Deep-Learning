import numpy as np
import time

n = 1000000000

A = np.random.rand(n)
B = np.random.rand(n)

tic = time.time()
C = np.dot(A, B)
toc = time.time()

print(C)
print('Duration: ',(toc-tic),'s')


tic = time.time()
C = 0
for i in range(n):
    C += A[i]*B[i]
toc = time.time()

print(C)
print('Duration: ',(toc-tic),'s')
