class Result:
    
    all =[]
    
    def __init__(self, player, game, score = 0):
        self.player = player
        self.game = game
        self.set_score(score)
        Result.all.append(self)
    
    def get_score(self):
        return self._score
    
    def set_score(self, score):
        if (type(score) is int) and (1 <= score <= 5000):
            self._score = score
    
    score = property(get_score, set_score)