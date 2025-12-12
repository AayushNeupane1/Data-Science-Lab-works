#  Student Marks Manager 
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute 
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks. 

student={
    "Aayush":[85,90,78],
    "Aastha":[88,76,92],
    "Smriti":[90,91,89]
}
s_avg=0

for name, marks in student.items():
    avg=sum(marks)/len(marks)
    s_avg+=avg
    if avg>=90:
        grade='A'
    elif avg>=80:
        grade='B'
    elif avg>=70:
        grade='C'
    else:
        grade='D'
    student[name]=(marks,avg,grade)
    print(f"{name}: Marks: {marks}, Average: {avg}, Grade: {grade}")


    #top 2 students 
