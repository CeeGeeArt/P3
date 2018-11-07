class Team:
    points = 0
    name = ""

    # constructor
    def __init__(self, name):
        self.name = name

    # Getters
    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

    # Setters / add one point
    # setName only relevant if the teams should be able to change their names.
    def setName(self, name):
        self.name = name

    def setPoints(self, points):
        self.points = points

    def addPoint(self):
        self.points += 1