import fresh_tomatoes
import media


# define the details for each movie
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of \
    diner bandits intertwine in four tales of violence and redemption.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover.jpg/220px-Pulp_Fiction_cover.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
fight_club = media.Movie(
    "Fight Club",
    "An insomniac office worker looking for a way to change his life crosses \
    paths with a devil-may-care soap maker.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")
the_matrix = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature of \
    his reality and his role in the war against its controllers.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
movie_1984 = media.Movie(
    "1984",
    "George Orwell's novel of a totalitarian future society in which a man \
    whose daily work is rewriting history tries to rebel by falling in love.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Nineteen_Eighty_Four.jpg/220px-Nineteen_Eighty_Four.jpg",
    "https://www.youtube.com/watch?v=Z4rBDUJTnNU")
memento = media.Movie(
    "Memento",
    "A man creates a strange system to help him remember things; so he can \
    hunt for the murderer of his wife without his short-term memory loss being \
    an obstacle.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Memento_poster.jpg/220px-Memento_poster.jpg",
    "https://www.youtube.com/watch?v=0vS0E9bBSL0")
the_apartment = media.Movie(
    "The Apartment",
    "A man tries to rise in his company by letting its executives use his \
    apartment for trysts, but complications and a romance of his own ensue.",
    "http://upload.wikimedia.org/wikipedia/en/b/bb/Apartment_60.jpg",
    "https://www.youtube.com/watch?v=B4OXm9-E8OQ")

# the list of movies needed as parameter by open_movies_page
movies = [pulp_fiction, fight_club, the_matrix, movie_1984, memento, the_apartment]

fresh_tomatoes.open_movies_page(movies)
