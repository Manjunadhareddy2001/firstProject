import csv
head=["one","two","three"]
with open("manju.csv","w",newline='') as fp:
    a=csv.DictWriter(fp,fieldnames=head)
    values=[{"one":1,"two":2,"three":3},{"one":4,"two":5,"three":6}]
    a.writeheader()
    a.writerows(values)