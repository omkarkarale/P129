import csv

data1 = []
data2 = []

with open('brightest_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data1.append(i)

with open('dwarf_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data2.append(i)

header1 = data1[0]
brightest_stars_data = data1[1:]

header2 = data2[0]
dwarf_stars_data = data2[1:]

headers = header1 + header2

Stars_data = []

for i, row in enumerate(dwarf_stars_data):
    Stars_data.append(brightest_stars_data[i] + dwarf_stars_data[i])

with open('tempfile.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(Stars_data)

with open('tempfile.csv') as input, open('merged.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for i in csv.reader(input):
        if any(field.strip() for field in i):
            writer.writerow(i)

