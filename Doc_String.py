
def function_with_outputs(f_name, l_name):
    """
    Take the first name and second name and format it
    to return the tile case version of the name.
    """
    if f_name == "" or l_name == "":
        return "you didnt provide any values"    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(function_with_outputs(input("Enter the first name: "), input("Enter the last name: ")))

print("Using __doc__:")
print(function_with_outputs.__doc__)
 
print("Using help:")
help(function_with_outputs)