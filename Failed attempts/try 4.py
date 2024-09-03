myvalue = hello
try:
    print(f"The calculated value is: {float(myvalue) * 10}")
except ValueError:
    print("Error: myvalue is not a number.")