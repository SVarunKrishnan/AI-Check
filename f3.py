def calculate_vowels(data):
    vowel_set = "aeiouAEIOU"
    result = 0
    
    for item in data:
        if item in vowel_set:
            result += 1
            
    return result

print("Number of vowels:", calculate_vowels("Hello World from Python"))
