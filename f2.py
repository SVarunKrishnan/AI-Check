sentence = "Hello World from Python"
vowel_letters = "aeiouAEIOU"

matches = [letter for letter in sentence if letter in vowel_letters]
total = len(matches)

print("Vowel count is:", total)
