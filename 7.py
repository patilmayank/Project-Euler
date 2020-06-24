target=3
primelist=[2]
while len(primelist)<10001:
  isprime=True
  for prime in primelist:
    if target%prime==0:
      isprime=False
      break
  if isprime:
    primelist.append(target)
  target+=1
print (primelist[10000])
