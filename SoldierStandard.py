from Soldier import Soldier

class SoldierStandard(Soldier):
    def __init__(self, health, strength, primary_skill, skill_level, run_speed, agility, number_of_soldiers):
        Soldier.__init__(self, health, strength, primary_skill, skill_level, run_speed, agility)
        self.num_soldiers += 1
        if self.health <= 0:
            self.num_soldiers -= 1

    def fires_at(self):
        self.ammo -= 100

        self.strength -= 4

    def hit(self):
        if self.health == 0:
            self.num_soldiers -= 1

        else:
            self.health -= 4


    def location(self, tundra, desert, forest, wetlands):
        if tundra:
            self.endurance -= 40
            self.run_speed += 10
            self.agility += 20
            self.camo_strength += 20
        elif desert:
            self.endurance -= 20
            self.strength -= 50
            self.run_speed -= 30
            self.camo_strength += 5
            self.agility += 10

        elif forest:
            self.camo_strength *= 3
            self.endurance - 1
            self.run_speed += 4
            self.agility -=10
            self.strength -= 10

        else:
            self.run_speed += 5
            self.camo_strength *= 2
            self.agility -= 20
