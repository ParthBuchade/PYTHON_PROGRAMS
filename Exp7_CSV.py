
import csv
from dataclasses import fields
from fileinput import filename
from stat import filemode

file = open('E:\\Book1.csv')
print(file)
csvreader = csv.reader(file)
print(csvreader)

fields = ['name','age','CGPA']

rows = [['parth','20','8.8'],
        ['pratik','20','9.0'],
        ['om','19','9.4']]
filename = "Book1.csv"

# writing to csv file
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

