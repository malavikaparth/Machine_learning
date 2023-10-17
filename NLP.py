import re

#Pattern Matching from the beginning of the string
#Match will always try anf match from the beginning until it can no longer go forward but search does not.

#It's important to prefix your regex patterns with r
# to ensure that your patterns are interpreted in the way you want them to.
# Else, you may encounter problems to do with escape sequences in strings.

'''
IMPORTANT NOTES(https://docs.python.org/3/library/re.html)
----------------
1. Regular expressions use the backslash character ('\') 
   to indicate special forms or to allow special characters 
   to be used without invoking their special meaning.
'''

#Matching the whole word
print(re.match('\w+','malavika'))
print(re.search('la','malavika'))

#Matching digits(here one digit)
print(re.match('\d','05malavika'))

#Matching letters(Here two digits. Note the + after d to get all the digits)
print(re.match('\d+','05789malavika'))

#Matching space
print(re.match('\s+','malavika luca'))

#Matching lowercase
print(re.match('[a-z]','malavika luca'))

#Matching lowercase
print(re.match('[a-z]+','malavika luca'))

#Matching lowercase
print(re.match('[a-z]+\s','malavika luca'))

#Matching lowercase
print(re.match('[a-z]+\s[a-z]+','malavika luca'))

#Matching things with []
print(re.search('\[.*?\]+\s+\[.*?\]','[malavika] [luca]'))
