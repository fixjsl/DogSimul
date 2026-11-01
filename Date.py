class Date:
    def __init__(self, day=1, period="아침", try_chance=3):
        self.day = day
        self.period = period
        self.try_chance = try_chance

    def update_time(self):
        self.try_chance -= 1
        if self.try_chance == 2:
            self.period = "점심"
        elif self.try_chance == 1:
            self.period = "저녁"
        elif self.try_chance == 0:
            self.day += 1
            self.try_chance = 3
            self.period = "아침"
            return True
        return False
