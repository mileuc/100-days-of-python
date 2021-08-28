from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv("./.env")

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"
BASE_URL = "https://www.billboard.com/charts/hot-100"

valid_date = False
while not valid_date:
    input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get(f"{BASE_URL}/{input_date}")
    if response.status_code == 200:
        valid_date = True
    else:
        print("Sorry! Please enter a valid date!")

year = input_date.split("-")[0]
search_years = f"{int(year)-2}-{year}"  # in case a song was released within the 2 years prior to billboard year


# print("Valid date!")
# use BeautifulSoup to scrape the Billboard top 100 songs from a particular date of your choice
webpage_html = response.text
soup = BeautifulSoup(webpage_html, "html.parser")
# extract all of the song titles from the list
song_titles_tags = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artist_tags = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

song_titles = [tag.getText() for tag in song_titles_tags]
song_artists = [tag.getText() for tag in artist_tags]
song_tuples = []
for title in song_titles:
    index = song_titles.index(title)
    song_tuples.append((song_titles[index], song_artists[index]))

# print(f"{song_titles}\n{song_artists}\n{song_tuples}")

# use spotify API to create a new playlist for that date
# spotipy: a light weight Python library for the Spotify Web API
scope = "playlist-modify-private"  # write access to a user's private playlists.

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               cache_path=".cache"))

# get the user id of the authenticated user
# print(sp.current_user())
user_id = sp.current_user()["id"]

# search through spotify for each song and add them to our new playlist
song_uris = []
for song_tuple in song_tuples:
    title = song_tuple[0]
    artist = song_tuple[1]
    query = f"track:{title} artist:{artist} year:{search_years}"
    search_result = sp.search(q=query, type="track")
    try:
        song_uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify - skipped")

# pprint(song_uris)

# create playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False,
                                   description="Wrote code in Python to create this playlist!")
# print(playlist)  # to locate the id
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
# for testing to see what the output looked like
# title = song_tuples[0][0]
# artist = song_tuples[0][1]
# query = f"track:{title} artist:{artist} year:{year}"
# search_result = sp.search(q=query, type="track")
# pprint(search_result)
