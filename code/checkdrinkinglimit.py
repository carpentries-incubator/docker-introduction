
import json

legal_drinking_age = 18

with open("ages.json", "r") as agefile:
    people = json.load(agefile)

    for name,age in people.items():
        if age < legal_drinking_age:
            print(f"{name} is not allowed to drink because they are only {age} years old!" )
