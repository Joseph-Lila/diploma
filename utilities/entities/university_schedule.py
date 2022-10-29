import datetime
from sortedcontainers import SortedSet
from prettytable import PrettyTable


class UniversitySchedule:
    def __init__(self, name, description=None):
        self.__name = name
        self.__description = description
        self.__schedule = SortedSet()

    @property
    def schedule(self):
        return self.__schedule

    def add_schedule_item(self, start, end):
        """
        Here we add a new schedule item.
        :param start: datetime.time
        :param end: datetime.time
        :return: None
        """
        if type(start) != datetime.time or type(end) != datetime.time:
            raise TypeError('`start` and `end` must be datetime.time')
        if start > end:
            start, end = end, start
        self.__schedule.add((start, end))

    def __str__(self):
        table = PrettyTable()
        table.header = True
        table.title = self.__name
        table.field_names = ["Start", "End"]
        table.add_rows(self.__schedule)
        return str(table)
