
print("Exercise 1: Remove Letter(s) From a String in Python\n")

ex_str = "Today is a good day!"

# ex_str = ex_str.replace("T", "")

print(ex_str, "\n\n\n-----------------------")

# ------------------------------------------------------

print("Check whether the string is Symmetrical or Palindrome\n\n")

print("Please enter a string when prompted.")

userInput = input("Please enter a string:\n")

# function to check if string is symmetrical
def check_symmetrical(str):

    #get length
    str_length = len(str)

    # get string half
    mid_str = str_length // 2

    if str_length % 2 == 0:
        return str[:mid_str] == str[mid_str:]
    # ignore middle character and compare
    else:
        return str[:mid_str] == str[mid_str+1:]



if(check_symmetrical(userInput)):
    print("String is symmetrical")
else:
    print("String is not symmetrical")



# function to check if string is palindrome
def check_palindrome(str):
    return str == str[::-1]


if(check_palindrome(userInput)):
    print("String is palindrome")
else:
    print("String is not palindrome")



