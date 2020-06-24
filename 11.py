target=3
primelist=[2]
n=2000000
while target<n:
    isprime=True
    for i in primelist:
        if i>n**0.5:
            break
        if target%i==0:
            isprime=False
            break
    if isprime:
        primelist.append(target)
    target+=1
print(sum(primelist))
