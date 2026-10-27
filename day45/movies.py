from bs4 import BeautifulSoup
import requests


URL =  "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)

movie_webpage = response.text

# print(movie_webpage)

soup = BeautifulSoup(movie_webpage, "html.parser")


website_movies = soup.find_all(name="h3" ,class_="title")

list_of_movies = [website_movie.getText() for website_movie in website_movies]

ordered_list_of_movies = list_of_movies[::-1]


# print(ordered_list_of_movies)




with open("movies.txt","w") as movie_file:
    for movie in ordered_list_of_movies:
        movie_file.write(f"{movie}\n")


