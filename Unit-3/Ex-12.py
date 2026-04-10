import json
import csv
with open("filejson.json","r") as json_file:
    v=json.load(json_file)
    print(v)
    # json_file.close()
with open("necs.csv","w",newline=' ') as csv_file:
    headers= v[0].keys()
    writer=csv.DictWriter(csv_file,fieldnames=headers)
    writer.writeheader()
    writer.writerows(v)