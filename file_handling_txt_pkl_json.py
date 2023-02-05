import os
print(os.getcwd()) # confirm text file is in your intended directory

# working with text files

# Reading from text files
# ----------------------------------------------------------------------------------------------------------------------

dog_handle = open('dogs.txt', 'r') # creating a connection to the txt with read mode 'r'
line = dog_handle.readline()
line_stripped = line.strip() # removes whitespace and return carriages
# When we're done reading from the file, we need to close it.
dog_handle.close()


# iterate through each line like so:
try:
  with open('dogs.txt', 'r') as infile: # the with statement will handle closing the file
    for line in infile:
      print(line.strip())
except FileNotFoundError:
    print("The file was not found.")


# Writing to text files
# ----------------------------------------------------------------------------------------------------------------------
cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll']

with open('cats.txt', 'w') as outfile: # note that we set the arguement to 'w' - write
  for cat in cat_list:
    outfile.write(cat + '\n') # newline is needed, otherwise you concatenate each string

# all values written to a textfile must be in string:
nums = range(11) # range 0 : 10
for x in nums:
    print(x)

with open('nums.txt', 'w') as outfile:
  for num in nums:
    outfile.write(str(num) + '\n')
# To append to an existing file instead of overwriting it, use 'a' instead of 'w' as the second argument for open().
# When appending to a file, you may need to handle a FileNotFoundError.


# Pickling
# ----------------------------------------------------------------------------------------------------------------------
# if we want to save lists, sets, dictionaries, etc, the pickle module would allow us to do so
# this would save us from writing each line to an outfile, and instead just write the entire data structure
import pickle

cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll', 'Tabby', 'Maine Coon', 'Cornish Rex']

# The file produced by pickling is not a text file and is not human readable.

# To write an object to a file, we use dump()
with open('cats.pkl', 'wb') as outfile: # wb : for writing in binary mode to a pkl file type
    pickle.dump(cat_list, outfile)

# read this file back in
with open('cats.pkl', 'rb') as infile:
    # Since we are reading from a binary file, we use 'rb' instead of 'r'.
  restored_list = pickle.load(infile) # To read an object from a file, we use load(),

# note that what was written, and what was read back in are not the same object
cat_list == restored_list    # true
cat_list is restored_list    # false

# if working entirely within python, pickling is very useful, however if transferring data
# between multiple languages then using JSON is more ideal.


# working with JSON files
# ----------------------------------------------------------------------------------------------------------------------
import json
cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll', 'Tabby', 'Maine Coon', 'Cornish Rex']
with open('cats.json', 'w') as outfile:  # just 'w' since it's a text file
  json.dump(cat_list, outfile)

with open('cats.json', 'r') as infile:  # just 'r' since it's a text file
  restored_list = json.load(infile)


#example 2:
jsonstring = r"""
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
"""

json_obj = json.loads(jsonstring)

for line in json_obj:
    print(line)

# write json object
with open('SuperSquad.json', 'w') as outfile:  # just 'w' since it's a text file
  json.dump(json_obj, outfile)

# read json object back in
with open('SuperSquad.json', 'r') as infile:
    squad = json.load(infile)

# if your json is one long string, use this to reformat it:
# http://jsonviewer.stack.hu/
