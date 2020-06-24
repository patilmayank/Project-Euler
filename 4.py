maxnum = 0
for x in range(100,1000):
  for i in range(100,x):
    product=i*x
    productstring=str(product)
    if productstring==productstring[::-1]:
      maxnum = max(maxnum,product)
print(maxnum)
