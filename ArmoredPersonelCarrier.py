class ArmoredPersonellCarrier:
    def __init__(self, CurrentNumberofOccupants, with_machinegun, with_grenade_launcher, mines_factor, soldiers):
        self.armor_level = 100
        self.weight = 38000
        self.ammo = 5
        self.soldiers = soldiers #stored as a dictionary with name as key and rank with primary weapon as values
        if mines_factor > 5:
            self.weight += 5000

            self.armor_level *= 8

        if with_machinegun:
            self.ammo += 2000

        if with_grenade_launcher:
            self.ammo += 100

        self.occupants = [i for i in soldiers.keys()]

        self.CurrentNumberofOccupants = len(self.occupants)

    def remove_soldier(self, name):
        del self.soldiers[name]


    def add_soldier(self, name, other_info):
        self.soldiers[name] = other_info
