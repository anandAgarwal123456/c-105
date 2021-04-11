import pandas as pd
import csv
import math

with open('marks.csv',newline='') as d:
    data = csv.reader(d)
    marksData = list(data)

marksData.pop(0)

totalMarks = 0
totalEntries = len(marksData)

for marks in marksData:
    totalMarks = totalMarks + float(marks[1])

mean = totalMarks/totalEntries
print(mean)

square = []

for marks in marksData:
    minus = float(marks[1]) - mean
    minus = minus**2
    square.append(minus)

print(square) 

sum =0

for marks in square:
    sum = sum + marks

number = sum/(totalEntries-1)

standardDeviation = math.sqrt(number)

print(standardDeviation)    

