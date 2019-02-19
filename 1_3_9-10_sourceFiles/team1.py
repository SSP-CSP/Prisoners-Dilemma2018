####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Keng' # Only 10 chars displayed.
strategy_name = 'Point_based'
strategy_description = 'This strat decides based off of the amount of points you and your opponent has'

def move(my_history,my_score, their_score):
    my_score=0
    their_score=0
    
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_score < 0 and their_score > 0: 
        return 'b'
    else:
        return 'c'