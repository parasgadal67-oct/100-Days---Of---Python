# creating a user name with lower(), withoutspace, and combining the city length to it.
username = "PARAS GADAL"
city = "Dehradun"

print(len(city))
print(username.lower().replace(" ", "") + str(len(city)))