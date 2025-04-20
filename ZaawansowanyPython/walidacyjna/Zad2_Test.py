import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import główna.Zad2 as zad2

movie_list = [
    zad2.Movie( "The Shawshank Redemption",1994,9.3 ),
    zad2.Movie( "The Godfather",1972,9.2 ),
    zad2.Movie( "The Dark Knight",2008,9.0 ),
    zad2.Movie( "The Godfather Part II",1974,9.0 ),
    zad2.Movie( "12 Angry Men",1957,9.0 ),
    zad2.Movie( "The Lord of the Rings: The Return of the King",2003,9.0 ),
    zad2.Movie( "Schindler's List",1993,9.0 ),
    zad2.Movie( "Pulp Fiction",1994,8.9 ),
    zad2.Movie( "The Lord of the Rings: The Fellowship of the Ring",2001,8.9),
    zad2.Movie( "The Good, the Bad and the Ugly",1966,8.8),
]

print(f"{ movie_list } Lista nie posortowana")

# Sortowanie rosnące po roku wydania
movie_list.sort(key= lambda movie: movie.year)
print(f"{ movie_list } Lista posortowana")

# Sortowanie rosnące po ocenie
movie_list.sort(key= lambda movie: movie.rating)
print(f"{ movie_list } Lista posortowana")

# Sortowanie rosnące alfabetyczne
movie_list.sort(key= lambda movie: movie.title)
print(f"{ movie_list } Lista posortowana")

# Sortowanie malejące po roku wydania
movie_list.sort(key= lambda movie: movie.year, reverse=True)
print(f"{ movie_list } Lista posortowana")

# Sortowanie malejące po roku wydania
movie_list.sort(key= lambda movie: movie.rating, reverse=True)
print(f"{ movie_list } Lista posortowana")