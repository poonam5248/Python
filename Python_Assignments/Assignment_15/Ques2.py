''' Ques 2. Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought
some better butter, To make the bitter butter better".'''


import re
text='''Betty bought a bit of butter, But the butter was so bitter,So she bought some better butter,
 To make the bitter butter better.'''

p = re.compile(r"\b[bB]\w+")
result=p.findall(text)
print(result)