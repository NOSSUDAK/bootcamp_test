from movie_manager import (
    Film,
    add_note,
    read_notes,
    remove_note,
    get_highest_rating_films,
    get_lowest_rating_films,
    get_average_rating,
    print_notes
)

FILE_NAME = "test.csv"
# create some test films and write to the file
film = Film("Mamba", "Movie about warriors", 1)
add_note(FILE_NAME, film)
film = Film("LOTR", "Movie about elves and orcs", 5)
add_note(FILE_NAME, film)
film = Film("Taxi", "Movie about cars", 3)
add_note(FILE_NAME, film)
film = Film("Titanic", "Movie about love", 5)
add_note(FILE_NAME, film)

# read all films from file
for film in read_notes(FILE_NAME):
    print(film)

# delete a film from file
remove_note(FILE_NAME, "LOTR")

# print all data from file
print_notes(FILE_NAME)

# list all top rated films
for film in get_highest_rating_films(FILE_NAME):
    print(film)

# list all low rated films
for film in get_lowest_rating_films(FILE_NAME):
    print(film)

# average rating
print(f"Average rating is {get_average_rating(FILE_NAME)} stars")
