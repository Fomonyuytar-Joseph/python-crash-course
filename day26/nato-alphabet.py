import pandas

#read the csv file using the pandas library
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#we convert the DataFrame form pandas to a dictionary 
nato_alpha_dict = {row.letter: row.code for (index , row) in nato_alphabet.iterrows()}

#get the user input and convert it then to upper case just in case it in small letters
user_input = input("Enter a word: ").upper()

#convert this user input to a list of letters
split_user_input = [letter for letter in user_input]


# we loop through the list of letters and then check the equivalent letter code
result = [nato_alpha_dict[letter]  for letter in split_user_input if  nato_alpha_dict[letter] ]

print(result)


#simpler version 

final_result = [nato_alpha_dict[letter] for letter in user_input]

print(final_result)
