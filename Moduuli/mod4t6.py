N=1000000

n=0
toistot=0
while toistot < N:
    x=0
    y=0
    if(x*x+y*y<1):
        n+=1
pi=4*n/ N
print(f"Piin likiarvo on {pi}")
