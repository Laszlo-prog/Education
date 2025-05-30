# Create a list
shopping_list = ["bread", "milk"]

# Add items
shopping_list.append("eggs")
shopping_list.insert(1, "butter")
shopping_list.extend(["juice", "cheese"])

print("Current List:", shopping_list)
# Output: Current List: ['bread', 'butter', 'milk', 'eggs', 'juice', 'cheese']

# Remove items
shopping_list.remove("butter")
shopping_list.pop(2)  # Removes 'eggs'
del shopping_list[0]  # Removes 'bread'

print("Updated List:", shopping_list)
# Output: Updated List: ['milk', 'juice', 'cheese']