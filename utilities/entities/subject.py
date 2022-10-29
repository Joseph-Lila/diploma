from typing import Union


class Subject:
    def __init__(self, title, description, type_of_class, needed_equipment: Union[None, list, tuple] = None):
        self.__title = title
        self.__description = description
        self.__type_of_class = type_of_class
        self.__needed_equipment = needed_equipment
