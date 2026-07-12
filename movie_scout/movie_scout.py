import config
import json


class MovieScout:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_movie(self, title):
        e = {
            "Response": "False",
            "Error": "Movie not found in library."
        }
        for movie in LIBRARY:
            if title.lower() == movie['Title'].lower():
                return movie

        return e

    def display_movie(self, movie_data):
        print("\n--- MOVIE DETAILS ---")
        print(f"Movie Title: {movie_data.get('Title', 'None')}")
        print(f"Production Year: {movie_data.get('Year', 'N/A')}")
        print(f"Director: {movie_data.get('Director', 'N/A')}")
        print(f"imdbRating: {movie_data.get('imdbRating', 'N/A')}")

    def get_status(self, movie_data):
        if movie_data.get("Response") == "True":
            print("Movie found!")
        else:
            print(f"{movie_data.get('Error', 'Unknown Error')}")

    def save_to_watchlist(self, movie_data):
        try:
            with open("watchlist.json", "r") as file:
                watchlist = json.load(file)
        except FileNotFoundError:
            watchlist = []

        for saved_movie in watchlist:
            if saved_movie['Title'].lower() == movie_data['Title'].lower():
                print("Movie has already been saved!")
                return

        watchlist.append(movie_data)

        with open("watchlist.json", "w") as file:
            json.dump(watchlist, file)


LIBRARY = [
    {"Title": "Inception", "Year": "2010", "Director": "Christopher Nolan",
        "imdbRating": "8.8", "Response": "True"},
    {"Title": "The Matrix", "Year": "1999", "Director": "The Wachowskis",
        "imdbRating": "8.7", "Response": "True"},
    {"Title": "Shrek", "Year": "2001", "Director": "Andrew Adamson",
        "imdbRating": "7.9", "Response": "True"}
]

scout = MovieScout(config.API_KEY)
movies = ["Inception", "The Matrix", "Shrek"]

while True:
    print("\n--- Movie Scout ---")
    print("1. Search Movie")
    print("2. View Watchlist")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        user_title = input("What movie are you looking for? ")
        data = scout.fetch_movie(user_title)
        scout.get_status(data)
        scout.display_movie(data)
        if data.get("Response") == True:
            answer = input("Add to watchlist? (y/n): ")
            if answer == "y":
                scout.save_to_watchlist(data)
    elif choice == "2":
        try:
            with open("watchlist.json", "r") as file:
                watchlist = json.load(file)
                if not watchlist:
                    print("\nYour watchlist is currently empty.")
                else:
                    print("\n--- YOUR WATCHLIST ---")
                    for movie in watchlist:
                        print(f"- {movie['Title']} ({movie['Year']})")
        except FileNotFoundError:
            print("Sorry. No movies found.")

    elif choice == "3":
        print("Thanks for using Movie Scout, Goodbye!")
        break
