import numpy as np
import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'AI'
strategy_name = 'Guess'
strategy_description = 'Random for first few rounds, then move is guessed'
    
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    X = np.array([])
    y = np.array([]).T
    
    #convert their_history and my_history into numpy arrays
    for i in range(len(their_history)):
        if 'c' == their_history[i]:
            y = np.concatenate((y, [0]))
        else:
            y = np.concatenate([y, [1]])

    y = y[:,np.newaxis]
            
    for i in range(len(my_history)):
        if 'c' == my_history[i]:
            X = np.concatenate((X, [0]))
        else:
            X = np.concatenate((X, [1]))
    X = X[:,np.newaxis]
        
    if (len(my_history) > 0):

        # seed random numbers to make calculation
        # deterministic (just a good practice)
        np.random.seed(1)

        # initialize weights randomly with mean 0
        syn0 = 2*np.random.random((len(my_history),1)) - 1

        for iter in xrange(10000):

            # forward propagation
            l0 = X
            l1 = nonlin(np.dot(l0.T,syn0))
            # how much did we miss?
            l1_error = y - l1.T

            # multiply how much we missed by the 
            # slope of the sigmoid at the values in l1
            l1_delta = l1_error * nonlin(l1,True)

            # update weights
            syn0 += np.dot(np.squeeze(np.asarray(l0.T)), np.squeeze(np.asarray(l1_delta)))
            
        
        #thinks we should betray
        if (l1 > 0.5):
            return 'b'
            
        #thinks we should collude
        if (l1 < 0.5):
            return 'c'
            
        #can't be guessed
        if (l1 == 0.5):
            list = ['c','b']
            return random.choice(list)
    else:
        list = ['c','b']
        return random.choice(list)