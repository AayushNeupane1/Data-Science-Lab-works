# Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.

import random as r

student=[]
print("Enter the names of six students separated by space(Eg: A B C D E F )): ")
student=input().split()
volunteers=r.sample(student,3)
print("Selected Volunteers for presentation are: ",volunteers)