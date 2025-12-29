# 2. File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers

# def process_file(filename):
#     numbers = []
    
#     try:
#         with open(filename,'r') as file:
#             for line in file:
#                 try:
#                     num = float(line.strip())
#                     numbers.append(num)
#                 except ValueError:
#                     print(f"Skipping invalid entry: {line.strip()}")
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return
    
#     if numbers:
#         total = sum(numbers)
#         average = total / len(numbers)
#         print(f"Sum: {total}")
#         print(f"Average: {average}")
#     else:
#         print("No valid numbers found.")


# process_file('qst2.txt')

import re

try:
    sum = 0
    length = 0
    with open("q2.txt", "r") as f:
        for i in f.readlines():
            match = re.search(r"\d+", i)
            if not match:
                continue
            i = match.group()
            try:
                sum += float(i) if "." in i else int(i)
                length += 1
            except ValueError:
                continue
except FileNotFoundError:
    print("File not found." )

print(f"Sum : {sum}")
print(f"Average: {sum/length}")