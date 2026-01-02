# Create a generator function using the yield keyword that produces numbers from 1 to
# 5 one by one to illustrate how lazy evaluation can save memory when dealing with large
# datasets.

def number_generator(n):
    for i in range(1,n+1):
        yield i

number=number_generator(5)
print("Generated numbers from 1 to 5:")
for num in number:
    print(num)
    