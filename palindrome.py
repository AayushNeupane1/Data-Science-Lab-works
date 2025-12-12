## Write a program to check if a given string is palindrome 

str=input("Enter the string").lower()
r_str=""
for char in str:
    # print(char)
    r_str=char+r_str    
def palindrome_(str,r_str):
    if str==r_str:
        print(f"The given {str} is palindrome")
    else:
        print("Not palindrome")

palindrome_(str,r_str)
    
    
    