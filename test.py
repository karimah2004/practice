#first, figure out how many users are making more than one review
#find out how many users are making reviews in locations they did not check into
#print out stores with each review- 1-5

import json

# Open the JSON file for reading
with open('user_name.json', 'r') as json_file:
    data = json.load(json_file)

# Create a list to store seen objects
seen_objects = []

# Iterate through the objects in the JSON data
for obj in data:
    # Convert the object to a JSON string for comparison
    obj_str = json.dumps(obj, sort_keys=True)
    
    # Check if the object string has been seen before
    if obj_str in seen_objects:
        print("Duplicate Object:")
        print(obj)
    else:
        # Add the object string to the list of seen objects
        seen_objects.append(obj_str)
#testing 
