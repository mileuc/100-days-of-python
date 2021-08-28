from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

# get webpage html code
response = requests.get(URL)
response.raise_for_status()
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "html.parser")
# print(soup.prettify())
movie_tags = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")
# grab the text, remove leading and trailing white spaces, and replace \xa0 with a space
movie_names = [tag.getText().strip().replace("\xa0", " ") for tag in movie_tags]
print(movie_names)

# create a text file with the list of the 100 greatest movies
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_names:
        if movie[0].isnumeric():
            # if first letter in string is a ranking number (and not a letter), write it to the text file
            file.write(f"{movie}\n")
