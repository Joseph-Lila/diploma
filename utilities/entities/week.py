from utilities.entities.day import Day


class Week:
    ACCEPTED_WEEK_TYPES = ['UNDER THE LINE', 'ABOVE THE LINE']

    def __init__(self, week_type, university_schedule):
        if week_type not in Week.ACCEPTED_WEEK_TYPES:
            raise ValueError('week_type must be one of {}'.format(Week.ACCEPTED_WEEK_TYPES))
        if university_schedule is None:
            raise ValueError('university_schedule can\'t be None')
        self.__week_type = week_type
        self.__university_schedule = university_schedule
        self.__days = []
        self.__generate_empty_days()

    def __generate_empty_days(self):
        for day_name in Day.ACCEPTED_DAY_NAMES:
            self.__days.append(Day(day_name, self.__university_schedule))
