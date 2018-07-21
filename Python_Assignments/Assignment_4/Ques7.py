# Ques 7. Count the number of occurrence of each letter in word "MISSISSIPPI".
#  Store count of every letter with the letter in a dictionary.

l=list("mississippi")
d={}
d['m']=l.count('m')
d['i']=l.count('i')
d['p']=l.count('p')
d['s']=l.count('s')

print(d)
