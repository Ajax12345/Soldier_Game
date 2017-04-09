from Soldier import Soldier
class SoldierElite(Soldier):
    def __init__(self, health, strength, primary_skill, skill_level, run_speed, agility, number_of_soldiers):
        Soldier.__init__(self, health, strength, primary_skill, skill_level, run_speed, agility)
        self.num_soldiers = number_of_soldiers
        self.num_soldiers += 1

        if self.health <= 0:
            self.num_soldiers -= 1

        if self.strength <= 5:
            self.strength = 10

        if self.ammo < 100:
            self.ammo = 500

    def fires_at(self):
        self.ammo -= 50

        self.strength -= 0.2

    def hit(self):
        if self.health == 0:
            self.num_soldiers -= 1

        else:
            self.health -= 20

    def hit_moderate(self):
        if self.health == 0:
            self.num_soldiers -= 1

        else:
            self.health -= 5

    def number_left(self):
        return self.num_soldiers

    def health_checker(self):
        return self.health

    def fatal_hit(self):
        self.num_soldiers -= 1


    def location(self, tundra, desert, forest, wetlands):
        if tundra:
            self.endurance -= 5
            self.run_speed += 50
            self.agility += 50
            self.camo_strength *= 5
        elif desert:
            self.endurance -= 10
            self.strength -= 5
            self.run_speed -= 2
            self.camo_strength *= 2
            self.agility += 10

        elif forest:
            self.camo_strength *= 10
            self.endurance += 5
            self.run_speed += 5
            self.agility += 10
            self.strength += 10

        else:
            self.run_speed += 5
            self.camo_strength *= 7
            self.agility += 40
