# Ques 2. Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(fname,encoding="utf8"):
        with open(fname,encoding="utf8") as f:
                return Counter(f.read().split())

print("Frequency of words in the file :",word_count("Textfile.txt",encoding="utf8"))