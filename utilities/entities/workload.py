from utilities.entities.group import Group
from utilities.entities.professor import Professor
from utilities.entities.subject import Subject


class Workload:
    def __init__(self, professor, subject, group, hours):
        self.__professor = professor
        self.__subject = subject
        self.__group = group
        self.__hours = hours

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject
