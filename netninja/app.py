from pathlib import Path
import json

path = Path(__file__).parent / "characters.json"

characters = {
    "characters": [
        {"name": "Mario", "age": 25},
        {"name": "Gertrude", "age": 23},
        {"name": "Marian", "age": 5},
        {"name": "Micheal", "age": 3},
    ]
}


def write_json():
    with path.open('w') as file:
        json.dump(characters, file , indent=2)
    return


def read_json():
    with path.open('r') as file:
        content = json.load(file)
    return content


def main():
    write_json()
    data = read_json()
    print(data)


if __name__ == "__main__":
    main()


# def open_file():
#     # directory path
#     path = Path(__file__).parent / "characters.txt"

#     data = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser "]

#     # context manager ----> auto closes

#     with path.open('w') as file:
#         for c in data:
#             file.write(c + "\n")


# def main():
#     open_file()


# if __name__ == "__main__":
#     main()
