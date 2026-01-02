# 6. Given a list of student names and a list of their corresponding scores, use the zip()
# function to pair them together and then apply the reduce() function from the
# # functools module to calculate the total sum of all scores

from functools import reduce

students = ["Aayush", "Aastha", "Smriti", "Samiksha"]
scores =[85,90,78,92]
paired_list=zip(students,scores)
total_score=reduce(lambda x,y:x+y,scores)
print("Paired list of students and their scores:",list(paired_list))
print("Sum of scores of all students: ",total_score)