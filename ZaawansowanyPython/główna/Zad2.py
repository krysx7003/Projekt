class Movie:
    title:str
    year:int
    rating:float

    def __init__(self,title,year,rating):
        self.title = title
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"Tytuł: {self.title}, rok: {self.year}, ocena {self.rating}/10\n"

    def __repr__(self):
        return self.__str__()