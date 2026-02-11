def ask_version_four():
    print("Starting process...")
    
    a = 0
    b = 1
    
    counter = 0
    values = [a, b]
    
    result = 0
    
    while counter < len(values):
        result += values[counter]
        counter += 1
    
    print("Loop finished.")
    
    print("Result:", result)
    print("Process complete.")


if __name__ == "__main__":
    ask_version_four()
