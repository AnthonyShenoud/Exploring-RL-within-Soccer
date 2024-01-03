from colorama import Fore
from prettytable import PrettyTable

def get_stats(list_of_players):
    # Initializing statistics for both teams
    team1_stats = {"Goals": 0, "Shots": 0, "Shots_on_target": 0, "Successful_passes": 0, "Failed_passes": 0,
                   "Successful_crosses": 0, "Failed_crosses": 0, "Duels_won": 0, "Duels_lost": 0, "Saves": 0,
                   "Interceptions": 0}
    team2_stats = {"Goals": 0, "Shots": 0, "Shots_on_target": 0, "Successful_passes": 0, "Failed_passes": 0,
                   "Successful_crosses": 0, "Failed_crosses": 0, "Duels_won": 0, "Duels_lost": 0, "Saves": 0,
                   "Interceptions": 0}

    # Iterating through the list of players
    for player in list_of_players:
        # Assigning the player to team 1 if their number is less than or equal to 10, otherwise to team 2
        if player.number <= 10:
            team_stats = team1_stats
        else:
            team_stats = team2_stats
        
        # Updating the corresponding team's statistics based on the player's stats
        team_stats["Goals"] += player.return_goals()
        team_stats["Shots"] += player.return_shots()
        team_stats["Shots_on_target"] += player.return_shots_on_target()
        team_stats["Successful_passes"] += player.return_successful_passes()
        team_stats["Failed_passes"] += player.return_failed_passes()
        team_stats["Successful_crosses"] += player.return_successful_crosses()
        team_stats["Failed_crosses"] += player.return_failed_crosses()
        team_stats["Duels_won"] += player.return_duels_won()
        team_stats["Duels_lost"] += player.return_duels_lost()
        team_stats["Saves"] += player.return_goalkeeping()
        team_stats["Interceptions"] += player.return_interceptions()
    
    # Returning the statistics for both teams
    return team1_stats, team2_stats

def display_stats(team1_stats, team2_stats, team1_name, team2_name, text):
    # Displaying statistics for both teams
     
    table = PrettyTable()
    table.padding_width = 5

    table.field_names = [f"{Fore.CYAN}{text[1]}", team1_name, team2_name + Fore.RESET]

    for i, element in enumerate(team1_stats):
        table.add_row([Fore.CYAN + text[i+2] + Fore.RESET, team1_stats[element], team2_stats[element]])

    print(table)

def reset_stats(list_of_players):
    for player in list_of_players:
        # Updating the corresponding team's statistics based on the player's stats
        player.goals = 0
        player.shots_on_target = 0
        player.total_shots = 0
        player.successful_passes = 0
        player.failed_passes = 0
        player.successful_crosses = 0
        player.failed_crosses = 0
        player.duels_won = 0
        player.duels_lost = 0
        player.goalkeeping = 0
        player.interceptions = 0
        player.successful_clearances = 0
        player.failed_clearances = 0
