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

---

## Lab 5: Data Science Fundamentals with Pandas

Covers data science fundamentals using the Pandas library for data manipulation, cleaning, transformation, and analysis.

### Questions and Objectives

1. **CSV to DataFrame**
   - Load a CSV file into a DataFrame.
   - Display column names, data types, and basic statistics.
   - File: [lab5/csv_to_DF.py](lab5/csv_to_DF.py)

2. **Display Head and Shape**
   - Display the first few rows and the shape of a DataFrame.
   - Understand the structure and dimensions of the dataset.
   - File: [lab5/headShape.py](lab5/headShape.py)

3. **Detect and Remove Duplicates**
   - Detect duplicate rows in the dataset.
   - Remove duplicates and verify the result.
   - File: [lab5/duplicateValues.py](lab5/duplicateValues.py)

4. **Handle Missing Values**
   - Identify missing values in a DataFrame.
   - Fill missing values using appropriate strategies (mean, median, forward fill, etc.).
   - File: [lab5/fillingMissing.py](lab5/fillingMissing.py)

5. **Outlier Detection and Removal**
   - Identify outliers in the Marks column using the IQR (Interquartile Range) method.
   - Remove the outliers from the dataset.
   - **IQR Method**: `IQR = Q3 - Q1`, `Lower Bound = Q1 - 1.5*IQR`, `Upper Bound = Q3 + 1.5*IQR`
   - File: [lab5/outliers.py](lab5/outliers.py)

6. **Filter Data Based on Conditions**
   - Filter rows from a DataFrame based on specific conditions.
   - Example: Select students with marks greater than 90.
   - File: [lab5/conditionCSV.py](lab5/conditionCSV.py)

7. **Data Transformation**
   - Transform data by applying operations on columns.
   - Create new derived columns, apply scaling, normalization, etc.
   - File: [lab5/transorm.py](lab5/transorm.py)

### Data Files
- [lab5/students.csv](lab5/students.csv) - Student records with names, ages, and marks
- [lab5/transform.csv](lab5/transform.csv) - Original data for transformation
- [lab5/cleanedTransform.csv](lab5/cleanedTransform.csv) - Cleaned and transformed data

### Key Pandas Operations
- `pd.read_csv()` - Load CSV files
- `df.head()`, `df.shape` - Data exploration
- `df.describe()` - Statistical summary
- `df.duplicated()`, `df.drop_duplicates()` - Handle duplicates
- `df.isnull()`, `df.fillna()` - Handle missing values
- `df.quantile()` - Calculate quartiles for outlier detection
- Boolean indexing - Filter data based on conditions

---

## Lab 6: Statistical Analysis and Data Visualization

A Jupyter notebook covering statistical concepts including covariance, correlation, and data visualization using Matplotlib and Seaborn.

### Topics Covered
- Covariance calculation and interpretation
- Correlation coefficient analysis
- Statistical measures (mean, variance)
- Data visualization with Matplotlib
- Advanced plotting with Seaborn
- Scatter plots, regression plots, and jointplots
- Understanding relationships between variables

### Questions and Objectives

1. **Hours Studied vs Marks Scored**
   - Create a dataset of hours studied and marks scored for 10 students
   - Calculate the covariance between the two variables
   - Plot the data using a scatter plot

2. **Correlation Analysis**
   - Using the same dataset, compute the correlation coefficient
   - Interpret whether the relationship is positive, negative, or weak
   - Visualize it using a seaborn regression plot

3. **Temperature and Ice-Cream Sales**
   - Generate a dataset of daily temperature and ice-cream sales
   - Find the covariance between temperature and sales
   - Plot the relationship using a scatter plot

4. **Covariance vs Correlation Comparison**
   - Calculate the correlation for the temperature vs ice-cream sales dataset
   - Compare the covariance and correlation values
   - Explain why correlation is easier to interpret

5. **Random Data Relationship**
   - Create two random numerical datasets with no clear relationship
   - Compute their covariance and correlation
   - Visualize them using a scatter plot and observe the pattern

6. **Height and Weight Analysis**
   - Load a small dataset with height and weight values
   - Calculate mean, variance, covariance, and correlation
   - Plot the data using a seaborn jointplot

7. **Linear vs Random Comparison**
   - Create a dataset where one variable increases linearly and another increases randomly
   - Compute covariance and correlation
   - Plot both cases and compare the results

### Key Libraries
- **NumPy** - Numerical computing and random data generation
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Basic plotting and visualization
- **Seaborn** - Statistical data visualization

### Key Statistical Concepts
- **Covariance**: Measures how two variables change together (units dependent)
- **Correlation**: Standardized measure of linear relationship (-1 to 1)
- **Positive Correlation**: Both variables increase together
- **Negative Correlation**: One increases while the other decreases
- **No Correlation**: Variables show no linear relationship

### Visualization Types
- **Scatter Plot** - Shows relationship between two variables
- **Regression Plot** - Scatter plot with fitted regression line
- **Joint Plot** - Combines scatter plot with marginal distributions

**File:** [lab6.ipynb](lab6.ipynb)

---
