def compute_sum(value1, value2):
    temp_result = value1 + value2
    return temp_result


def ask_version_three():
    print("Preparing inputs...")
    
    num1 = 0
    num2 = 1
    
    print("Calling helper function...")
    
    final_value = compute_sum(num1, num2)
    
    print("Computation complete.")
    
    print("Result:", final_value)
    print("Execution finished.")


if __name__ == "__main__":
    ask_version_three()
