class Motorfordon:
    def __init__(self, max_speed):
        self.max_speed = max_speed
class Fyrhjuling:
    def __init__(self, wheel_radius):
        self.wheel_radius = wheel_radius
class Bil(Motorfordon, Fyrhjuling):
    def __init__(self, max_speed, wheel_radius):
        Motorfordon.__init__(self, max_speed)
        Fyrhjuling.__init__(self, wheel_radius)
b = Bil(120, 15)
print(b.max_speed)      # 120
print(b.wheel_radius)   # 15
