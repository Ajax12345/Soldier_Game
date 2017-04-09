class Soldier:
    def __init__(self, health, strength, primary_skill, skill_level, run_speed, agility):
        self.health = health
        self.strength = strength
        self.primary_skill = "Infantry"
        self.skill_level = skill_level
        self.run_speed = run_speed
        self.agility = agility
        self.num_soldiers = 6
        self.ammo = 500
        self.endurance = 100
        self.camo_strength = 100
        self.squad_roles = {"Lt": ["Lt. Walters", "M4"] , "Sgt":["Sgt. Thomas", "M4"], "Grenadier":["LCpl Smith", "M4 with M203"], "Rifleman":["Pfc Browning", "M27"], "Rifleman":["Pfc Downing", "M27"], "Support":["Cpl Brown", "AT-4"]}

    def fires_at(self):
        self.ammo -= 100
        self.strength -= 0.5



    def hit(self):
        if self.health == 0:
            self.num_soldiers -= 1

        else:
            self.health -= 1

    def location(self, tundra, desert, forest, wetlands):
        if tundra:
            self.endurance -= 20
            self.run_speed += 10
            self.agility += 30
            self.camo_strength += 5

        elif desert:
            self.endurance -= 30
            self.strength -= 50
            self.run_speed -= 10
            self.camo_strength -= 10
            self.agility += 1

        elif forest:
            self.camo_strength += 40
            self.endurance -= 5
            self.run_speed -= 5
            self.agility -= 2
            self.strength -= 10

        else:
            self.run_speed -= 2
            self.camo_strength +=10
            self.agility -= 20

    def number_checker(self):
        return self.num_soldiers


    def view_soldiers_profile(self, position):
        print("Name:", self.squad_roles[position][0])
        print("Primary Weapon:", self.squad_roles[position][1])
        print("Unit:", self.primary_skill)
