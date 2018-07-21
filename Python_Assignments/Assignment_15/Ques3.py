''' Ques 3. Split the following irregular sentence into words
sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence".'''


import re
irregular_sentence="A,very very;irregular_sentence"


p = re.compile(r"[^A-Za-z0-9]")
result=p.sub(" ",irregular_sentence)
print(result)