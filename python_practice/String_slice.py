"""
s = 'abcde'

print(len(s))

s1 = 'a\tb\\c'
s2 = r'a\tb\\c'

print(len(s))
print(len(s2))

s3 = 'abc\nabcd\r\nab'

print(s3)
print(len(s3))

print(s3.splitlines())

print("abc" != "ABC")
print("abc" == 'xyz')

print('bbb' in 'aaa-bbb-ccc')

import re

s = 'aaa-AAA-123'
print(re.search('aaa', s))



s_blank = 'one two   three\nfour\tfive'
print(s_blank)
print(s_blank.split())


s_comma = 'one,two,three,four,five'
print(s_comma.split(','))



var1 = 7
var2 = 2
result = var1 // var2 + var1%var2
print(result)



def concatenate_string(str1,str2):
    return str1+" "+str2


result = concatenate_string("hello", "world")
print(result)


def print_uppercase(text):
    for letter in text:
        print(letter.upper())
print_uppercase("Test")




def test(x, y=[]):
    y.append(x)
    return y 
print(test(1))
print(test(2))


name = input("Enter your name ")
if name == "Johan" or "brain":
    print("welcome johan or brain")
else:
    print("your not johan or brain")
"""

import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
print(response)

data = response.json()

print(data)





























