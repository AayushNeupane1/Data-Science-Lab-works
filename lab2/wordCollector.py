# 2. Unique Words Collector 
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them 
# alphabetically, and count the total number of unique words.

par = input("Enter the paragraph: ")

words = par.lower().split()

unique_words = []
frequency = []

for w in words:
    if w not in unique_words:
        unique_words.append(w)
        count = 0
        for i in words:
            if i== w:
                count += 1

        frequency.append(count)

print("Word frequency:")
for i in range(len(unique_words)):
    print(unique_words[i], ":", frequency[i], "ASCII:", [ord(c) for c in unique_words[i]])



unique_words = set(words)
unique_words = sorted(unique_words)
count_unique = len(unique_words)

print("sorted:", unique_words)
print("Total number of unique words:", count_unique)
