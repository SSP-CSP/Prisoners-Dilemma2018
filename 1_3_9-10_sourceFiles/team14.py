####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Davis'
strategy_name = 'SSP Davis'
strategy_description = 'Betray first round, Collude 40% of the time. betray if severe penalty.'
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; betry.
        return 'b'
    else:
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' # Betray if they were severely punished last time, 
            
        elif random.random()<0.6: # 60% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 40% of the time collude.
  
