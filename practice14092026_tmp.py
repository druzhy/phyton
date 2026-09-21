def my_max (n , m):
    if n < m:
        return m
    return n

def my_sum(a,b):
    c = a + b + my_max( a, b)
    return c

#n = float(input())
#m = float(input())
#res = my_sum(n, m)
res = my_sum (4 , 6)
print (res)