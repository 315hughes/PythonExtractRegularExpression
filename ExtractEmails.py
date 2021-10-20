import re

#this regular expresison shall find all emails in the text file systemrip
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

for line in open("SystemRip.txt"):
    for match in re.finditer(pattern, line):
        print(line)



