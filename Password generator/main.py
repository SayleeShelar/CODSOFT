import string
import random

'''This line imports a module called 'string' which contains useful functions and variables
 to work with strings (text). It includes things like a list of all letters, digits, punctuation, etc.'''

if __name__ == "__main__": # This condition checks if the script is being run directly (not imported as a module).

    s1 = string.ascii_lowercase # s1 contains all the lowercase letters in the English alphabet (a to z).
   # print(s1)

    s2 = string.ascii_uppercase # s2 contains all the uppercase letters in the English alphabet (A to Z).
    #print(s2)

    s3 = string.digits # s3 contains all the digits (0 to 9).
    #print(s3)

    s4 = string.punctuation # s4 contains all the punctuation characters (like !, @, #, $, etc.).
    #print(s4)

    plen = int(input("Enter password length\n"))
    # This line prompts the user to enter the desired length of the password.
    # The input is converted to an integer and stored in the variable 'plen'.

    s = [] 
    # An empty list 's' is created to hold all the characters for the password.

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))#difference between extend and append is that when u use append it will add the list in the list and when you use extend it will add the elements of the list
    # print(s) 

    random.shuffle(s)
    # The list 's' is shuffled randomly to ensure that the password characters are in a random order.
    # print(s)
    
    print("your password is:")
    print("".join(s[0:plen])) # This line joins the first 'plen' characters of the shuffled list 's' into a single string,
    