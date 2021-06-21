# simulation of Lemma 2

# CAVEAT: here the random split is implemented by
#   a random shuffle followed by a partition into N parts
#   which ensures that the each element has identical probability
#   of being splitted into each group

# WLOG, we assume that the first kN^2 elements are Byzantine

# LOWER BOUND ON N:
#   N satisfies ln(N^2) / sqrt(N^2) < [(1/2 - k)/2]^2

import numpy as np
from math import ceil
from sympy.solvers import solve
from sympy import symbols, log, sqrt

# this bound is too loose for simulation
def N_lower_bound(k):
  N = symbols('N')
  N_min = ceil(max(solve( 2*log(N) / N - (1/4-k/2)**2, N )))
  print("smallest N for k = {} is: {}".format(k, N_min))
  return N_min

# N_split: 2D N*N array, threshold: i is Byzantine iff i < thres
def check_EN(N, k, thres, verbose=False):
  arr = np.arange(N**2)
  np.random.shuffle(arr)
  arr = np.reshape(arr, (N,N))
  num_Byz = np.sum(arr < thres, axis=1)

  if verbose:
    print(num_Byz)
  return num_Byz, np.sum(num_Byz >= ceil(N/2)) == 0

if __name__ == "__main__":
  verbose = False
  num_iter = 1000

  k = 0.4
  N = 300
  thres = k * N**2

  results = []

  for i in range(num_iter):
    results.append(check_EN(N, k, thres, verbose=(verbose and i%100==0))[1])

  num_pass = sum(results)
  print("{} / {} trials satisfy condition EN".format(num_pass, num_iter))