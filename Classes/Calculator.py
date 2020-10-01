from Classes.Course import Course
from Classes.ErrorMsg import ErrorMsg


class Calculator:
    gpa = 0
    points = 0
    courses = [[]]  # array of arrays from 1 point courses to 10 point courses
    added_courses = []  # array of courses in insert order
    courses_count = 0

    def __init__(self):
        for x in range(19):
            self.courses.append([])

    # adds a course to the calculator
    def add_course(self, name, points, grade):
        if len(name) < 1:
            return ErrorMsg("Course name must have at least 1 character!")
        if len(name) > 30:
            return ErrorMsg("Course name must be less then 30 characters!")

        course = Course(name, points, grade)
        # put new course in appropriate array and keep it sorted
        i = 0
        for x in self.courses[int(points * 2 - 2)]:
            if course.grade < x.grade:
                self.courses[int(points * 2 - 2)].insert(i, course)
                break
            i += 1

        if i == len(self.courses[int(points * 2 - 2)]):  # last position
            self.courses[int(points * 2 - 2)].append(course)

        self.added_courses.append(course)
        self.courses_count += 1
        new_points = self.points + points
        self.gpa = (self.points / new_points * self.gpa) + (points / new_points * grade)
        self.points += points
        return course

    # removes a course from the calculator
    def remove_course(self, course):
        if course in self.courses[int(course.points * 2 - 2)]:
            self.courses[int(course.points * 2 - 2)].remove(course)
            if not self.points - course.points == 0:
                self.gpa = ((self.gpa * self.points) - (course.grade * course.points)) \
                           / (self.points - course.points)
            else:
                self.gpa = 0
            self.points = self.points - course.points
            self.added_courses.remove(course)
