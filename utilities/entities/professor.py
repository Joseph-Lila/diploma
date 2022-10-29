class Professor:
    def __init__(self, name: str, surname: str, lastname: str, rank: str = None):
        self.__name: str = name
        self.__surname: str = surname
        self.__lastname: str = lastname
        self.__rank: str = rank

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def rank(self):
        return self.__rank

    @name.setter
    def name(self, value):
        self.__name = value

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @rank.setter
    def rank(self, value):
        self.__rank = value

    def __str__(self):
        return f"{self.rank if self.rank else ''} {self.surname} {self.name[0]}.{self.lastname[0]}."
