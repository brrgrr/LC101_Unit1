#1
from test import testEqual

testEqual('Python'[1] , 'y')
testEqual('Strings are sequences of characters.'[5] , 'g')
testEqual(len('wonderful') , 9)
testEqual('Mystery'[:4] , 'Myst')
testEqual('p' in 'Pineapple' , True)
testEqual('apple' in 'Pineapple' , True)
testEqual('pear' not in 'Pineapple' , True)
testEqual('apple' > 'pineapple' , False)
testEqual('pineapple' < 'Peach' , False)

#2
def num_digits(n):
    n_str = str(n)
    return len(n_str)

def main():
    print(num_digits(50))
    print(num_digits(20000))
    print(num_digits(1))

if __name__ == "__main__":
    main()

#3
from test import testEqual

def remove(substr,original_string):
    index = original_string.find(substr)
    if index < 0:
        return original_string
    else:
        return original_string[:index] + original_string[index+len(substr):]
        

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')

#4
from test import testEqual

def reverse(text):
    r = ''
    for char in text:
        r = char + r
    return r

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")

#5
from test import testEqual

def reverse(text):
    r = ''
    for char in text:
        r = char + r
    return r

def is_palindrome(text):
    return text == reverse(text)

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

#6
def mirror(text):
    m = text + reverse(text)
    return m

def reverse(text):
    r = ''
    for char in text:
        r = char + r
    return r


from test import testEqual
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

#7
import string
alphabet = (string.ascii_lowercase)
def encrypt(message, cipher):
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

cipher = "qwertyuiopasdfghjklzxcvbnm"
message = "hello world"

encrypted = encrypt(message, cipher)
print(encrypted)


#8
import string 
alphabet = (string.ascii_lowercase)
def encrypt(message, cipher):
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

def decrypt(encrypted, cipher):
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted


cipher = "qwertyuiopasdfghjklzxcvbnm"
message = "hello world"

encrypted = encrypt(message, cipher)
print(encrypted)

decrypted = decrypt(encrypted, cipher)
print(decrypted)

#9
import string

def rot13(mess):
    alphabet = (string.ascii_lowercase)
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + 13
            encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted

def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()

#Weekly Graded Assignment
def analyze_text(text):
    alpha = 0
    e_count = 0
    for char in text:
        if char.isalpha():
            alpha += 1
        if char.lower() == "e":
            e_count += 1
            
    answer_string = "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'."
    return answer_string.format(alpha, e_count, (e_count / alpha * 100))

# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)



