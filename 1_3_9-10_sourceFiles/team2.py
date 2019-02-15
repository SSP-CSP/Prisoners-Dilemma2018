####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = "Jeff"
strategy_name = "Pessimistic Backstabber"
strategy_description = "Collude until betrayed. Then always betray. Betray on 100."

def move(my_history, their_history, my_score, their_score):#defines the variables used
    if len(my_history) == 100: #if my history is equal to 100
        return 'b' # then betray
    elif 'b' in their_history: #else if a b is in their history then betray
        return 'b'
    else:
        return 'c' #if they didn't betray ever or it isn't the final round then collude.          
