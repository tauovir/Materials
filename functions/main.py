
def count1(n):
    print(n)
    if n>10:
        return

    count1(n+1)

def factorial(n):
    if n <=1:
        return 1
    else:
        print(f"{n}*{n-1}= {n*(n-1)}")
        fact =  n * factorial(n-1)
        print("fact:",fact)
    return fact

x = factorial(5)
print(x)