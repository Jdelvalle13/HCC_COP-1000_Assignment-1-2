value = abcde

try:
    numeric_value = float(value)

    result = numeric_value * 10
    print (result)

except ValueError:
    print("Error: Please enter a numerical value.")