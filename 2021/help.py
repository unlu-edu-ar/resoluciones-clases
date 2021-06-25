## Primera comparacion 

def f(x):
    print("A")
    if (x == 0):
        print("B")
    print("C")

f(0)
# f(1)

def abs3(n):
    if (n < 0):
        return -n
    return n

##Explicacion de condiciones anidadas

def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if (x == 1):
            print("E", end="")
        else:
            print("F", end="")
    print("G")

# f(0)
# f(1)
# f(2)

def abs5(n):
    if (n >= 0):
        return n
    else:
        return -n