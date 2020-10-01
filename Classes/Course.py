class Course:

    # init for Course
    def __init__(self, name, points, grade):
        self.name = name
        self.points = points
        self.grade = grade
        self.enabled = True

    # set flag bool
    def set_flag(self, enabled):
        self.enabled = enabled
