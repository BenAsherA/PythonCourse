def replace_except_first_letter(string, letter):
    if string:
        string_after_replacements = string[1:].replace(string[0],letter)
        return string[0] + string_after_replacements
    return ''

matching_letters_replaced_by_e = replace_except_first_letter(input("Please enter a string: "),'e')
print(matching_letters_replaced_by_e)