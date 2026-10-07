from pathlib import Path

path = Path(
    '/home/joseph/learning/python-crash-course/python_book/files_and_exceptions/pi_digits.txt')
contents = path.read_text()

pi_string = ""
lines = contents.splitlines()

for line in lines:
    pi_string+=line.lstrip()

print(pi_string)
