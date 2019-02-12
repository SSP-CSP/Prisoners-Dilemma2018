import inspect
import prisoners_dilemma
import os
print('---',os.path.dirname(os.path.abspath(__file__)) )
team_name = 'w' 
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    global bs
    if len(my_history) == 0:
        player1Id = ((inspect.getargvalues(inspect.currentframe().f_back))[3])['player1']
        player2Id = ((inspect.getargvalues(inspect.currentframe().f_back))[3])['player2']       
        myId =inspect.getfile(inspect.currentframe()) 
        if str(myId) in str(player1Id):
            myId = player1Id  
            oppId = player2Id       
        elif str(myId) in str(player2Id):
            myId = player2Id
            oppId = player1Id     
        bs = (runSim(oppId,myId))   
    move = bs.move(my_history, their_history, my_score, their_score)  
    return move
def runSim(o,me):   
    modSs = []
    mods = prisoners_dilemma.modules  
    for i in range(0,(len( mods)-1)):
        if me ==  mods[i]:
            del  mods[i]
    for i in range(0,(len( mods)-1)):
        modSs.append([pG(( mods[i]),o),(( mods[i]).team_name),(o.team_name),( mods[i])])
    modSs.sort(key = lambda x: x[0])
    modSs = modSs[::-1]
    return((modSs[0])[-1])
def pG(m,o):
    mS = 0
    oS = 0
    mH = []
    oH = []
    for round in range(200):
        mS, oS, mH, oH = pR(m, o, mS, oS, mH, oH) 
    return mS
def pR(m,o,mS,oS,mH,oH):
    R = 0 
    T = 100 
    SP = -500 
    P = -250 
    E = -250
    a1 = m.move(mH,oH,mS,oS)
    a2 = o.move(oH,mH,oS,mS) 
    if (type(a1) != str) or (len(a1) != 1):
        a1=' '   
    if (type(a2) != str) or (len(a2) != 1):
        a2=' '
    a3 = a1 + a2   
    if a3 == 'cc':
        mS += R
        oS += R    
    elif a3 == 'cb':
        mS += SP
        oS += T   
    elif a3 == 'bc':
        mS += T
        oS += SP     
    elif a3 == 'bb':   
        mS += P
        oS += P      
    else:
        mS += E
        oS += E  
    if a1 in 'bc':
        mH += a1   
    else:
        mH += ' '
    if a2 in 'bc': 
        oH += a2
    else: 
        oH += ' '   
    return (mS,oS,mH,oH)  
         