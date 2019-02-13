####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'I have headache' # Only 10 chars displayed.
strategy_name = 'Titfortat'
strategy_description = '''\copying the last round of my opponenet Start by colluding, betray on last round.'''

    import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history of this player.
    
    Returns 'c' or 'b' for collude or betray.
    '''

    try: 
        return their_history[-1]#return the last decission that my opponent made, Tit for Tat.
    except IndexError: # else return collude aka on the first round.
        return 'c'
    if len(my_history) > 99:
        return 'b'
