phrase = "Hello World from Python"
check = "aeiouAEIOU"

vowel_total = sum(
    1 for element in phrase
    if element in check
)

print("Count:", vowel_total)
