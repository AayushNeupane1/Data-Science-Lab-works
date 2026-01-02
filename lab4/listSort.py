# list to store the input of marks and sorting them in descending order

marks = []

print("Enter the marks seperated by space(Eg: 45 67 89 23): ")
marks=input()
marks=marks.split()
marks=[int(i) for i in marks]

marks.sort(reverse=True)
print("Sorted marks in descending order: ",marks)


# using sorted 

mark_sorted=[]

while True:
    try:
        mark=int(input("Enter the marks (or enter F to finish): "))
        mark_sorted.append(mark)

    except ValueError:
        break

mark_sorted=sorted(mark_sorted,reverse=True)
print("Sorted marks in descending order using sorted(): ",mark_sorted)