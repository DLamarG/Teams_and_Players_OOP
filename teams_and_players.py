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



class TradePlayer:

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

# class TradePlayer(Menu):

#     def __init__(self):
#         self.trading_team_name = None
#         self.traded_player_name = None
#         self.trading_team_ready = False
#         self.trading_player_position = None
#         self.recieved_player_name = None
#         self.recieving_team_name = None
#         self.recieving_team_ready = False
#         self.recieving_player_position = None
#         self.make_trade = None
#         #super().__init__()
    


#     def swap_trading_team_to_recieving_team(self, trading_team_name, trading_player_name, receiving_team_name, receiving_player_name, recieving_player_position, trading_player_position):
#         with open('players.csv', 'r') as file:
#             reader = csv.reader(file)
#             players = list(reader)

#         for player in players:
#             if player[0] == trading_team_name and player[1] == trading_player_name:
#                 print(f"Before: {player}")
#                 player[0] = receiving_team_name
#                 player[1] = receiving_player_name
#                 player[2] = recieving_player_position
#                 print(f"After: {player}")
        
#         print("Modified Players List:", players) 
#         # Update the CSV file with the modified player information
#         with open('players.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(players)


#         with open('players.csv', 'r') as file:
#             reader = csv.reader(file)
#             players = list(reader)

#         for player in players:
#             if player[0] == receiving_team_name and player[1] == receiving_player_name:
#                 print(f"Before: {player}")
#                 player[0] = trading_team_name
#                 player[1] = trading_player_name
#                 player[2] = trading_player_position
#                 print(f"After: {player}")
                

#         # Update the CSV file with the modified player information
#         with open('players.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(players)




#     def validate_trading_team_input(self):
#         depth = 0
#         depth2 = 0
#         depth3 = 0
#         print("Follow the instructions to validate information")
#         if depth == 0:
#             team_name = str(input("Enter Trading Team Name\n")).title()
#             self.trading_team_name = team_name
#             depth += 1
#         if depth == 1:
#             player_name = str(input("Enter Trading Team Player Name\n")).title()
#             self.traded_player_name = player_name
#             depth += 1
#         if depth == 2:
#             player_position1 = str(input("Enter players position\n")).title()
#             self.trading_player_position = player_position1
#             depth += 1
#         if depth == 3:
#             with open('players.csv', 'r') as file:
#                 reader = csv.reader(file)
#                 players = list(reader)
#             for player in players:
#                 if player[0].title() == self.trading_team_name:
#                     depth2 += 1
#                 if player[1].title() == self.traded_player_name:
#                     depth2 += 1
#                 if player[3].title() == 'True':
#                     depth2 += 1
#                 if player[2].title() == self.trading_player_position:
#                     depth2 += 1
#                 if depth2 == 4:
#                     self.trading_team_ready = True
        
#                 if depth == 3:
#                     team_name = str(input("Enter Recieving Team Name\n")).title()
#                     self.recieving_team_name = team_name
#                     depth += 1
#                 if depth == 4:
#                     player_name = str(input("Enter Recieving Team Player Name\n")).title()
#                     self.recieving_player_name = player_name
#                     depth += 1
#                 if depth == 5:
#                     player_position2 = str(input("Enter players position\n")).title()
#                     self.recieving_player_position = player_position2
#                     depth += 1
#                 if depth == 6:
#                     with open('players.csv', 'r') as file:
#                         reader = csv.reader(file)
#                         players = list(reader)
#                     for player in players:
#                         if player[0].title() == self.recieving_team_name:
#                             depth3 += 1
#                         if player[1].title() == self.recieved_player_name:
#                             depth3 += 1
#                         if player[3].title() == 'True':
#                             depth3 += 1
#                         if player[2].title() == self.recieving_player_position:
#                             depth3 += 1
#                         if depth3 == 4:
#                             self.recieving_team_ready = True
        
#         if self.recieving_team_ready == True and self.trading_team_ready == True:
#             print("Teams are ready for trade")
#             trade_go = str(input("Would you like to make this trade?\n yes or no\n")).title()
#             self.make_trade = trade_go
#             if self.make_trade == 'Yes':
#                 # Call the swap_teams_and_players method with the respective team and player names
#                 print("yellow")
#                 self.swap_trading_team_to_recieving_team(self.trading_team_name, self.traded_player_name, self.recieving_team_name, self.recieved_player_name, self.recieving_player_position, self.trading_player_position)
#             else:
#                 print("Teams are not ready for trade")

        






new_run = Menu()
new_run.run()