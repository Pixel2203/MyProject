testdata = [
  {
    "title": "Inception",
    "genre": "Science Fiction",
    "rating": 8.8,
    "date": "2010-07-16"
  },
  {
    "title": "The Dark Knight",
    "genre": "Action",
    "rating": 9.0,
    "date": "2008-07-18"
  },
  {
    "title": "Parasite",
    "genre": "Thriller",
    "rating": 8.6,
    "date": "2019-05-30"
  },
  {
    "title": "Interstellar",
    "genre": "Science Fiction",
    "rating": 8.7,
    "date": "2014-11-07"
  },
  {
    "title": "The Godfather",
    "genre": "Crime",
    "rating": 9.2,
    "date": "1972-03-24"
  },
  {
    "title": "Pulp Fiction",
    "genre": "Crime",
    "rating": 8.9,
    "date": "1994-10-14"
  },
  {
    "title": "The Shawshank Redemption",
    "genre": "Drama",
    "rating": 9.3,
    "date": "1994-09-23"
  },
  {
    "title": "Avengers: Endgame",
    "genre": "Superhero",
    "rating": 8.4,
    "date": "2019-04-26"
  },
  {
    "title": "Forrest Gump",
    "genre": "Drama",
    "rating": 8.8,
    "date": "1994-07-06"
  },
  {
    "title": "The Matrix",
    "genre": "Science Fiction",
    "rating": 8.7,
    "date": "1999-03-31"
  }
]



genres = [testdata["genre"] for testdata in testdata]


print("We got the following genres: " , genres)
print("What Genre Do you want to get Info about?")

fav_genre = input("Genre: ")

found_movies = [movie for movie in testdata if movie["genre"] == fav_genre]
print("We found the following movies:")
print([movie["title"] for movie in found_movies])
print()
min_rating = float(input("Minimum Rating: "))
print("We found the following Movies, matching your Rating: ")
print([movie["title"] for movie in found_movies if movie["rating"] >= min_rating])
