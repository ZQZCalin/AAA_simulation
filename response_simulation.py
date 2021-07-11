from math import factorial

def comb(n, k):
  return factorial(n) / ( factorial(k) * factorial(n-k) )

n = 20
k = 5

p_list = [0.1, 0.2, 0.3, 0.4]

for p in p_list:

  prob_X_leq_k = sum([ comb(n, i) * p**i * (1-p)**(n-i)  for i in range(0, k+1) ])

  prob_remove_all_but_k = 1 / comb(n, k)

  prob_remaining = sum([ comb(n-k, i) / comb(k+i, k) * p**(k+i) * (1-p)**(n-k-i)  for i in range(1, n-k+1) ])

  total_prob = prob_X_leq_k * prob_remove_all_but_k + prob_remaining
  # one thing is to check this value against multiple values of p
  # if it changes with p, then obviously it's not the same as P_A

  print("at p = {}, P_D: {} vs P_A: {}".format(p, total_prob, 1/comb(n, k)))