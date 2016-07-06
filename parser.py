import csv
import os

def googleSearch(input):
   from google import search
   for url in search(input):
       return url
       break

writer = csv.writer(open("out.csv", "wb"), delimiter=',', quoting=csv.QUOTE_NONE, escapechar=None)
reader = csv.reader(open("parse-me.csv", "rb"))
header = reader.next()
writer.writerow(header)

for row in reader:
   row[1] = str(googleSearch(row[0]));
   writer.writerow(row)
os.rename('out.csv', 'parse-me.csv')


# notes - pip install google
