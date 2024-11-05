class Vehicule:

    def __init__(self, immatriculation, type, is_parked = False, time = 0):
        self.immatriculation = immatriculation
        self.type = type
        self.is_parked = is_parked
        self.__time = time

    @property
    def time(self):
        return self.__time
    
    @time.setter
    def time(self, value):
        self.__time = value
        
        
    
        