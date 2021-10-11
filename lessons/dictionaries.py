"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key (lookup)
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update/ reassign a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Demonstration of dictionary literals
# schools = {}  # same as dict()

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 21650
}

# What happens when a key doesnt exist
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")