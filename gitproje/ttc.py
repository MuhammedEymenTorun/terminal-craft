#!/usr/bin/env python3
import json as js


class character:
    def __init__(self, name, power, gender, health, hungry, inventory=None):
        self.name = name
        self.power = power
        self.gender = gender
        self.health = health
        self.hungry = hungry
        self.inventory = inventory if inventory else {
            "block": {
                "soil": 0,
                "wood": 0,
                "stone": 0,
                "iron": 0,
                "gold": 0,
                "diamond": 0
            },
            "weapons": [],
            "foods": {
                "cow_meat": 0,
                "sheep_meat": 0,
                "chicken": 0
            }
        }

    def to_dict(self):
        return {
            "name": self.name,
            "power": self.power,
            "gender": self.gender,
            "health": self.health,
            "hungry": self.hungry,
            "inventory": self.inventory
        }


def saving_data(character, filename="data.json"):
    with open(filename, "w") as file:
        js.dump(character.to_dict(), file, indent=4)


def load_game(filename="data.json"):
    with open(filename, "r") as f:
        data = js.load(f)
    return data


class block:
    def __init__(self, type, durability):
        self.type = type
        self.durability = durability


class weopen:
    def __init__(self, type, consist):
        self.type = type
        self.consist = consist


steve = character("steve", 1.5, "male", 10, 10)
alex = character("alex", 1.2, "female", 10, 10)

soil = block("soil", 2)
wood = block("wood", 5)
stone = block("stone", 10)
iron = block("iron", 25)
gold = block("gold", 35)
diamond = block("diamond", 50)

wooden_sword = weopen("wooden_sword", 5)
wooden_pickaxe = weopen("wooden_pickaxe", 5)
wooden_axe = weopen("wooden_axe", 5)
stone_sword = weopen("stone_sword", 10)
stone_pickaxe = weopen("stone_pickaxe", 10)
stone_axe = weopen("stone_axe", 10)
# functions
def welcome_screen():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⡿⠿⠿⠿⠿⠿⠿⢿⠀
⠀⠀⠀⠀⠀⠀⠸⠿⣇⣀⣀⣀⣀⣀⣀⣸⠿⢿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠿⠿⣿⣿⣀⡸⠿⢿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣧⣤⡼⠿⢧⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣿⠛⢻⣿⡇⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣿⠛⠛⠀⢸⣿⡇⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⠛⠛⠀⠀⠀⢸⣿⡇⠀⢸⣿⡇
⠀⠀⠀⠀⢰⣶⣾⣿⣿⣿⠛⠛⠀⠀⠀⠀⠀⠈⠛⢳⣶⡞⠛⠁
⠀⠀⢰⣶⣾⣿⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀
⢰⣶⡎⠉⢹⣿⡏⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣷⣶⡎⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


def steve_view():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣴⠶⠶⠾⠻⢻⡟⠓⠶⠶⢤⣤⣄⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠉⢹⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣤⠤⠤⠔⠒⠒⠒⠋⠉⢹⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⡃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣷⠀⠀⠀⠀⠀⠀⠀⠀⢙⠉⢹⠀⣀⣀⢀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣄⣀⣤⣄⠀⠀⢰⠒⡞⠉⢹⣽⠦⢿⠈⢉⡇⠀⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⣧⢐⣇⣸⡤⠤⢼⠤⠟⠚⠚⢻⠀⠀⠀⠸⣇⠀⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⠋⢀⣸⡧⠤⠼⡖⠒⡄⠀⢸⠀⠀⠀⠀⠈⠉⠧⠤⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⢸⡀⢸⣶⣶⡗⠀⣇⠀⢸⠀⠀⠀⠀⢀⣀⣠⡤⢿⣦⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣤⣤⣤⣾⣷⣮⣷⡦⠶⠶⠾⠦⠾⡶⠒⢻⡏⠉⠁⠀⠀⢸⠀⠙⠳⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⡿⠃⣿⠹⠿⠤⣆⠀⠀⠀⣤⠴⠤⠇⠀⢸⡇⠀⠀⠀⠀⢸⠀⠀⠀⠈⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⣿⠀⠀⠀⠙⠒⠒⠒⠛⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣢⡿⠓⠦⢤⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⣀⣠⣼⣀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠀⠀⢸⠉⠛⠦⣄⣿
⠀⠀⠀⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⢸⠀⠀⠀⠈⣿
⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⢀⡼⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⣠⠏⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⢰⣾⣋⣀⠀⠀⠀⠀⢀⠞⠁⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⠘⠙⢿⣍⠉⠙⠒⠶⣇⠀⠀⠀⢠⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⠀⠀⠀⠙⢷⣄⠀⠀⠈⠳⡄⢠⡟⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠙⠳⠶⠶⠶⠾⠟⠀⢸⡧⠤⠤⠤⠤⠤⠤⢤⡤⠤⠤⠤⠤⣿⠀⠀⠀⠀⢀⣼⡀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢾⡷⠀⠀⠀⠀⠿⣶⣖⡋⠉⠉⠀⠉⠙⠲⣤⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠹⡟⠛⢶⣴⠶⠚⠋⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⣸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⣀⣀⣀⣀⣧⣀⣀⣀⣀⣀⣀⣀⣧⠞⢹⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⠀⠀⢀⣯⠀⠀⠀⠀⠀⠈⠉⡇⢀⣸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⣤⣤⣤⣤⣤⣤⣤⣼⣿⣤⣤⣤⣤⣤⣤⣤⡷⠛⣁⠀⠀⠀⠀⠀⠀
""")

def alex_view():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⡦⠤⠤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠛⠋⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠐⣀⣀⣀⣀⣀⣀⠀⠀⠠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠉⠉⠉⠉⠉⠉⡗⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣶⠒⠺⠛⠀⠀⠀⠀⠀⠀⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⣠⣤⣤⣤⣤⣷⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⢸⣯⠀⣹⣆⢹⡿⠀⠀⠀⣿⡄⣹⡀⣹⣿⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⢸⡏⠉⠉⠉⠉⠁⠀⠀⠀⠉⠉⠉⠉⠛⡗⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⡇⠀⢸⡇⠀⠀⠀⢠⡤⡤⣦⠶⣦⠀⠀⠀⠀⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢸⡀⠀⠀⠀⠀⢸⡇⠀⢸⡇⠀⠀⠀⠘⠷⠶⠾⠶⠿⠀⠀⠀⠀⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⣠⣠⣶⢶⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠛⠒⠶⠾⠷⠶⢶⣦⣠⣼⣷⣶⣾⣷⣤⣤⣤⣤⣦⣧⣴⣤⣦⣶⣶⣴⣾⣧⣼⣿⠀⠀⣀⣠⡄⠀⢀⣠⣶⠾⠛⠉⠛⠿⣇⠀⠈⣧⣹⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠟⢹⠀⠀⠀⠀⠀⠀⠘⡇⡇⠀⠈⠉⠁⠈⠘⠓⠴⠀⠀⠀⠀⠀⡀⢽⣯⠉⢙⣿⣴⠿⠟⠛⠋⢉⣿⡶⠟⠋⠀⠀⠀⠀⠀⠀⣹⣦⡴⠛⠫⢻⣷⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡟⠀⢸⡄⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠸⡟⠛⢻⠀⠀⠀⠀⣿⠛⠛⠁⠀⢸⣧⠀⠀⠀⠀⢀⣼⣿⠆⠀⠀⠀⠀⢀⣤⡴⣦⢈⣯⠀⠀⠀⠀⢹⡟⢷⡀⠘
⠀⠀⠀⠀⢀⣾⠛⣏⠀⢠⣇⣀⣀⣀⣀⣀⠀⢸⡇⠀⠀⠀⠀⠀⡇⠀⠸⠷⠶⠾⠶⠟⠀⠀⠀⠀⠸⡿⣄⣀⣠⠴⠿⢿⣤⣾⣄⣀⡤⣞⣫⣵⡟⠹⠋⠹⣧⡀⠀⠀⠀⢹⡞⣿⣦
⠀⠀⠀⢀⣾⠃⠀⣿⢀⡾⠉⠉⠉⠉⠉⠉⢉⣿⡇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢸⢿⡀⠀⠀⠈⠁⠈⠛⠛⠛⢿⣥⣿⠇⣠⣀⢀⡟⣷⡀⠀⠀⠀⢳⡼⣿
⠀⠀⢠⣾⠃⠀⠀⣿⣿⣀⣀⣀⠀⠀⠀⢠⣿⢳⡇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣸⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⢾⡏⠉⠀⢹⡏⢻⡿⡿⣿⡀⠀⠀⢈⣿⣿
⠀⢠⡿⠃⠀⠀⣠⡏⠉⠉⠉⠙⠛⠛⢻⣿⠃⢸⡟⠛⢻⣇⠤⢴⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⡟⠀⠀⠈⢳⣄⠀⠀⠀⠀⣶⠞⠃⠀⣿⢻⣿⣾⠿⠀⠿⣧⣼⣞⠛⣿⣿
⣠⡿⠁⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⢠⡟⣿⠀⢸⡇⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠘⢧⡀⢐⣶⡿⡷⠀⣤⣾⣷⣿⣧⠀⠀⠀⠙⠋⠻⠿⠟⢿
⣿⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⣠⡟⠀⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⢿⣦⠀⠀⠀⠀⠀⠳⣤⣿⡅⠀⣤⣽⣤⣼⡏⠻⣧⠀⠀⠀⠀⠀⠀⠀⠈
⣿⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⣠⡿⠀⠀⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠹⣷⡀⠀⠀⠀⣀⣹⡏⠁⣀⣻⡀⠘⣯⣁⡤⠿⣷⠀⠀⠀⠀⠀⠀⠀
⢻⣦⠞⠁⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠈⠻⣆⠀⠀⣿⡟⠃⠀⣿⠉⢙⣿⠋⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣤⣄⣀⣀⣀⠀⠀⣴⡟⠀⠀⠀⠀⡟⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⣸⢿⣿⡛⠃⠘⣿⠉⠀⣿⠋⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠛⠋⠀⠀⠀⠀⣤⣷⣀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣰⣿⠀⠀⠀⠀⠸⣿⡿⠄⠀⣤⠾⠀⣾⠛⠀⠀⣀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠈⢻⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠋⠙⠉⢩⣿⠀⠀⠀⠀⠀⠘⣷⣤⣤⣼⣶⣶⠿⠿⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣾⣿⣀⣀⣀⣤⣤⣶⣶⣦⣤⠦⠤⠤⠦⠶⠶⠾⢿⣿⠿⠀⠀⠀⠀⠀⠀⠘⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣷⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⡆⠀⠀⠀⠀⠀⠀⠀⠠⣿⢻⡄⠀⠀⠀⠀⠀⣀⣀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠏⠉⠉⠉⠉⠉⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⣧⠀⠀⠀⠀⠀⠀⠀⠀⠸⣟⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣤⣤⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣇⣀⣀⣀⣀⣀⣀⣀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣾⣿⡉⠉⠉⠉⠉⠉⠉⠉⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⢸⣇⣀⣀⣀⣀⣀⣀⣀⣘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⡞⠁⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

def inventory(character):
    print(f"{character.name} inventory")
    print(character.inventory)
def increase_hunger(character, amount):
    character.hungry += amount
    if character.hungry > 10:
        character.hungry = 10
def decrease_hunger(character, amount):
    character.hungry -= amount
    if character.hungry < 0:
        character.hungry = 0
        while character.health > 0:
            character.health -= 1
            print(f"{character.name} is starving! Health: {character.health}")
            if character.health <= 0:
                print(f"{character.name} has died of starvation.")
                break
def mining(character, block):
    block.durability -= character.power
    if block.durability >=0:
        print(f"{character.name} mined {block.type} block.")
        

# game loop
welcome_screen()
print("Welcome to Termienal craft")
print("-" * 173)

active_player = None

try:
    chosing_character = int(input(f"{steve.name}(1)\n{alex.name}(2)\nseç: "))

    if chosing_character == 1:
        active_player = steve
        saving_data(active_player)
        loaded = load_game()
        steve_view()
        print(f"Selam {loaded['name']}")

    elif chosing_character == 2:
        active_player = alex
        saving_data(active_player)
        loaded = load_game()
        alex_view()
        print(f"Selam {loaded['name']}")

    else:
        print("1 or 2")
        exit()

except ValueError:
    print("sadece sayılar")
    exit()

print(f"Active {active_player.name}")

while True:
    try:
        gaming = int(input("0-exit\n1-braking\n2-inventory\n3-minig\nseç: "))
    except ValueError:
        print("sadece sayılar")
        continue

    if gaming == 1:
        print("Braking is not ready yet.")
    elif gaming == 2:
        inventory(active_player)
    elif gaming == 0:
        import time as t
        dots = "BYE..."
        for i in dots:
            print(i, end=" ")
            t.sleep(0.5)
        exit()
    elif gaming == 3:
        try:
            A = int(input("mining için YES(1)/NO(0)"))
            if A == 1:
                import random as r
                blocks = [soil, wood, stone, iron, gold, diamond]
                rblock = r.choice(blocks)
                try:
                    while True:
                        hit = int(input(f"{rblock.type} block durability: {rblock.durability}\nMine? YES(1)/NO(0)"))
                        if hit == 1:
                            mining(active_player, rblock)
                            if rblock.durability <= 0:
                                print(f"{rblock.type} block mined successfully!")
                                rblock = block(rblock.type, rblock.durability)  # Reset durability for next mining
                                active_player.inventory["block"][rblock.type] += 1
                                break
                        elif hit == 0:
                            print("Mining stopped.")
                            break
                        else:
                            print("1 or 0")
                except ValueError:
                    print("sayılar")
            elif A == 0:
                print("Mining cancelled.")
                exit()
            else:
                print("1 or 0")
        except ValueError:
            print("sayılar")
            
    else:
        print("1, 2, 3 or 0")