import datetime

from utilities.entities.group import Group
from utilities.entities.professor import Professor
from utilities.entities.subject import Subject
from utilities.entities.workload import Workload


class DayItem:
    def __init__(self, start, end, room=None, professor=None, group=None, subject=None):
        """
        Create a new DayItem object
        :param start: datetime.time
        :param end: datetime.time
        :param room: Room
        :param professor: Professor
        :param group: Group
        :param subject: Subject
        """
        self.__start = start
        self.__finish = end
        self.__subject = subject
        self.__group = group
        self.__room = room
        self.__professor = professor

    def is_empty(self):
        return self.__room is None

    def fill(self, room, professor, group, subject):
        self.__room = room
        self.__professor = professor
        self.__group = group
        self.__subject = subject

    def clear(self):
        self.__room = None
        self.__professor = None
        self.__group = None
        self.__subject = None

    def __str__(self):
        return "{} {} {}".format(
            self.__subject if self.__subject else '',
            self.__room if self.__room else '',
            self.__professor if self.__professor else ''
        )
