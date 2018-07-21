# Ques 4. Extract month from the time.


from datetime import datetime

#d=datetime.date.today()
d=datetime.now()
print(d)
#print(d.month)
print("Month:",d.strftime("%B"))