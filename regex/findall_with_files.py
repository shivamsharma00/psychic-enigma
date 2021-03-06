
### For more information    https://docs.python.org/3/library/re.html

'''

For files, you may be in the habit of writing a loop to iterate over the lines of the file,
and you could then call findall() on each line. Instead, let findall() do the iteration for you
-- much better! Just feed the whole file text into findall() and let it return a list of 
all the matches in a single step (recall that f.read() returns the whole text of a file in a single string):

'''
import re

# open file
f = open('test.txt', 'r')
# feed the file into findall:
strings = re.findall(r'some pattern', f.read())

