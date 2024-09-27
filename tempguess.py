def get_temperature_recommendation(temperature):
    if temperature < 0:
        return "It's freezing! Wear a heavy coat, gloves, and a hat."
    elif temperature < 10:
        return "It's very cold. Wear a warm coat and bring a scarf."
    elif temperature < 20:
        return "It's chilly. A light jacket should be fine."
    elif temperature < 30:
        return "It's warm. A t-shirt and jeans are perfect."
    else:
        return "It's hot! Wear light clothes and don't forget sunscreen."

# Get user input
temp = input("Enter the current temperature in Celsius: ")

# Convert input to float
try:
    temp = float(temp)
    # Get and print the recommendation
    recommendation = get_temperature_recommendation(temp)
    print(f"Temperature: {temp}°C")
    print(f"Recommendation: {recommendation}")
except ValueError:
    print("Please enter a valid number for the temperature.")
