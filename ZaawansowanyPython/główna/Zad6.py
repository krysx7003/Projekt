MILEAGE_MULT = 0.000001
AGE_MULT = 0.001

class Car:
    make: str 
    model: str 
    year: int
    _mileage: int 
    _price: float

    def __init__(self,make,model,year,mileage,price):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage
        self._price = price
    
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self._mileage = value
        else:
            raise ValueError("Mileage cannot be negative.")
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative.")

    def __str__(self):
        return f"Marka: {self.make}, model: {self.model}, rocznik: {self.year}, przejechane: {self.mileage}, cena: {self.price}"

    def __repr__(self):
        return self.__str__()
    
    def drive(self,drive_length):
        self.mileage += drive_length

    def calculate_depreciation(self,curr_year):
        self.price -= ( self.mileage * MILEAGE_MULT + ( curr_year - self.year ) * AGE_MULT ) * self.price