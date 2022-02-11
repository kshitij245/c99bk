from base64 import standard_b64encode
import math 
import csv

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

squared_List=[]
for r in data:
    a=int(r)-mean(data)
    a=a**2
    squared_List.append(a)

sum=0
for i in squared_List:
    sum=sum+i

result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)

