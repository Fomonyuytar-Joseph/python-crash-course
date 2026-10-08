from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

pi_string = ""
lines = contents.splitlines()

for line in lines:
    pi_string += line.lstrip()

print(pi_string)
