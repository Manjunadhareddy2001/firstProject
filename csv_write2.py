import csv
with open("hea.csv","w",newline='') as fp:
    a=csv.writer(fp)
    b=[[1,2,3],[4,5,6]]
    k=a.writerows(b)
    