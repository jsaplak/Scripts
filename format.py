
global var_1, var_2

var_1 = "'"
var_2 = ", "
qv = ""

def Format(input_s):
    values = input_s.split()
    format_input_s = [f"{var_1}{value}{var_1}" for value in values]
    return"({})".format(var_2.join(format_input_s))



print("SIMPLE LIST FORMATTER\nPress s for settings\n(press q to quit)")

while (qv != "q"):
    
    user_i = input("Enter Values: ")
    
    if user_i == "s":
        print("============")
        print(f"press w to change Wrapper\npress se for new Seperator{var_1}Value{var_1}\n")
        print(f"# Wrapper: {var_1}Value{var_1}")
        print(f"# Seperator: Value{var_2}|(line to ID spacebar)")
    if user_i == "({var_1}w{var_1})":
            var_1 = input("Enter New Wrapper: ")
    if user_i == "({var_1}se{var_1})":
            var_2 = input("Enter New Seperator: ")
    
    if user_i == "q":
        break
    else:
        print("\n============\n")
        print(Format(user_i))
        # print("\n")
    