
import json

#! JavaScript Object Notation
#! Python to JSON Conversions
#? Python            JSON
#  dict             object
# list, tuple       array
# str               string
# int, long, float  number
# True              true
# False             false
# None              null



person = {'name':'John', 'age':30, 'City':'New York', 'hasChildren':False, 'titles':["Engineer", 'Programmer']}
# separators=(';', '=')
personJSON = json.dumps(person, indent=4, sort_keys=True)

print(personJSON)

# Save json in file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# Converting JSON to Dictionary
new_person = json.loads(personJSON)
print(new_person)

# OR 
with open('person.json', 'r') as file:
    person = json.loads(file)
    print(person)