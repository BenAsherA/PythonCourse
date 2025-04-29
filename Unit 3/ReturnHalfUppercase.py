def uppercase_last_half(string):
    lowercase_half = string[:len(string) // 2]
    uppercase_half = string[len(string) // 2:].upper()
    return lowercase_half + uppercase_half

user_input = input("Please enter a string: ")
print(uppercase_last_half(user_input))