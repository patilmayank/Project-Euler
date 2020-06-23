import math
n=64
def factor(n):
  factorn=[]
  for x in range(1,int(math.sqrt(n))+1):
    if n%x==0:
      factorn.append(x)
      factorn.append(n/x)
  return factorn

factors_of_n = factor(n)

primefactors = []
for i in factors_of_n:
  print(i)
  factors_of_i = factor(i)
  if len(factors_of_i) == 2:
    # do something
    primefactors.append(i)
  print(factors_of_i)
sortedprimes=sorted(primefactors)
print(sortedprimes)
print(sortedprimes[-1])
