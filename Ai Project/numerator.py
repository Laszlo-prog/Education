try:

    numerator = int(input("Enter the number: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"The result is : { result}")

except ZeroDivisionError:
    print("Error: Please enter a valid integer.")

except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexception error occurred: {e}")

finally:
    print("Thank you for a using our calculator.")