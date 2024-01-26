import csv
from random import *
class Menu:

    def __init__(self):
        self.options = ["List Team Names", "List Players on Team", "List Players Stats", "List Teams by Division", "Trade Player", "List Trades by Team", "Add New Player", "Remove Player" "Exit"]


    def display_menu(self):
        print()
        print(" == Welcome to Player Trader! == ")
        print()
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
        print()


    def get_user_choice(self):
            selection = str(input(  "Select an option\n"))
            print()
            if selection == '1':
                TeamInfo.print_team_name_to_screen()
            if selection == '2':
                pass
            if selection == '3':
                 pass
            if selection == '4':
                pass
            if selection == '5':
                pass
            if selection == '6':
                pass
            if selection == '7':
                 exit()
            print()
            print()
            self.display_menu()
            self.get_user_choice()
            

    def play(self):
            self.display_menu()
            self.get_user_choice()
 

    def run(self):
        self.play()



class TeamInfo:

    def __init__(self):
          self.inventory = None

    @classmethod
    def print_team_name_to_screen(cls):
        with open("Teams.csv", 'r') as csvfile:
            teams = csv.DictReader(csvfile)
            for row in teams:
                print()
                print(f" Team_Name: {row['Team_Name']}")
                print()





new_run = Menu()
new_run.run()