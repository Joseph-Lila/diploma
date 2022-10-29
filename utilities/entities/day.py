from enum import Enum

from sortedcontainers import SortedSet

from utilities.entities.day_item import DayItem


class Day:
    ACCEPTED_DAY_NAMES = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ']

    def __init__(self, name, university_schedule):
        self.__name = name
        self.__university_schedule = university_schedule
        self.__day_items = SortedSet()
        self.__generate_empty_day_items()

    def __generate_empty_day_items(self):
        if self.__university_schedule is None:
            raise TypeError('University schedule is required!')
        for schedule_item in self.__university_schedule.schedule:
            self.__day_items.add(DayItem(*schedule_item))
