# create a factorial by two different function

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

def print_fatc(n):
    result=fact(n)
    print(f"the farctorial of {n} is {result}")


print_fatc(5)