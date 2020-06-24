fib=[1,2]
totalfib=2
for x in range(31):
  fib.append(fib[-1]+fib[-2])
  if fib[-1]%2==0:
     totalfib+=fib[-1]
print(totalfib)
print(fib)
