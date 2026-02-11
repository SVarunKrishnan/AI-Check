def ask_version_two():
    print("Initializing data...")
    
    data = {
        "first": 0,
        "second": 1
    }
    
    print("Dictionary created.")
    
    x = data.get("first")
    y = data.get("second")
    
    print("Values extracted:", x, y)
    
    result = x + y
    
    print("Performing addition...")
    
    print("Result:", result)
    print("Done.")
    

if __name__ == "__main__":
    ask_version_two()
