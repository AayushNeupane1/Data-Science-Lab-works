# Data Science Lab

A comprehensive Python learning lab covering fundamentals to advanced concepts.

## Overview

This repository contains all the lab activities required for data science, starting from Python basics, advanced Python, file handling, data types, and fundamentals of data science.



## Lab 1: Basics of Python, Data Types, Control Structures, Functions and Loop

Covers the basics of Python, conditions, input handling, functions, and control structures.

### Questions and Objectives

1. **Sum of Two Numbers**
   - Write a program that takes two numbers as input from the user, and print their sum.
   - File: [lab1/add.py](lab1/add.py)

2. **Palindrome Checker**
   - Write a program that checks if a given string is palindrome.
   - File: [lab1/palindrome.py](lab1/palindrome.py)

3. **Prime Numbers**
   - Write a program that prints all prime numbers up to a given number 'n'.
   - File: [lab1/prime.py](lab1/prime.py)

4. **Fibonacci Series**
   - Write a python program that prints the Fibonacci series up to n terms.
   - File: [lab1/fibo.py](lab1/fibo.py)

5. **Greatest Common Divisor (GCD)**
   - Define a function that takes two numbers as arguments, and returns their greatest common divisor (GCD).
   - File: [lab1/gcd.py](lab1/gcd.py)

6. **Even or Odd**
   - Write a program that checks if a given number is even or odd.
   - File: [lab1/oddEven.py](lab1/oddEven.py)

7. **Largest Number in List**
   - Write a program that takes a list of numbers as input, and returns the largest number in the list.
   - File: [lab1/largest.py](lab1/largest.py)

8. **Leap Year Checker**
   - Write a program that checks if a year is a leap year.
   - File: [lab1/leap.py](lab1/leap.py)

9. **Temperature Conversion**
   - Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and Kelvin, based on the choice of user.
   - File: [lab1/tempt.py](lab1/tempt.py)

10. **Multiple Files with Separate Functions**
    - Location: [lab1/multiple_files/](lab1/multiple_files/)
    
    a. **Birth Year and Leap Year Checker**
       - A program that takes the age of a user, and gives their birth year, and if birth year was a leap year.
       - File: [lab1/multiple_files/birth_year.py](lab1/multiple_files/birth_year.py)
    
    b. **Body Mass Index (BMI) Calculator**
       - A program that computes the Body Mass Index (BMI) of a user, taking their height and weight as input.
       - The program should allow the user to enter their height in either feet/inches or centimeters and their weight in either kilograms or pounds.
       - Extend the program to convert BMI into a category based on standard criteria:
         - **Underweight**: BMI < 18.5
         - **Normal weight**: BMI 18.5 - 24.9
         - **Overweight**: BMI 25 - 29.9
         - **Obese**: BMI ≥ 30
       - File: [lab1/multiple_files/bmi.py](lab1/multiple_files/bmi.py)
    
    c. **Army Entrance Eligibility Checker**
       - A program that checks if a user is eligible for army entrance based on their BMI and age.
       - The eligibility criteria are as follows:
         - Age must be between 18 and 40 years.
         - BMI must be within the range of 18.5 to 29.9.
       - File: [lab1/multiple_files/army.py](lab1/multiple_files/army.py)

---

## Lab 2: Data Structures in Python

Covers data structures including lists, dictionaries, and sets. Focuses on manipulation, analysis, and organization of data.

### Questions and Objectives

1. **Movie Ratings Analyzer**
   - Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...].
   - Compute the average rating.
   - Find the highest-rated movie.
   - List all movies with rating above the average.
   - File: [lab2/movie.py](lab2/movie.py)

2. **Unique Words Collector**
   - Take a paragraph input from the user.
   - Split it into words, remove duplicates, sort them alphabetically.
   - Count the total number of unique words.
   - File: [lab2/wordCollector.py](lab2/wordCollector.py)

3. **Student Marks Manager**
   - Store student names as keys and marks (list of integers) as values in a dictionary.
   - Compute each student's average and grade (A/B/C/D).
   - Print the top 2 students based on average marks.
   - File: [lab2/studentsmark.py](lab2/studentsmark.py)

4. **Inventory Tracker**
   - Manage a small store inventory like {"apple": 10, "banana": 5, "milk": 2}.
   - Program should allow:
     - Adding new items
     - Selling items (subtract quantity)
     - Print items that are low in stock (<3)
   - File: [lab2/inventoryTracker.py](lab2/inventoryTracker.py)

5. **Word Reverser Game**
   - Ask the user for a list of words.
   - Reverse each word only if its length is even.
   - Print the new list of words after processing.
   - File: [lab2/wordReverser.py](lab2/wordReverser.py)

---

## Lab 3: File Handling & Exception Handling

Covers file handling operations and exception handling for robust file operations with different file formats.

### Questions and Objectives

1. **Basic File Read & Write**
   - Create a text file and write multiple lines into it.
   - Read the contents of the file and display them on the screen.
   - Handle the case where the file does not exist using try-except.
   - File: [lab3/basicfileHandling.py](lab3/basicfileHandling.py)

2. **File Processing with Exception Handling**
   - Reads numbers from a text file (one number per line).
   - Ignores invalid entries using exception handling.
   - Calculates and displays the sum and average of valid numbers.
   - File: [lab3/fileProcessing.py](lab3/fileProcessing.py)

3. **CSV File Handling**
   - Read data from a CSV file containing student records (roll number, name, marks).
   - Display all student records.
   - Handle file-related and data conversion errors using try-except.
   - File: [lab3/csv.py](lab3/csv.py)

4. **Writing and Reading JSON Data**
   - Stores student details (ID, name, and marks) in a JSON file.
   - Reads the JSON file and displays the student information.
   - Handles exceptions related to file access and JSON decoding.
   - File: [lab3/jsonfile.py](lab3/jsonfile.py)

5. **Menu-Driven File Operations**
   - Write data to a file.
   - Read data from a file.
   - Append data to a file.
   - Handle invalid user input and file errors using exception handling.
   - File: [lab3/menuDriven.py](lab3/menuDriven.py)

### Data Files
- [lab3/qst1.txt](lab3/qst1.txt)
- [lab3/qst2.txt](lab3/qst2.txt)
- [lab3/qst3.csv](lab3/qst3.csv)
- [lab3/qst4.json](lab3/qst4.json)
- [lab3/qst5.txt](lab3/qst5.txt)

---

## Lab 4: Advanced Python Concepts

Covers advanced Python concepts including generators, list comprehensions, regular expressions, and functional programming.

### Files
- [lab4/generator.py](lab4/generator.py)
- [lab4/listComprehension.py](lab4/listComprehension.py)
- [lab4/listSort.py](lab4/listSort.py)
- [lab4/randomStudent.py](lab4/randomStudent.py)
- [lab4/regex.py](lab4/regex.py)
- [lab4/zipFunction.py](lab4/zipFunction.py)


