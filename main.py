import requests
from bs4 import BeautifulSoup


URL = "https://stacker.com/stories/1587/100-best-movies-all-time"

response = requests.get(url=URL)
em_web = response.text
soup = BeautifulSoup(em_web, "html.parser")

all_movies = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")
all_desc = soup.select(selector="div.paragraph--view-mode--full:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)")

list_movies = [movie.getText() for movie in all_movies]
list_movies.pop(0)
# list_desc = [desc.getText() for desc in all_desc]

print(all_desc)
movies = list_movies[::-1]
# descs = list_desc[::-1]
# with open("movies.txt", mode="w", encoding="utf8") as file:
#
#     for movie in movies:
#         file.write(movie)
#

