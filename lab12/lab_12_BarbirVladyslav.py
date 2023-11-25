################Task01##############
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __format_time(self, value):
        return f"{value:02}"

    def __str__(self):
        return f"{self.__format_time(self.__hours)}:{self.__format_time(self.__minutes)}:{self.__format_time(self.__seconds)}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)
################Task02##############
class WeekDayError(Exception):
    pass


class Weeker:
    DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Invalid day of the week")
        self.__current_day_index = self.DAYS_OF_WEEK.index(day)

    def __str__(self):
        return self.DAYS_OF_WEEK[self.__current_day_index]

    def add_days(self, n):
        self.__current_day_index = (self.__current_day_index + n) % 7

    def subtract_days(self, n):
        self.__current_day_index = (self.__current_day_index - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
################Task03##############
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
################Task04##############
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])
        return side1 + side2 + side3

point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)

triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())
