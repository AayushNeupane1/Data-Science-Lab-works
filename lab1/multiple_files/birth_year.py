#wap that takes the age of the user and return the birth year and also checks if the year is leap year or not

import datetime as d
age=int(input("Enter your age:"))

def  birth_yr(age):
    current_yr=d.datetime.now().year
    birth_yr=current_yr-age
    if (birth_yr%4==0 and birth_yr%100!=0 ) or  birth_yr%400==0:
        print(f"Your birth year {birth_yr} is leap year")
    
    else:
        print(f"Your birth year {birth_yr} is not  a leap year")

birth_yr(age)