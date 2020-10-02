from Classes.Course import Course
from Classes.ErrorMsg import ErrorMsg


class Calculator:
    gpa = 0
    total_points = 0
    courses = [[]]  # array of arrays from 1 point courses to 10 point courses
    added_courses = []  # array of courses in insert order
    courses_count = 0
    max_gpa_120 = 100
    max_gpa_160 = 100

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
        self.add_course_to_gpa_and_total_points(course)
        return course

    # removes a course from the calculator
    def remove_course(self, course):
        if course in self.courses[int(course.points * 2 - 2)]:
            self.courses[int(course.points * 2 - 2)].remove(course)
            if course.enabled:
                self.remove_course_from_gpa_and_total_points(course)

            self.added_courses.remove(course)

    # updates GPA and total points when enabling or disabling a course
    def enable_disable_update(self, course):
        if course.enabled:
            self.add_course_to_gpa_and_total_points(course)

        else:
            self.remove_course_from_gpa_and_total_points(course)

    # adding a course to the GPA and Total Points
    def add_course_to_gpa_and_total_points(self, course):
        new_points = self.total_points + course.points
        self.gpa = (self.total_points / new_points * self.gpa) + (course.points / new_points * course.grade)
        self.total_points += course.points

    # removes a course from the GPA and Total Points
    def remove_course_from_gpa_and_total_points(self, course):
        if not self.total_points - course.points == 0:
            self.gpa = ((self.gpa * self.total_points) - (course.grade * course.points)) \
                       / (self.total_points - course.points)
        else:
            self.gpa = 0
        self.total_points = self.total_points - course.points

    # calculates max GPA possible for 120 and 160 total points
    def calculate_max_gpa(self):
        self.max_gpa_120 = ((self.total_points * (self.gpa - 100)) + 12000) / 120
        self.max_gpa_160 = ((self.total_points * (self.gpa - 100)) + 16000) / 160
