#finding gcd using euclidian theorem
def gcd(r1,r2):
    print("Q  || r1   ||  r2   ||  r  ||  s1  ||  s2  ||  s  ||  t1  ||  t2  ||  t ||")
    s1=1
    s2=0
    t1=0
    t2=1
    while(r2>0):
        q=int(r1/r2)
        r=r1%r2
        s=s1-s2*q
        t=t1-t2*q
        print(f"{q}  ||  {r1}  ||  {r2}   ||  {r}  ||  {s1}  ||  {s2}  ||  {s}  ||  {t1}  ||  {t2}  ||  {t}")
        r1=r2
        r2=r
        s1=s2
        s2=s
        t1=t2
        t2=t
        s=0
        t=0
    print(f"\nGcd:{r1}\n")
    print(f"s:{s1}\nt:{t1}")

if __name__=="__main__":
    x=int(input("Enter greater no:\n"))
    y=int(input("Enter smaller no:\n"))
    gcd(x,y)
    print(f"Gcd:{x}s+{y}t")