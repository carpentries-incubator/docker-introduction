
import json
import argparse

legal_drinking_age = 18
progargs = argparse.ArgumentParser(
    description="Reads a json file of names and ages and prints out the people who are not allowed to drink")
progargs.add_argument('-i', '--input',
                      required=True,
                      type=argparse.FileType('r'),
                      help='Input json file')
OPTIONS = progargs.parse_args()
print(f"Reading in json file '{OPTIONS.input.name}'")
people = json.load(OPTIONS.input)

for name, age in people.items():
    if age < legal_drinking_age:
        print(f"{name} is not allowed to drink because they are only {age} years old!")
