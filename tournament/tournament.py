class Match(object):
    count = 0
    
    def __init__(self, player1, player2):
        self.players = (player1, player2)
        self.result = None
        self.metadata = {}
        Match.count += 1
        
    def set_meta(self, data):
        self.metadata.update(data)
        
    def get_meta(self, key=None):
        if key == None:
            return self.metadata
        else:
            return self.metadata[key]
            
    def get_players(self):
        return self.players
        
    def get_result(self):
        if result == None:
            raise ValueError("Match result has not yet been determined.")
        else:
            return self.result
            
    def __repr__(self):
        if result == None:
            return ("Uncompleted match #%d between '%s' and '%s'." %
                    (Match.count, self.player[0], self.player[1]))
        else:
            return ("Completed match #%d between '%s' and '%s'. Result: %s." %
                    (Match.count, self.player[0], self.player[1], self.result))

class Participant(object):
    def __init__(self, T, identifier):
        self.identifier = identifier
        self.tournament = T
        
        self.d = {}
        
    def initialize(self, order = None):
        '''Sets the score ot zero and the history to empty.'''
        self.score = 0
        self.history = []
        
    def get_score(self):
        '''Returns the score of the participant.'''
        return self.score
        
    def set_score(self, score):
        '''Sets the score of the participant.'''
        self.score = score
        
    def add_result(self, opponent, result):
        '''Adds the result to the player's history.'''
        self.history.append({'opponent': opponent, 'result': result})
        
    def get_history(self, opponent=None, result=None):
        '''Returns the participant's history. Can be filtered by either
           opponent or result.'''
           ofilter = lambda x: (opponent != self and opponent in x.get_players()) or opponent == None
           rfilter = lambda x: result == x.get_result() or result == None
           return ofilter(rfilter(self.history))
           
    def add_matchup(self, opponent=None, metadata={}):
        d = {'opponent': opponent}
        d.update(metadata)
        self.upcoming.append({'opponent': opponent, metadata))
        
    

class Tournament(object):
    def __init__(self):
        self.participants = set()

    def add_participant(self, participant):
        self.participants.add(participant)
        
    def get_rankings(self, participants):
        return sorted(self.participants, key = self.get_score)
        
    def initialize(self):
        """Initialize the tournament, setting the score for each participant to
           0 and assigning the participants a uniformly random permutation."""
           
    def score
