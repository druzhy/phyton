def my_abs (a):
    if a < 0:
        c = -a
    else:
        c = a
    return c

#def my_abs (a):
#    if a < 0:
#        return -a
#    else:
#        return a

#def my_abs (a):
#    if a < 0:
#        return -a
#    return a

n = float(input())
res = my_abs(n)
print(res)