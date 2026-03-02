# User se input lene ke liye
original_str = input("Apna text likhein: ")

# Reverse karne ke liye khali string
reversed_str = ""

# Loop har character par chalega
for char in original_str:
    # Character ko hamesha aage (prefix) jodein
    reversed_str = char + reversed_str

print("Reversed text hai:", reversed_str)
