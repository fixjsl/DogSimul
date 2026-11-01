import random as r

from GlobalEnum import Face_Enum


class Dog:
    def __init__(self, name, feel=60, bored=0):
        self.name = name
        self.feel = feel
        self.bored = bored
        self.state = Face_Enum.NORMAL

    def update_stat(self, feel_change, bored_change):
        self.feel += feel_change
        self.bored += bored_change
        self.control_stat()

    def update_daliy_stat(self):
        feel = r.randint(-20, 20)
        bored = r.randint(-20, 20)
        self.update_stat(feel, bored)
        self.control_stat()
        print(f"기분이 {abs(feel)}만큼 {'증가' if feel >= 0 else '감소'}했다")
        print(f"지루함이 {abs(bored)}만큼 {'증가' if bored >= 0 else '감소'}했다")

    def control_stat(self):
        if self.feel < 0:
            self.feel = 0
        elif self.feel > 100:
            self.feel = 100
        if self.bored < 0:
            self.bored = 0
        elif self.bored > 100:
            self.bored = 100

    def is_dead(self):
        return self.bored >= 100 and self.feel <= 0

    def Dog_feel_check(self):
        if self.feel >= 70 and self.bored < 30:
            self.state = Face_Enum.HAPPY
        elif 30 <= self.feel < 70:
            if self.bored < 30:
                self.state = Face_Enum.NORMAL
            elif 30 <= self.bored < 70:
                self.state = Face_Enum.BORED
            else:
                self.state = Face_Enum.ANGRY
        else:
            self.state = Face_Enum.SAD
