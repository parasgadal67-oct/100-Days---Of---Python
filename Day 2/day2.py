# creating a name formatter 
name = "paras gadal"
age = 23
city = "dehra dun"
hobby = "Singing"
phone_number = int( 8394833407)
goal = "to become a ai engineer"

# using f string and upper method to format the name
print(f"My name is {name.upper()}.")
#using replace() to replace number with letters
print(f"I am {str(age).replace('23', 'Twenty three')} years old.")
#using title () to capitalize the first letter 
print(f"I live in {city.title()}.")
#using lower() to convert to lowercase
print(f"My hobby is {hobby.lower()}.")
#usind find() and  To find the index of specific character
print(f"My phone number is {str(phone_number)} and the index of '3' is {str(phone_number).find('3')}.")
#using len() to find length of the goal
print(f"My goal is {goal} and the length of my goal is {len(goal)} characters.")