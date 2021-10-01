import requests
from bs4 import BeautifulSoup


URL = "https://stacker.com/stories/1587/100-best-movies-all-time"

response = requests.get(url=URL)
em_web = response.text
soup = BeautifulSoup(em_web, "html.parser")

all_movies = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")

list_movies = [movie.getText() for movie in all_movies]
list_movies.pop(0);
movies = list_movies[::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(movie)

