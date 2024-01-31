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
                trade_player_instance.official_player_trade()
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
        self.traded_player_name = None
        self.trading_team_ready = False
        self.trading_player_position = None
        self.recieved_player_name = None
        self.recieving_team_name = None
        self.recieving_team_ready = False
        self.recieving_player_position = None
        self.make_trade = None

    def load_players(self):
        with open('players.csv', 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def save_players(self, players):
        with open('players.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(players)

    def validate_team_player(self, team_name, player_name, player_position):
        players = self.load_players()
        for player in players:
            if player[0].title() == team_name and player[1].title() == player_name and \
                    player[2].title() == player_position and player[3].title() == 'True':
                return True
        return False

    def validate_trading_team_input(self):
        print("Follow the instructions to validate information for trading team")
        team_name = str(input("Enter Trading Team Name: ")).title()
        player_name = str(input("Enter Trading Team Player Name: ")).title()
        player_position = str(input("Enter player position: ")).title()

        if self.validate_team_player(team_name, player_name, player_position):
            self.trading_team_ready = True
            self.trading_team_name = team_name
            self.traded_player_name = player_name
            self.trading_player_position = player_position
            print("Trading Team is ready.")

    def validate_receiving_team_input(self):
        print("Follow the instructions to validate information for receiving team")
        team_name = str(input("Enter Receiving Team Name: ")).title()
        player_name = str(input("Enter Receiving Team Player Name: ")).title()
        player_position = str(input("Enter player position: ")).title()

        if self.validate_team_player(team_name, player_name, player_position):
            self.recieving_team_ready = True
            self.recieving_team_name = team_name
            self.recieved_player_name = player_name
            self.recieving_player_position = player_position
            print("Receiving Team is ready.")

    def swap_players(self):
        trading_players = [self.trading_team_name, self.traded_player_name, self.trading_player_position]
        receiving_players = [self.recieving_team_name, self.recieved_player_name, self.recieving_player_position]

        players = self.load_players()
        for player in players:
            if player[:3] == trading_players:
                player[:3] = receiving_players
            elif player[:3] == receiving_players:
                player[:3] = trading_players

        self.save_players(players)
        print("Players swapped successfully.")

    def make_trade_decision(self):
        if self.recieving_team_ready and self.trading_team_ready:
            print("Teams are ready for trade")
            trade_go = str(input("Would you like to make this trade? (yes or no): ")).title()
            self.make_trade = trade_go
            if self.make_trade == 'Yes':
                self.swap_players()
            else:
                print("Trade canceled. Teams are not ready for trade.")

    def official_player_trade(self):
        count = 0
        if count == 0:
            self.validate_trading_team_input()
            count += 1
        if count == 1:
            self.validate_receiving_team_input()
            count += 1
        if count == 2:
            self.make_trade_decision()


        




new_run = Menu()
new_run.run()