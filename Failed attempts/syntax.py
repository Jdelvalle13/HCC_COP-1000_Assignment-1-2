value = 67o

try:
    if isinstance(value,(float, int)):
        result = value * 10
        print (result)

    else:
        print("Error: Please enter a numerical value")

except: SyntaxError
