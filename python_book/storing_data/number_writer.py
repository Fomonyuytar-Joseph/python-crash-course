from pathlib import Path
import json


numbers = [2,3,5,7,11]

path = Path("numbers.json")

# converts any python data structure to json
contents = json.dumps(numbers)

path.write_text(contents)