class BaseballPlayer:

    def __init__(self, name, jersey_number, handed):
        self.name = name
        self.jersey_number = jersey_number
        self.handed = handed
        self.total_hits = 0
        self.total_runs = 0
        self.total_rbis = 0
        self.total_games = 0

    def complete_a_game(self, hits, rbis, runs):
        self.total_hits += hits
        self.total_rbis += rbis
        self.total_runs += runs
        self.total_games += 1
        
    def __str__(self):
        return 'rbis: ' + str(self.total_rbis) + ' hits: ' + str(self.total_hits) + ' runs: ' + str(self.total_runs) + ' games: ' + str(self.total_games)

albert = BaseballPlayer('Albert', 5, 'right')
print(albert)
albert.complete_a_game(3, 2, 1)
print(albert)
albert.complete_a_game(1, 3, 1)
print(albert)

      