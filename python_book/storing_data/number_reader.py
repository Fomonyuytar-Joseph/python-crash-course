from pathlib import Path
import json


path = Path("numbers.json")

contents = path.read_text()

#converts json to the required data structure
numbers = json.loads(contents)

print(numbers)
