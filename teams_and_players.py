import csv
from random import *
class Menu():

    def __init__(self):
        self.options = ["List Team Names", "List Team and Coach", "List Team and Coach", "List Teams by Division", "Trade Player", "List Trades by Team", "Add New Player", "Remove Player", "Exit"]


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
                TeamInfo.print_team_name_and_coach_to_screen()
            if selection == '3':
                TeamInfo.print_team_division_coach_to_screen()
            if selection == '4':
                pass
            if selection == '5':
                trade_player_instance = TradePlayer()
                trade_player_instance.validate_trading_team_input()
            if selection == '6':
                pass
            if selection == '7':
                 pass
            if selection == '8':
                 pass
            if selection == '9':
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

    @classmethod
    def print_team_name_and_coach_to_screen(cls):
        with open("Teams.csv", 'r') as csvfile:
            teams = csv.DictReader(csvfile)
            for row in teams:
                print()
                print(f"Team_Name: {row['Team_Name']}")
                print(f"Coach: {row['Coach']}")
                print()


    @classmethod
    def print_team_division_coach_to_screen(cls):
        with open("Teams.csv", 'r') as csvfile:
            teams = csv.DictReader(csvfile)
            for row in teams:
                print()
                print(f"Team: {row['Team_Name']}")
                print(f"Coach: {row['Coach']} ")
                print(f"Division: {row['Division']}")
                print()



class TradePlayer(Menu):

    def __init__(self):
        self.trading_team_name = None
        self.recieving_team_name = None
        self.traded_player_name = None
        self.recieved_player_name = None
        self.trading_team_ready = False
        self.recieving_team_ready = False
        # super().__init__()


    # def rent_video(self):
    #     movies = []
    #     count1 = 0
    #     print("Please enter the following information to check availability of your video")
    #     if count1 == 0:
    #         input1 = str(input( "Enter Account ID\n"))
    #         self.customer_id = input1
    #         count1 += 1
    #     if count1 == 1:
    #         input2 = str(input( "Enter Movie Title\n"))
    #         self.movie_title = input2.title()
    #         count1 += 1
    #     with open('inventory.csv', 'r') as file:
    #         reader = csv.reader(file)
    #         movies = list(reader)
    #     for movie in movies:
    #         if movie[1].title() == self.movie_title.title():
    #             if movie[2] > '0':
    #                 pass

    def validate_trading_team_input(self):
        depth = 0
        depth2 = 0
        depth3 = 0
        print("Follow the instructions to validate information")
        if depth == 0:
            team_name = str(input("Enter Trading Team Name\n"))
            self.trading_team_name = team_name
            depth += 1
        if depth == 1:
            player_name = str(input("Enter Trading Team Player Name\n"))
            self.traded_player_name = player_name
            depth += 1
        if depth == 2:
            with open('players.csv', 'r') as file:
                reader = csv.reader(file)
                players = list(reader)
            for player in players:
                if player[0].title() == self.trading_team_name.title():
                    depth2 += 1
                if player[1].title() == self.traded_player_name.title():
                    depth2 += 1
                if player[3].title() == True:
                    depth2 += 1
                if depth2 == 3:
                    self.trading_team_ready = True
        
        if depth3 == 0:
            team_name = str(input("Enter Recieving Team Name\n"))
            self.trading_team_name = team_name
            depth += 1
        if depth3 == 1:
            player_name = str(input("Enter Recieving Team Player Name\n"))
            self.traded_player_name = player_name
            depth += 1
        if depth3 == 2:
            with open('players.csv', 'r') as file:
                reader = csv.reader(file)
                players = list(reader)
            for player in players:
                if player[0].title() == self.recieving_team_name.title():
                    depth2 += 1
                if player[1].title() == self.recieved_player_name.title():
                    depth2 += 1
                if player[3].title() == True:
                    depth2 += 1
                if depth2 == 3:
                    self.recieved_team_ready = True
        
        








new_run = Menu()
new_run.run()