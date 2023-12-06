def no_c(my_string):
   string = ""
   for char in my_string:
    if char in my_string != "c" and char != "C":
        string += char
    return string
