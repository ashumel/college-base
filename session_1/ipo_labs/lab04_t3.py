import re
msg = 'HELLO ANDREY, where have you been, well, hug me soon!'
count_latin_upper = len(re.findall('[A-Z]', msg))
count_latin_lower = len(re.findall('[a-z]', msg))
print(count_latin_upper, count_latin_lower)