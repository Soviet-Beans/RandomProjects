# Libraries

import random
import time

# Characters

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '{}[]()*;,._-!@#$%^&'

# Generator


global password
all = lower + upper + numbers + symbols
length = int(input('How long would you like your password to be? (max 80) '))
password = ''.join(random.sample(all,length))
print(password)
pause = input('Press enter to continue')

# Save

save = open('passwords.txt', 'a')
save.write('\n')
save.write(password)