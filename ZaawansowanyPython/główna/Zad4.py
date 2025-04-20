class Polynomial:
    terms_num:int
    coeficient_list:list

    def __init__(self,terms_num):
        self.terms_num = terms_num
        self.coeficient_list = [0] * terms_num
    
    def __getitem__(self, key):
        if key < self.terms_num: 
            return self.coeficient_list[key]        
        else:
            return 0
  
    def __setitem__(self, key, new_value): 
        self.coeficient_list[key] = new_value
    
    def __add__(self,other):

        if isinstance(other,int):
            new_poly = Polynomial(self.terms_num)
            new_poly.coeficient_list = self.coeficient_list[:]
            new_poly.terms_num = self.terms_num
            new_poly.coeficient_list[0] += other
            return new_poly

        elif isinstance(other,Polynomial):
            max_len = max(self.terms_num,other.terms_num)
            new_poly = Polynomial(max_len)

            for i in range(self.terms_num):
                new_poly.coeficient_list[i] += self.coeficient_list[i]

            for i in range(other.terms_num):
                new_poly.coeficient_list[i] += other.coeficient_list[i]

            new_poly.terms_num = max_len
            return new_poly


    def __radd__(self,other):
        return self.__add__(other)

    def __str__(self):
        poly = ""
        for i in range(self.terms_num - 1, -1, -1):
            if i != 0:
                poly += f"{ self.coeficient_list[i] }*x^{i} + "
            else:
                poly += f"{ self.coeficient_list[i] }"
        
        return poly

    def __repr__(self):
        return self.__str__()