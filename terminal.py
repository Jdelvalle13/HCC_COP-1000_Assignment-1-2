def main():
    user_input = input("Enter a value: ")
    
    try:
        value = float(user_input)
        result = value * 10
        print("Result:", result)
    
    except ValueError:
        print("Error: Please enter a numerical value.")

if __name__ == "__main__":
    main()
