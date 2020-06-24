target=3
n = input("Give me a number. I will give you the prime numbers up until that number, and I will give\n"
          "you the LCM of all consecutive integers up until that number")
primelist=[2]
while target<=int(n):
  isprime=True
  for prime in primelist:
    if target%prime==0:
      isprime=False
      break
  if isprime:
    primelist.append(target)
  target+=1
print (primelist)
product = 1
for i in primelist:
    for x in range(1,int(n)):
        if i**x <= int(n):
            product = product * i**(x)/i**(x-1)
print (product)
