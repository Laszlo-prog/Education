import pandas as pd
import os


#Create a fruit list!
fruits = ["apple", "orange", "grape", "strawberry","lime", "tomate"]
print("======Add item in fruits list =======")

# Add an item to the end of the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Insert an item at a specific position
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']

# Add multiple items to the list
fruits.extend(["mango", "pineapple"])
print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange', 'mango', 'pineapple']

print("=========Remove item section=========")

#remove the first specific fruits
fruits.remove("banana")
print(fruits)
#remove an item by index
removed_fruits = fruits.pop(1)
print(f"Removed: {removed_fruits}")
print(fruits)
#removed last item on list

last_fruits = fruits.pop()
print(f"Removed: {last_fruits}")
print(fruits)


# Delete an item by index using 'del'
del fruits[0]
print(fruits)  # Output: ['grape']

# Clear the entire list
fruits.clear()
print(fruits)  # Output: []