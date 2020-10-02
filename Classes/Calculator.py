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

    # greedy algorithm
    # returns the top 3 courses to improve
    def top_3_to_improve(self):
        result = []
        min_list = []
        # gather all possible courses
        for i in range(19):
            if self.courses[i]:
                temp = next((x for x in self.courses[i] if x.enabled), None)
                if temp:
                    min_list.append(temp)

        # sort by improve_score
        min_list.sort(key=lambda course: course.improve_score, reverse=True)

        if min_list:
            result.append(min_list[0])  # 1st to improve
            self.add_next_to_min_list(min_list, min_list[0])

        if min_list:
            result.append(min_list[0])  # 2nd to improve
            self.add_next_to_min_list(min_list, min_list[0])

        if min_list:
            result.append(min_list[0])  # 3rd to improve

        return result

    # help function for top_3_to_improve
    def add_next_to_min_list(self, min_list, last_course):
        min_list.remove(last_course)
        index = self.courses[int(last_course.points * 2) - 2].index(last_course) + 1
        temp = next((x for x in self.courses[int(last_course.points * 2) - 2][index:] if x.enabled), None)

        # add course to min_list and keep it sorted
        if temp:
            i = 0
            for course in min_list:
                if temp.improve_score > course.improve_score:
                    min_list.insert(i, temp)
                    break
                i += 1

            if i == len(min_list):  # last position
                min_list.append(temp)