import torch
import time

device = torch.cuda.current_device()

n = 10000

A = torch.rand(n, n).to(device)
B = torch.rand(n, n).to(device)

tic = time.time()
Z = torch.matmul(A, B)
toc = time.time()

print('Time:',(toc-tic),'s.')

