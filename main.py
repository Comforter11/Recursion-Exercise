# Check if number is a palindrome.
def is_palindrome(a_string):
    if len(a_string) <= 1:
        return True
    if a_string[0] == a_string[len(a_string) - 1]:
        return is_palindrome(a_string[1:-1])
    else:
        return False

a_string = input("Please enter a string: ")


def is_palindrome (s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
print (is_palindrome(''))
#>>> True
print (is_palindrome('madma'))
#>>> False
print (is_palindrome('madam'))
#>>> True
print (is_palindrome('mad'))
#>>> True




