import re

print('ab*c and ac - ', re.findall("ab*c", 'ac'))
# in above line
# "ab*c" - a string starting with a and ending with a c. and
# has b, 0 or more times
print('ab*c and abcd -', re.findall('ab*c', 'abcd'))
print('ab*c and acc - ', re.findall('ab*c', 'acc'))
print('ab*C and abcac - ', re.findall('ab*c', 'abcac'))
print('ab*c and abdc - ', re.findall('ab*c', 'abdc'))
print('ab*c and abbc - ', re.findall('ab*c', 'abbc'))


# pattern matcing is case sensitive
# to ignoring cases
print('ab*c and ABC - ', re.findall('ab*c', 'ABC'))
print('ab*c and ABBC - ', re.findall('ab*c', 'ABBC', re.IGNORECASE))

# '.' stands for single character exactly
print('a.c and abc - ', re.findall('a.c', 'abc'))
print('a.c and ac - ', re.findall('a.c', 'ac'))
print('a.c and abbc - ', re.findall('a.c', 'abbc'))
print('a.c and acc - ', re.findall('a.c', 'acc'))

# '.*' pattern stands for repeating a character any
# number of time (just it should start from a and ends with c)
print('a.*c and abc - ', re.findall('a.*c', 'abc'))
print('a.*c and abbc - ', re.findall('a.*c', 'abbc'))
print('a.*c and ac - ', re.findall('a.*c', 'ac'))
print('a.*c and acc - ', re.findall('a.*c', 'acc'))

# re.search() also find particular pattern, but it try to
# find all possible patterns in string.
# it returns MatchObject that stores different groups of data.
match_results = re.search('ab*c', "ABC", re.IGNORECASE)
print('Result of re.search() - ', match_results.group())

# re.sub(), where sub is short of substitute,
# and allows to replace text in a string 
s = 'Everything is <replaced> if it"s in <tags>.'
string = re.sub("<.*>", "Elephants", s)
print(string)
# as '.*' is greedy so it will try to take data in <re ..... gs> and replace it by ELephants.

# we will use '*?' pattern for non greedy searching.
string = re.sub('<.*?>', 'Élephents', s)
print(string)









x = 'My 2 Favourite numbers are 19and 42'
print(re.findall('[0-9]+', x))
# Here + helps to find number as long as possible, like, 2, 19, 42.
# it stop searchinf when it got a space or other character.
# without +
print(re.findall('[0-9]', x))
# here it will return as sson as it find a number, so it will return 2, 1, 9, 4, 2

# with alphabets
print(re.findall('[AEIOU]+', x))


'Warning : Greedy Matching'
# The repeat character (* and +) push outwards in both directions (greedy) to match the
# largest possible string  

x1 = 'From : Using the : character'
print(re.findall('^F.+:', x1))
# in '^F.+:'
# ^F - first character in the match is an F
# + - one or more character
# : - last character in the match is a :

# lets extract an email
email = 'From stephen.marquard@uct.ac.za to sharma.shivam3242@gmail.com Sat Jan 5 09:14:16 2008'
print(re.findall('\\S+@\\S+', email))


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

'Extracting a host name - The double split pattern'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


'Extracting a host name - using find and string slicing'
atpos = data.find('@')  # returns the index value of @ in data
print(atpos)   # print index value

sppos =  data.find(' ', atpos)   # return index value of space next to atpos(@) that is at index 31
print(sppos)

# now we will host name frome email id that is 'uct.ac.za'
host = data[atpos+1: sppos]
print(host)


'Extracting a host name - The Regex Version'
#     	'@([^ ]*)'  - The regex code
#  @ - look through the string until you find an at sign
#  [^ ] - match non-blank characters
#  *  - match many of them
y = re.findall('@([^ ]*)', data)
print(y)


'Extracting a host name - Even cooler Regex Version'
#     	'^From .*@([^ ]*)'  - The regex code
#  ^ -  starting at the beginning of the line
#  From - looking for the string 'From' in starting of line
#   .* - any number of character
#  @ - look through the string until you find an at sign
#  [^ ] - match non-blank characters
#  *  - match many of them
# returns only paranthesis search values
y = re.findall('^From .*@([^ ]*)', data)
print(y)



'''
Wild card characters

-> The dot character matches any character
-> if we add the asterisk character, the character is "any number of times"

-> ^X.*:
^ - matches the start of the line
. - matches any character
* - many times
: - matches colon too

-> ^X-\S+:
matches - X-................:
\S - match any non-whitespace character
+ - one or more times

example: does not match to following sentance due to space
'X-Place is behind schedule'


^  - matches the beginning of a line w
$  - matches the end of a line
.  - matches any character
\s - matches whitespace
\S - matches any non-whitespace character
*  - Repeats a character zero or more times
*? - Repeats a character zero or more times (Non-greedy)
+  - Repeats a character one or more times
+? - Repeats a character one or more times (Non-greedy)
[aeiou] - Matches a single character in the listed set
[^XYZ]  - Matches a single not in the listed set
[a-z0-9] - The set of characters can include a range
(   - indicates where string extraction is to start    
)   - Indicates where string extraction is to end.
'''

'''
-> re.search() returns a True/False depending on weather the string matches 
   the regular expression

-> to extract the matching string, use re.findall()


[0-9]+
-> above statement will look for one or more digits

'''
