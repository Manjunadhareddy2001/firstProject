import csv
with open("hea.csv","r") as fp:
    a=csv.reader(fp)
    b=list(a)
    print(b)