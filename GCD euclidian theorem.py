#finding gcd using euclidian theorem
def gcd(r1,r2):
    print("Q  || r1   ||  r2   ||  r  ||")
    while(r2>0):
        q=int(r1/r2)
        r=r1%r2

        print(f"{q}  ||  {r1}  ||  {r2}   ||  {r}  ||")
        r1=r2
        r2=r
    print(f"\nGcd:{r1}\n")

if __name__=="__main__":
    gcd(63,84)