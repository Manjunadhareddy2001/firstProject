import csv

with open("hee.csv","w",newline='') as fp:
    a=csv.writer(fp)
    k=input("Enter values seperated byyyyyyy ,")
    a.writerow(k.split(","))
    