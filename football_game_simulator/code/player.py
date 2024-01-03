import random
from colorama import Fore

class Player():
    """Player Class: Creates players for two teams, numbered from 0 to 21."""    
    def __init__(self, name, position, number, pass_skill, shot_skill, goalkeeping, cross_skill, dribble_skill, defense_skill, interception_skill, adversary, color1, color2, disposition, adversary_disposition, text):
        self.name = name
        self.position = position
        self.number = number
        self.pass_skill = pass_skill
        self.shot_skill = shot_skill
        self.goalkeeping_skill = goalkeeping
        self.cross_skill = cross_skill
        self.dribble_skill = dribble_skill
        self.defense_skill = defense_skill
        self.interception_skill = interception_skill
        self.color1 = color1
        self.color2 = color2
        
        self.adversary = adversary  # Opponents with whom the player will have most duels (same positions)
        self.disposition = disposition
        self.adversary_disposition = adversary_disposition
        
        self.text = text
        
        # Stats for the match
        self.goals = 0
        self.shots_on_target = 0
        self.total_shots = 0
        self.successful_passes = 0
        self.failed_passes = 0
        self.successful_crosses = 0
        self.failed_crosses = 0
        self.duels_won = 0
        self.duels_lost = 0
        self.goalkeeping = 0
        self.interceptions = 0
        self.successful_clearances = 0
        self.failed_clearances = 0
        
        self.minute = "(0min)"
    
    # Function to retrieve player information
    def return_name(self):
        return self.name

    def return_goalkeeping_rating(self):
        return self.goalkeeping_skill
    
    def return_defense_rating(self):
        return self.defense_skill
    
    def return_interception_rating(self):
        return self.interception_skill
    
    def goalkeeping_save(self):
        self.goalkeeping += 1 
        
    def Duels_won(self):
        self.duels_won += 1 
        
    def Duels_lost(self):
        self.duels_lost += 1
        
    def successful_interception(self):
        self.interceptions += 1
        
    # Statistics
    
    def return_shots(self):
        return self.total_shots
    
    def return_shots_on_target(self):
        return self.shots_on_target
    
    def return_goals(self):
        return self.goals
    
    def return_successful_passes(self):
        return self.successful_passes
    
    def return_failed_passes(self):
        return self.failed_passes
    
    def return_successful_crosses(self):
        return self.successful_crosses
    
    def return_failed_crosses(self):
        return self.failed_crosses
    
    def return_interceptions(self):
        return self.interceptions 
    
    def return_duels_won(self):
        return self.duels_won
    
    def return_duels_lost(self):
        return self.duels_lost
    
    def return_goalkeeping(self):
        return self.goalkeeping
        
    def random_action(self, time, list_player):
        """Main function called for each action:
        - No input parameters
        - Outputs the player number now in possession of the ball
        This function varies based on the player's position."""
        self.minute = int(time)
        self.minute = f"({self.minute} min)"
        self.list_player = list_player
        
        # Code executed when the player receives the ball
        if self.position == "AC":
            random_action = random.randint(0,42)
            if random_action == 1:
                # Shot in the penalty area
                return self.shot_inside_box(self.list_player, self.minute)
            elif random_action == 2:
                return self.shot_outside_box()
            elif random_action == 3 or random_action == 4:
                return self.short_pass()
            elif random_action <= 7:
                return self.duel()
            else:
                return self.pass_action()
        
        # Other positions have similar actions following the same logic...
        # Continuing the logic for other positions (AG, AD, MC, DD, DG, DC, GK)...
        
        elif self.position == "AG" or self.position == "AD":
            random_action = random.randint(0,55)
            if random_action == 2:
                return self.shot_inside_box(self.list_player, self.minute)
            elif random_action <= 4:
                return self.shot_outside_box()
            elif random_action <= 8:
                return self.cross()
            elif random_action <= 13:
                return self.short_pass()
            elif random_action == 30:
                return self.duel()
            else:
                return self.pass_action()
        
        elif self.position == "MC":
            random_action = random.randint(0,90)
            if random_action == 1:
                return self.shot_outside_box()
            elif random_action <= 15:
                return self.short_pass()
            elif random_action <= 20:
                return self.duel()
            else:
                return self.pass_action()
        
        elif self.position == "DD" or self.position == "DG":
            random_action = random.randint(0,40)
            if random_action == 1:
                return self.cross()
            elif random_action <= 15:
                return self.short_pass()
            elif random_action <= 18:
                return self.duel()
            else:
                return self.pass_action()
        
        elif self.position == "DC":
            random_action = random.randint(0,20)
            if random_action <= 3:
                return self.short_pass()
            elif random_action == 4:
                return self.clearance()
            elif random_action == 6:
                return self.duel()
            else:
                return self.pass_action()
        
        else:  # Goalkeeper
            random_action = random.randint(0,6)
            if random_action == 1:
                return self.short_pass()
            elif random_action == 2:
                return self.clearance()
            else:
                return self.pass_action()
    
    def pass_action(self): 
        self.action = self.number 
        random_rating = random.randint(0,95)  # Random rating to determine success
        
        if random_rating > self.pass_skill:
            # Failed pass
            if self.number <= 10:   
                self.action = random.randint(11,21)
            else:
                self.action = random.randint(0,10)
            
            self.failed_passes += 1
        
        else:  # Successful pass 
            # Now check if it's intercepted
            
            defender = self.adversary
            
            # Choose the opponent who can intercept the pass 
            opponent = random.choice(defender)
            defense_rating = self.list_player[opponent].return_interception_rating()
            
            random_rating = random.randint(0,5000)
            
            if random_rating > defense_rating:
                if self.number <= 10:           
                    while self.action == self.number : 
                        self.action = random.randint(0,10)
                else:
                    while self.action == self.number : 
                        self.action = random.randint(11,21)
                    
                self.successful_passes += 1 

            else:
                self.action = opponent
                self.failed_passes += 1
                self.list_player[self.action].successful_interception() 
    
        return self.action

    def shot_inside_box(self, list_player, time):
        self.list_player = list_player
        self.minute = time
        random_rating = random.randint(0,140)
        self.total_shots += 1      
        
        if random_rating > self.shot_skill: 
            # Missed shot
            if self.number <= 10:
                self.action = 11
            else:
                self.action = 0
                # Giving the ball to the opposing goalkeeper 
            #print(self.color1 + self.name + self.text[0][0] + self.minute + Fore.RESET)
        
        else:
            # Shot on target 
            # Check if the opposing goalkeeper makes the save or not         
            if self.number <= 10:
                opponent_goalkeeper_rating = self.list_player[11].return_goalkeeping_rating()
                goalkeeper_number = 11
                engagement = 21  # Indicator for a goal and who's starting the engagement
            else:
                opponent_goalkeeper_rating = self.list_player[0].return_goalkeeping_rating()
                goalkeeper_number = 0
                engagement = 11
            
            random_rating = random.randint(0,130)  # Determine if the goalkeeper stops it
            
            if random_rating > opponent_goalkeeper_rating:
                # Goal in the box
                #print("\n" + self.color2 + self.name + self.text[1][0] + self.minute + Fore.RESET + "\n")
                self.action = engagement
                self.goals += 1
                self.shots_on_target += 1
               

            else:
                # Goalkeeper saves, they keep the ball 
                self.action = goalkeeper_number
                #print(self.color1 + self.name + self.text[2][0] + self.minute + Fore.RESET + "\n")
                self.shots_on_target += 1
                self.list_player[self.action].goalkeeping_save()  # Increase goalkeeper's save count
          
        return self.action
    
    
    def shot_outside_box(self):
        random_rating = random.randint(0,160) 
        self.total_shots += 1
        
        if random_rating > self.shot_skill: 
            # Missed shot
            if self.number <= 10:
                self.action = 11
            else:
                self.action = 0
            #print(self.color1 + self.name + self.text[3][0] + self.minute + Fore.RESET + "\n")
        
        else:
            # Shot on target 
            # Check if the opposing goalkeeper makes the save or not         
            if self.number <= 10:
                opponent_goalkeeper_rating = self.list_player[11].return_goalkeeping_rating()
                goalkeeper_number = 11
                
                engagement = 21  # Indicator for a goal and who's starting the engagement
            else:
                opponent_goalkeeper_rating = self.list_player[0].return_goalkeeping_rating() + random.randint(0,6)
                goalkeeper_number = 0
                engagement = 11
            
            random_rating = random.randint(0,100)  # Determine if the goalkeeper stops it
            
            if random_rating > opponent_goalkeeper_rating:
                # Goal scored 
                #print("\n" + self.color2 + self.name + self.text[4][0] + self.minute + Fore.RESET + "\n")
                self.action = engagement
                self.goals += 1
                self.shots_on_target += 1
             

            else:
                # Goalkeeper saves, they keep the ball 
                self.action = goalkeeper_number
                #print(self.color1 + self.name + self.text[5][0] + self.minute + Fore.RESET + "\n")
                self.shots_on_target += 1
                self.list_player[self.action].goalkeeping_save()
          
        return self.action
    
    
    def cross(self):
        random_rating = random.randint(0,75)
        
        if random_rating > self.cross_skill: 
            # Goes out for a goal kick 
            if self.number <= 10:
                self.action = 11
            else:
                self.action = 0
            #print(self.color1 + self.name + self.text[6][0] + self.minute + Fore.RESET + "\n")
            self.failed_crosses += 1

        else:
            # Successful cross
            self.action = self.number
            if len(self.disposition[-1]) >= 2:  
                while self.action == self.number:
                    self.action = random.choice(self.disposition[-1])
            else:
                while self.action == self.number:
                    self.action = random.choice(self.disposition[-1] + self.disposition[-2])
                    
            # Check if it's intercepted
            defender = random.choice(self.adversary_disposition[1])
            defense_rating = self.list_player[defender].return_interception_rating() + (len(self.adversary_disposition[1])*3)
            
            random_rating = random.randint(0,160)
            
            if random_rating > defense_rating:
                #print(self.color1 + self.name + self.text[7][0] + self.list_player[self.action].return_name() + self.minute + Fore.RESET)
                self.successful_crosses += 1 
                return self.list_player[self.action].shot_inside_box(self.list_player, self.minute)  # Must shoot as the defender didn't touch it 


            else:
                self.action = defender
                #print(self.color1 + self.name + self.text[8][0][0] + self.list_player[int(self.action)].return_name() + self.text[8][1][0] + self.minute + Fore.RESET)
                self.failed_crosses += 1
                self.list_player[self.action].successful_interception()
    
        return self.action

    def short_pass(self):

        random_rating = random.randint(0,95)  # Random note to determine if the action succeeds
        
        if random_rating > self.pass_skill:
            # Failed pass
            self.action = random.choice(self.adversary)
            self.failed_passes += 1
        
        else:
            if self.number == 0 or  self.number == 11:            
                self.action = self.number + 1
                # Can't pass to the player further down as they're goalkeepers
            
            elif self.number == 10 or  self.number == 21:            
                self.action = self.number - 1
                # Can only pass to the player in front as there's nobody else after
            
            else:
                random_rating = random.randint(0,1)
                if random_rating == 0:
                    self.action = self.number - 1
                else:
                    self.action = self.number + 1
                    
            self.successful_passes += 1
        
        return self.action
    
    
    def clearance(self):

        random_rating = random.randint(0,130)  # Random note to determine if the action succeeds
        
        if random_rating > self.pass_skill:
            # Failed clearance
            if self.number <= 10:   
                self.action = random.randint(12,18)
            else:
                self.action = random.randint(1,7)
            
        else:
            # Check if it's intercepted
            
            defender = self.adversary
            
            # Choosing the defender who might intercept the clearance 
            opponent = random.choice(defender)
            interception_rating = self.list_player[opponent].return_interception_rating()  # Retrieving the chosen defender's interception rating 
            
            random_rating = random.randint(0,125)
            
            if random_rating > interception_rating: # The pass isn't intercepted 
                    
                # Successful clearance
                self.action = self.number
                
                if self.number <= 10:   
                    while self.action == self.number:
                        self.action = random.randint(1,7)
                else:
                    while self.action == self.number:
                        self.action = random.randint(12,18)
                
           
            else: # The defender intercepts it 
                self.action = opponent
                self.list_player[self.action].successful_interception()
        
        return self.action 
    
    
    def duel(self):
        random_zone = random.randint(0,5)
        if random_zone == 2:
            if self.number <= 10:  
                opponent = random.randint(12,21)
            else:
                opponent = random.randint(1,10)
        else:
            opponent = random.choice(self.adversary)
        
        opponent_defense = self.list_player[opponent].return_defense_rating()
        attack_rating = self.dribble_skill + random.randint(0,5)
        opponent_defense += random.randint(0,5)
        
        if attack_rating >= opponent_defense:
            # Successful dribble
            self.action = self.number
            
            self.duels_won += 1 
            
            self.list_player[opponent].Duels_lost()
            if random.randint(1,5) == 2:
                abc = 1
                #print(self.name + self.text[9][0][0] + self.list_player[opponent].return_name() + self.text[9][1][0] + self.minute)
        else:
            # Lost duel 
            self.action = opponent
            self.duels_lost += 1
            self.list_player[self.action].Duels_won()
            if random.randint(1,5) == 2:
                abc = 1
                #print(self.name + self.text[10][0] + self.list_player[opponent].return_name() + self.minute)
        
        return self.action

