import Soldier
import SoldierElite as elite
import SoldierStandard
import ArmoredPersonelCarrier as carrier
import random

def main():
    soldier = Soldier.Soldier(100, 500, "Infantry", 15, 20, 10)
    while soldier.number_checker() > 0:
        player_answer = False
        print("-----------------------------------------------------------")
        print("Welcome to Keyboard Warrior 1.0!")
        print("Are you a returning user or want to set up a game account? If you are the teacher or administrator, enter your teacher name. ('Returning'/'New') ")
        answer = input()
        if answer == "New":
            setupAccount()

        else:
            while True:
                the_user_name = input("Enter your user name: ")
                flag = validator(the_user_name)
                if flag:
                    print("Successfully logged in")
                    #print("Press 'T' for game tutorial or press 'P' to jump right in!")
                    answer = input("Press 'T' for game tutorial or press 'P' to jump right in!")
                    if answer == 'T':
                        tutorial()

                    else:
                        number_of_soldiers = random.randint(1, 10)
                        #the_next_operation = theaters_of_operation(the_user_name)
                        #if the_next_operation == "Embassy":
                        embassy(the_user_name, number_of_soldiers)
                        #the_next_operation.remove("Embassy")

                        break
                else:
                    print("Not a valid username. Please try again")
                    continue



def tutorial():
    print("Welcome to the first version of this game. The goal of the game is to judiciously deploy troops\n")
    print("to various zones around the world to combat various global insurgencies. This is a game on a massive scale,\n")
    print("so the points will be awarded for the most enemy troops, vehicles, and installations destroyed by your own men in the shortest amount of time")
    print('\n')
def setupAccount():
    current_users = open('the_game_users.txt').readlines()
    current_users = [i.strip('\n') for i in current_users]
    while True:
        user_name = input("Enter your prefered nickname: ")
        if user_name not in current_users:
            file_name = user_name+".txt"
            user_file = open(file_name, 'a')


            f = open('the_game_users.txt', 'w')
            f.write(user_name)
            #f.write("")
            f.write('\n')
            user_file.write("Embassy 0")
            user_file.write('\n')
            print("Thank you for registering. Now, login from the main menu")
            break

        else:
            print("That name already exists. Enter another name")
            continue

def validator(user):
    f = open('the_game_users.txt').readlines()
    f = [i.strip('\n') for i in f]
    return bool(user in f)

def theaters_of_operation(user_name):
    all_scenarios = ["Embassy", "Sudan", "Mogadishu", "Vietnam", "Iraq", "Kabul"]
    full_user_name = user_name+".txt"
    f = open(full_user_name).readlines()
    f = [i.strip('\n') for i in f]
    the_file = [i.split() for i in f]
    levels_so_far = [i[0] for i in the_file]
    need_to_complete = [i for i in all_scenarios if i not in levels_so_far]
    return need_to_complete[0]


def embassy(user_name, soldiers):
    total_score = 0
    the_marine_names = {"Walters": ["Lt", "M4"] , "Thomas":["Sgt", "M4"], "Smith":["LCpl", "M4 with M203"], "Browning":["Pfc", "M27"], "Downing":["Pfc", "M27"], "Brown":["Cpl", "AT-4"]}
    regular_soldier_list = ["Hawking", "McCandish", "Manning", "Pearson", "Rodriguez", "Daniels", "Wright", "Hicks", "Heath", "Conway", "Walton"]
    initialized_soldiers = []
    regular_soldier_number = random.randint(1, 10)
    used_soldiers = []
    for i in range(regular_soldier_number):
        while True:
            soldier = random.choice(regular_soldier_list)
            if soldier not in used_soldiers:
                initialized_soldiers.append(soldier)
                used_soldiers.append(soldier)
                break

            else:
                continue

    the_file_name = user_name+".txt"
    f = open(the_file_name, 'w')
    print("The world is in flames. You are commanding officer the marines guarding the U.S embassy in Sudan")
    print("You are given ", soldiers, " marines and your mission is to defend the U.S compound from assaults.")
    insurgent_weapons = ["RPG", "AK-47", "RPK-74", "Dragunov"]
    compound_fortifications = ["Barracks", "HQ", "West Wall", "North Wall", "East Wall"]
    waves = random.randint(1, 5)
    marines = elite.SoldierElite(100, 500, "Guards", 15, 15, 5, soldiers)
    number_of_attackers = random.randint(20, 100)
    hiding_places = ["roof tops", "cars", "hit and run"]
    air_support_odds = [True, True, True, False, False]
    for i in range(waves):
        weapon = random.choice(insurgent_weapons)
        target = random.choice(compound_fortifications)
        if weapon == "RPG":
            if target == "Barracks":
                marines.hit()

            elif target == "HQ":
                marines.hit()

            elif target == "West Wall":
                marines.hit_moderate()

            elif target == "North Wall":
                marines.hit_moderate()

            elif target == "East Wall":
                marines.hit_moderate()

        elif weapon == "Ak-47":
            if target == "Barracks":
                marines.hit_moderate()

        elif weapon == "RPK-74":
            if target == "Barracks":
                marines.hit_moderate()

            elif target == "HQ":
                marines.hit_moderate()

            elif target == "West Wall" or target == "North Wall" or target == "East Wall":
                marines.hit()

        else:
            if target == "West Wall" or target == "East Wall" or target == "North Wall":
                marines.fatal_hit()

            else:
                marines.hit()

        print("You have lost ", abs(soldiers-marines.number_left()), " marines. Continue the fight!")
        contact1 = random.choice(hiding_places)
        contact2 = random.choice(hiding_places)
        contact3 = random.choice(hiding_places)
        print("Marines returning fire")
        if contact1 == "cars" or contact2 == "cars" or contact3 == "cars":
            marines.fires_at()
            number_of_attackers -= 5

        if contact2 == "roof tops" or contact1 == "roof tops" or contact3 == "roof tops":
            marines.fires_at()
            number_of_attackers -= 10

        if contact1 == "hit and run" or contact2 == "hit and run" or contact3 == "hit and run":
            marines.fires_at()
            number_of_attackers -= 2

        stryker = carrier.ArmoredPersonellCarrier(marines.number_left, True, False, 100, the_marine_names)
        if marines.number_left() > 0 and marines.number_left() < 2:
            print("You are running short of men. Do you want to call for air support or evacuate (A/E) ")
            answer = input()
            if answer == "A":
                if random.choice(air_support_odds):
                    print("Support on the way. Nice work commander!")
                    f.write(str(10))

                else:
                    print("Request denied. Prepare to evacuate")
                    stryker = carrier.ArmoredPersonellCarrier(marines.number_left, True, False, 100, the_marine_names)
                    the_names = the_marine_names.keys()
                    info = the_marine_names.values()
                    for i in range(len(the_names)):
                        stryker.add_soldier(the_names[i], info[i])

                    stryker.add_soldier("Bridgefield", ["Capt", "M4"])
                    stryker.add_soldier("Hunter", ["Sgt", "M16 with M203"])
            else:
                stryker = carrier.ArmoredPersonellCarrier(marines.number_left, True, False, 100, )
                the_names = the_marine_names.keys()
                info = the_marine_names.values()
                for i in range(len(the_names)):
                    stryker.add_soldier(the_names[i], info[i])

                    stryker.add_soldier("Bridgefield", ["Capt", "M4"])
                    stryker.add_soldier("Hunter", ["Sgt", "M16 with M203"])

                f.write(str(8))

        else:
            print("Attack Repulsed! Nice work commander!")
            total_score += 20
            print("Your total score is ", total_score)

            f.write(str(total_score))
            f.write('\n')





main()
