sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# list_of_words = sentence.split()
result = {item:len(item) for item in sentence.split()}

print(result)
