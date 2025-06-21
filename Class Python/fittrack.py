class Workout(object):
    def __init__(self, start, end, calories, ):
        self.start = start
        self.end = end
        self.calories = calories
        self.icon = ':)'
        self.workout = 'workout'
    def get_calories(self):
        return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_calories(self):
        return self.calories
    def set_start(self):
        return self.start
    def set_end(self):
        return self.end
    
my_workout = Workout('05.06.2025 1:23 PM', '05.06.2025 2:01 PM', 200)

