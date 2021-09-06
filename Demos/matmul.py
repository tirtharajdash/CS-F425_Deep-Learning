import torch
import time

n = 100000

A = torch.rand(n, n)
B = torch.rand(n, n)

tic = time.time()
Z = torch.matmul(A, B)
toc = time.time()

print('Time:',(toc-tic),'s.')
