#that will print fibonacci series upto n term 

n=int(input("Enter the number of terms you want in fibonacci series"))

def fib_(n):
    if n<=1:
        return n 
    else:
        return fib_(n-1)+fib_(n-2)


for i in range(n):
    print(fib_(i))

