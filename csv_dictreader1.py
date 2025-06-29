import csv

with open("manju.csv","r") as fp:
    a=csv.DictReader(fp)
    b=list(a)
    print(b)