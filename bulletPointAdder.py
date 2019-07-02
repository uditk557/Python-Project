#1 python3
# It adds bullet points to the start of a wikipedia list

import pyperclip
text = pyperclip.paste()

lines = text.split()
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)