
import csv
import json
import datetime
import argparse

progargs = argparse.ArgumentParser(
    description="Reads a csv file of names and birthdays and writes a json file with the names and current ages")
progargs.add_argument('-i', '--input',
                      required=True,
                      type=argparse.FileType('r'),
                      help='Input csv file')

progargs.add_argument('-o', '--output',
                      required=True,
                      type=argparse.FileType('w'),
                      help='Output json')

OPTIONS = progargs.parse_args()

# taken from https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


ages = {}
print "Reading in csv file '{}'".format(OPTIONS.input.name)
reader = csv.DictReader(OPTIONS.input, delimiter=',',)
for line in reader:
    name = line["Names"]
    birthday = datetime.datetime.strptime(line["Birthday"], "%m/%d/%Y")
    age = calculate_age(birthday)
    ages[name] = age

print "Writing to json file '{}'".format(OPTIONS.output.name)
json.dump(ages, OPTIONS.output)
