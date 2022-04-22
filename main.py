import math
n = input("n= ")
k = input("k= ")
if n == k:
    print(1)
elif k == 1:
    print(n)
elif k > n:          
    print(0)
else:                
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n-k)  
    div = a // (b * c)
    print(div)  