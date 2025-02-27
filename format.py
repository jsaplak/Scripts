
global var_1, var_2

var_1 = "'"
var_2 = ", "
qv = ""

def Format(input_s):
    values = input_s.split()
    format_input_s = [f"{var_1}{value}{var_1}" for value in values]
    return"({})".format(var_2.join(format_input_s))



print("== SIMPLE LIST FORMATTER ==\nPress s for settings\nPress q to quit")

while (qv != "q"):
    
    user_i = input("Enter Values: ")
    
    if user_i == "s":
        while True:
            print("====== Settings ======")
            print(f"press w to change Wrapper\npress se for new Seperator\n")
            print(f"# Wrapper: {var_1}Value{var_1}")
            print(f"# Seperator: Value{var_2}|(line to ID spacebar)")

            settings_i = input("Enter (press b to return): ")

            if settings_i == "w":
                    var_1 = input("Enter New Wrapper: ")
            elif settings_i == "se":
                    var_2 = input("Enter New Seperator: ")
            elif settings_i == "b":
                break
            else:
                print("Not an Option")

    
    if user_i == "q":
        break
    else:
        print("\n============\n")
        print(Format(user_i))
    
    