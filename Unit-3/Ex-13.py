import csv
with open("necs.csv","r") as file:
    p=csv.reader(file)
    # print(p)
    row=0
    for i in p:
        row+=1

    print(row)
