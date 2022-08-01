import csv


class Film:
    def __init__(self, film_name: str, note: str, rating: int):
        self.film_name = film_name
        self.note = note
        self.rating = rating

    def __str__(self):
        return f"'{self.film_name}' - {self.note} with {self.rating} star rating"


def read_notes(file_name: str) -> list:
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return [Film(*row) for row in film_reader]


def add_note(file_name: str, film) -> None:
    with open(file_name, 'a', newline='') as csvfile:
        film_writer = csv.writer(
            csvfile, delimiter=' ',
            quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        film_writer.writerow([film.film_name, film.note, film.rating])
    print(f"'{film.film_name}' film was saved to file")


def remove_note(file_name: str, film_name: str) -> None:
    rows_to_keep = []
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in film_reader:
            if film_name not in row:
                rows_to_keep.append(row)
    with open(file_name, 'w', newline='') as csvfile:
        film_writer = csv.writer(
            csvfile, delimiter=' ',
            quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        for row in rows_to_keep:
            film_writer.writerow(row)
    print("Data removed")


def print_notes(file_name: str) -> None:
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in film_reader:
            print(row)


def get_highest_rating_films(file_name: str) -> list:
    top_rated_films = []
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in film_reader:
            if int(row[-1]) == 5:
                top_rated_films.append(Film(*row))
    return top_rated_films


def get_lowest_rating_films(file_name: str) -> list:
    low_rated_films = []
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in film_reader:
            if int(row[-1]) == 1:
                low_rated_films.append(Film(*row))
    return low_rated_films


def get_average_rating(file_name: str) -> float:
    with open(file_name, newline='') as csvfile:
        film_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        ratings = [int(row[-1]) for row in film_reader]
    return round(sum(ratings) / len(ratings), 1)
