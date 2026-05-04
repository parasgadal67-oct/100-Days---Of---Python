# dictionary of countries and their capitals
countries = {"Nepal" : "Kathmandu",
             "India" : "Delhi",
             "USA" : "Washington DC",
             "Japan" : "Tokyo"}

print(countries.get("Nepal"))
# updating the dictionary by adding new country and its capital
capitals = countries.update({"Germany" : "Berlin",
                            "United Kingdom" : "London"})
print(countries)

# extracting the key() and values() from the dictionaries
keys = countries.keys()
print(keys)
values = countries.values()
print(values)

#removing the one character from dictionary .pop()
countries.pop("USA")
print(countries)

# finding the value in dictionary

print("Germany" in countries)
