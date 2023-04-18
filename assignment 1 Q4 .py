def first_non_repeated_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string1 = "aabbccddeeff"
print(first_non_repeated_char(string1)) 

string2 = "aabbccddee"
print(first_non_repeated_char(string2))

string3 = "abcdefgabc"
print(first_non_repeated_char(string3)) 
