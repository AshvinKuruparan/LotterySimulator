import numpy as np
#0.0000000300347201
class LotterySimulation:
    def __init__(self, odds_of_winning = 0.000000030034720,  weeks_to_simulate = 520):
        self.weeks_to_simulate = weeks_to_simulate
        self.odds = odds_of_winning
        self.money_spent = 0
        self.money_earned = 0
        
    #def __init__(self, odds, weeks):
     #   self.odds = odds
      #  self.weeks_to_simulate = weeks
    def play_lottery(self):
        tickets = np.random.rand()
        if tickets<= self.odds:
            return True
        return False
        
    def run (self):
        if self.weeks_to_simulate > 0:
            for iteration in range(self.weeks_to_simulate):
                if self.play_lottery():
                    self.money_earned += 40000000
        else:
            check = False
            while check == False:
                self.weeks_to_simulate += 1
                if self.play_lottery():
                    self.money_earned += 40000000
                    check = True
                
        self.money_spent = self.weeks_to_simulate * 2
        
    def print_summary(self):
        print('Money spent:    ', self.money_spent)
        print('Money won:      ', self.money_earned)
        print('Weeks simulated:', self.weeks_to_simulate)

np.random.seed(1030) # ensure always the same results

sim = LotterySimulation(weeks_to_simulate=52000)
sim.run()
sim.print_summary()