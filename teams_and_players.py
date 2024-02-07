import csv
from random import *
import pandas as pd


class Menu():

    def __init__(self):
        self.options = ["List Team Names", "List Team and Coach", "List Team and Coach", "List Teams by Division", "Trade Player", "Fire Current Coach", "Hire new Coach", "Remove Player", "Exit"]


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
                fire_coach = ManageCoaches()
                fire_coach.official_coach_termination()
            if selection == '7':
                 hire_coach = ManageCoaches()
                 hire_coach.official_coach_hire()
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



class TeamInfo():

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




class ManageCoaches:
    def __init__(self):
        self.fired_team_name = None
        self.fired_coach_name = None
        self.ready_to_fire = None
        self.hired_team_name = None
        self.hired_coach_name = None
        self.ready_to_hire = None

    def load_coaches(self):
        with open('teams_and_coaches.csv', 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    
    def load_inactive_coaches(self):
        with open('inactive_coaches.csv', 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def save_coaches(self, coaches, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(coaches)

    def save_inactive_coaches(self, coaches, filename):
        with open(filename, 'a', newline='') as file:  # Use 'a' mode to append to the file
            writer = csv.writer(file)
            for coach in coaches:
                writer.writerow([coach])  # Write each coach's name as a single row



    def validate_fire_coach_input(self, team_name, coach_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if coach[0].title() == team_name and coach[2].title() == coach_name and coach[1].title() == 'Yes':
                return True
        else:
            print("Oops, something went wrong. Please check input and try again!")

    def validate_hire_coach_input(self, team_name, coach_name):
        coaches = self.load_inactive_coaches()
        teams = self.load_coaches()
        for coach in coaches:
            if coach[0].title() == coach_name:
                return True
        else:
            print("Oops, something went wrong. Please check coach name and try again!")

        for team in teams:
            if team[0].title() == team_name and team[2] == "None":
                return True
        else:
            print("Oops, something went wrong. Please check team name and try again!")

    def validate_termination_input(self):
        print("Follow the instructions to validate information for coach termination")
        team_name = input("Enter Team Name: ").title()
        coach_name = input("Enter Coach Name: ").title()

        if self.validate_fire_coach_input(team_name, coach_name):
            self.ready_to_fire = True
            self.fired_team_name = team_name
            self.fired_coach_name = coach_name
            print("Coach is ready for termination.")


    def validate_hire_input(self):
        print("Follow the instructions to hire a new coach")
        team_name = input("Enter Team Name: ").title()
        coach_name = input("Enter Coach Name: ").title()

        if self.validate_hire_coach_input(team_name, coach_name):
            self.ready_to_hire = True
            self.hired_team_name = team_name
            self.hired_coach_name = coach_name
            print("Coach is ready to be hired.")

    def make_termination_decision(self):
        if self.ready_to_fire:
            print("Team is ready to terminate the coach.")
            termination_decision = input("Would you like to terminate this coach? (yes or no): ").title()

            if termination_decision == 'Yes':
                self.terminate_coach()
            else:
                print("Termination canceled. Team is not ready for termination.")

    
    def make_hire_decision(self):
        if self.ready_to_hire:
            print(f"Team is ready to hire ${self.hired_coach_name} the coach.")
            hire_decision = input(f"Would you like to hire Coach ${self.hired_coach_name}? (yes or no): ").title()

            if hire_decision == 'Yes':
                self.hire_coach()
            else:
                print(f"Hire canceled. Team is not ready to hire ${self.hired_coach_name}.")

    def terminate_coach(self):
        coaches = self.load_coaches()
        inactive_coaches = []
        
        for coach in coaches:
            if coach[0].title() == self.fired_team_name and coach[2].title() == self.fired_coach_name:
                if coach[2] not in inactive_coaches:  # Check if coach's name is already in the list
                    inactive_coaches.append(coach[2])  # Add fired coach's name to inactive_coaches list
                coach[2] = "None"

        self.save_coaches(coaches, 'teams_and_coaches.csv')
        self.save_inactive_coaches(inactive_coaches, 'inactive_coaches.csv')
        print(f"Coach {self.fired_coach_name} terminated successfully.")


    def hire_coach(self):
        coaches_and_teams = self.load_coaches()
        # coaches_inactive = self.load_inactive_coaches()
        
        for coach in coaches_and_teams:
            if coach[0].title() == self.hired_team_name and coach[2].title() == "None":
                coach[2] = self.hired_coach_name

        df = pd.read_csv('inactive_coaches.csv')
        df = df.drop(df[df.Coach_Name == self.hired_coach_name].index)
        df.to_csv('inactive_coaches.csv', index=False)

        self.save_coaches(coaches_and_teams, 'teams_and_coaches.csv')
        # self.save_coaches(coaches_inactive, 'inactive_coaches.csv')
        print(f"Coach {self.hired_coach_name} Hired successfully!")



    def official_coach_termination(self):
        count = 0
        if count == 0:
            self.validate_termination_input()
            count += 1
        if count == 1:
            self.make_termination_decision()
            count += 1
        if count == 2:
            count = 0


    def official_coach_hire(self):
        count = 0
        if count == 0:
            self.validate_hire_input()
            count += 1
        if count == 1:
            self.make_hire_decision()
            count += 1
        if count == 2:
            count = 0



new_run = Menu()
new_run.run()