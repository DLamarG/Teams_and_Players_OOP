import csv
from random import *
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
                 hire_coach.official_coach_hiring()
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




class ManageCoaches(Menu):

    def __init__(self):
        self.fired_team_name = None
        self.fired_coach_name = None
        self.hire = None
        self.fire = None
        self.ready_to_hire = None
        self.ready_to_fire = None
        self.hired_team_name = None
        self.hired_coach_name = None
        self.finalize_firing = None
        self.finalize_hiring = None


    def load_coaches(self):
        with open('coaches.csv', 'r') as file:
            reader = csv.reader(file)
            return list(reader)
        

    def save_coaches(self, coaches):
        with open('coaches.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(coaches)


    def validate_active_coach(self, fired_coach_name, fired_team_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if coach[2].title() == fired_coach_name and coach[1].title() == 'Yes' and coach[0] == fired_team_name:
                return True
        else:
            print("Woops somthing went wrong, please check input and try again!")

    def validate_active_coach_input(self):
        print("Follow the instructions to validate information for coach being fired")
        team_name = str(input("Enter Team Name: ")).title()
        coach_name = str(input("Enter Coach Name: ")).title()

        if self.validate_active_coach(coach_name, team_name):
            self.ready_to_fire = True
            self.fired_coach_name = coach_name
            self.fired_team_name = team_name
            print("Active Coach is ready.")

    
    def validate_inactive_coach(self, hired_coach_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if  coach[2].title() == hired_coach_name and coach[1].title() == 'No':
                return True
        else:
            print("Woops somthing went wrong, please check input and try again!")


    def validate_new_team_recieving_coach(self, hired_team_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if  coach[0].title() == hired_team_name and coach[2] == 'None':
                return True
        else:
            print("Woops somthing went wrong, please check input and try again!")

    def validate_inactive_coach_input(self):
        print("Follow the instructions to validate information for coach being fired")
        coach_name = str(input("Enter Coach Name: ")).title()
        team_name = str(input("Enter Team Name")).title()
        
        if self.validate_inactive_coach(coach_name) and self.validate_new_team_recieving_coach(team_name):
            self.hired_coach_name = coach_name
            self.hired_team_name = team_name
            print("In-active Coach is ready.")

    
    def make_fire_decision(self):
        if self.ready_to_fire:
            print("Team is ready for fire the current coach.")
            fire_go = str(input("Would you like to terminate this coach? (yes or no): ")).title()
            self.finalize_firing = fire_go
            if self.finalize_firing == 'Yes':
                self.fire_coach(self.fired_coach_name)
            else:
                print("Termination canceled. Team is not ready for termination.")

    
    def make_hire_decision(self):
        if self.ready_to_fire:
            print("Team is ready for hire the current coach.")
            fire_go = str(input("Would you like to hire this coach? (yes or no): ")).title()
            self.finalize_firing = fire_go
            if self.finalize_firing == 'Yes':
                self.hire_coach()
            else:
                print(f"Hire canceled. Team is not ready to hire ${self.hired_coach_name}.")



    def fire_coach(self, fired_coach_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if coach[2] == fired_coach_name:
                coach[2] == "None"
                coach[1] == "No"
        
        self.save_coaches(coaches)
        print(f"Coach ${self.fired_coach_name} fired successfully.")


    def hire_coach(self, hired_coach_name, hired_team_name):
        coaches = self.load_coaches()
        for coach in coaches:
            if coach[0] == hired_team_name:
                coach[2] == hired_coach_name
                coach[1] == "Yes"
        
        self.save_coaches(coaches)
        print(f"Coach ${self.hired_coach_name} hired successfully.")



    def official_coach_termination(self):
        count = 0
        if count == 0:
            self.validate_active_coach_input()
            count += 1
        if count == 1:
            self.make_fire_decision()
            count += 1
        if count == 2:
            count = 0


    def official_coach_hiring(self):
        count = 0
        if count == 0:
            self.validate_inactive_coach_input()
            count += 1
        if count == 1:
            self.make_hire_decision()
            count += 1
        if count == 2:
            count = 0



        

new_run = Menu()
new_run.run()