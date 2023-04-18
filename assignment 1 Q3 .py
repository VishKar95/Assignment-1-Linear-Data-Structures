def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

str1 = "waterbottle"
str2 = "erbottlewat"
print(is_rotation(str1, str2))  # Output: True

str3 = "hello"
str4 = "world"
print(is_rotation(str3, str4))  # Output: False
