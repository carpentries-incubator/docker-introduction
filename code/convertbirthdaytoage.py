
import csv
import json
import datetime
import os

# taken from https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

ages={}
with open(r'data_birthday.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=',',)
    for line in reader:
        name = line["Names"]
        birthday = datetime.datetime.strptime(line["Birthday"],"%m/%d/%Y")
        age= calculate_age(birthday)
        ages[name]=age

with open('ages.json', 'w') as f:
    json.dump(ages, f)
        



