

more_characters = ["Diddy Kong", "Donkey Kong" , "Wario"]


def write_characters_to_file(filename):
    file = open(filename,"a+")


    for c in more_characters:
        file.write(c + "\n")

    
    file.close()
    return


def main():
    write_characters_to_file("characters.txt")
    


if __name__ == "__main__":
    main()