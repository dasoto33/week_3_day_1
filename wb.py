# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#input striing and output string


def pascal_case(string_input):
    lst = string_input.split("-")
    if "_" in string_input:
        lst = string_input.split("_")
    for i, a in enumerate(lst):
        if i != 0:
            lst[i] = a[0].capitalize() + a[1:]
    return "".join(lst)

print(pascal_case("matrix"))
    

        
