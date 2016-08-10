import re
 
word = input()
reword = re.sub('[aiueo]', '', word)
print(reword)
