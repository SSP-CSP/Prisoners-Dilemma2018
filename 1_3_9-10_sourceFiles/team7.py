'''
PLTW Computer Science Principles
1.3.10 Prisoner's Dilemma Algorithm

Created by Tyler Gruhlke
Febuary 2019
'''

team_name = "Zuko Kaizo"
strategy_name = "Diplomat"
strategy_description = "Collude. If betrayed, betray until two consecutive colludes. Betry at end."


def move(my_history, their_history, my_score, their_score):
    if len(my_history) > 98:
        return 'b'
    else:
        try:
            if 'b' in their_history:
                if their_history[-1] == their_history[-2] == 'c':
                    return 'c'
                else:
                    return 'b'
            else:
                return 'c'
        except IndexError:
            return 'c'