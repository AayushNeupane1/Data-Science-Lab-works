# Use a list comprehension to create a new list containing only the even numbers between
# 1 and 20, demonstrating a more concise and readable alternative to traditional loops..

even_list=[i for i in range(1,21) if i%2==0]
print("Even numbers between 1 and 20:", even_list)

#using range
evenlist_range=list(range(2,21,2))
print("Even numbers between 1 and 20 using range:", evenlist_range)