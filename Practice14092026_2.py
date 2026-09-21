def my_max (n , m):
    if n < m:
        return m
    return n

n = float(input())
m = float(input())
res = my_max(n , m)
print(res)