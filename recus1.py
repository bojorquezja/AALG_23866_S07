def suma_It_Av(n):
    s = 0
    for x in range(1,n+1):
        s += x
    return s

def suma_Rc_Av(n, x = 1):
    if x == n:
        return x
    else:
        return x + suma_Rc_Av(n, x+1)
   

def suma_It_Re(n):
    s = 0
    for x in range(n,1-1,-1):
        s += x
    return s

def suma_Rc_Re(x):
    if x == 1:
        return x
    else:
        return x + suma_Rc_Re(x-1)
    




print("Iterativo Avance: ", suma_It_Av(3))
print("Recursivo Avance: ", suma_Rc_Av(3))
print("Iterativo Retroceso: ", suma_It_Re(3))
print("Recursivo Retroceso: ", suma_Rc_Re(3))