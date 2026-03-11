# Lab 5: Data Science Fundamentals with Pandas

This lab introduces data science fundamentals using the Pandas library. It covers data manipulation, cleaning, transformation, and analysis using DataFrames.

## Topics Covered
- Pandas DataFrames
- CSV file operations
- Data cleaning and preprocessing
- Handling missing values
- Duplicate detection and removal
- Outlier identification (IQR method)
- Data transformation
- Statistical analysis

---

## Questions and Solutions

### 1. CSV to DataFrame
**Question:** Load a CSV file into a DataFrame. Display column names, data types, and basic statistics.
**Solution:** [csv_to_DF.py](csv_to_DF.py)
**Data Files:** [students.csv](students.csv)

---

### 2. Display Head and Shape
**Question:** Display the first few rows and the shape of a DataFrame to understand its structure.

**Solution:** [headShape.py](headShape.py)

---

### 3. Detect and Remove Duplicates
**Question:** Detect duplicate rows in the dataset. Remove duplicates and verify the result.
**Solution:** [duplicateValues.py](duplicateValues.py)

---

### 4. Handle Missing Values
**Question:** Identify and fill missing values in a DataFrame using appropriate strategies.
**Solution:** [fillingMissing.py](fillingMissing.py)

---

### 5. Outlier Detection and Removal
**Question:** Identify outliers in the Marks column using the IQR method. Remove the outliers from the dataset.
**Solution:** [outliers.py](outliers.py)



### 6. Filter Data Based on Conditions
**Question:** Filter rows from a DataFrame based on specific conditions (e.g., students with marks > 90).
**Solution:** [conditionCSV.py](conditionCSV.py)



---

### 7. Data Transformation
**Question:** Transform data by applying operations on columns (e.g., scaling, normalization, creating new columns).

**Solution:** [transorm.py](transorm.py) / [transform.csv](transform.csv) / [cleanedTransform.csv](cleanedTransform.csv)
