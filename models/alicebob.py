from src.soup import BehaviorSoup

# TODO : adpater ce code pour alice et bob

class ABConfig(list):
    def __init__(self):
        list.__init__(self, [-1, -1])

    def __hash__(self):
        return self[0] + 10*self[1]
    
    def __str__(self):
        am, aj, bm, bj = '    ', '    ','    ', '    '
        if self[0] == -1:
            am = 'A   '
        elif self[0] == 0 :
            aj = 'Alic'
        else :
            am = 'A ok'
        if self[1] == -1:
            bm = 'B   '
        elif self[1] == 0 :
            bj = 'Bob '
        else :
            bm = 'B ok' 
        res = f"""
Maison Alice {am}                   -- Maison
Maison           -- jardin {aj}{bj} -- Maison Bob {bm}
Maison                                 Maison"""


        res= f"""
    ) )        /\                                                 ) )        /\\
   =====      /  \                                               =====      /  \\
  _|___|_____/ __ \____________                                 _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|                               |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|                               |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|                               |::::::::/__________\:::::::::|
 |_________|  ____  |__________|                               |_________|  ____  |__________|
  | ______ | / || \ | _______ |                                 | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||                                 ||  |   || ====== ||   |   ||
  ||--+---|| |{am}| ||---+---||         {aj}{bj}                ||--+---|| |{bm}| ||---+---||
  ||__|___|| |   o| ||___|___||                                 ||__|___|| |   o| ||___|___||
  |========| |____| |=========| -^^-^^^^^-^^-^^^^-^^-^^^--^^^-- |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)  ,, , ,, ,,   ,,, , ,,,, ,, ,  (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)  ,, , ,, , ,, ,, ,, ,,,, ,, ,  (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;  ,, , ,, , ,, ,, ,, ,,,, ,, , ','',,,,' /__________\,,,',',;;
        
"""
        return res
    
    def __repr__(self):
        res = self.__str__()
        return '\n'+res+'\n'


def alice_guard_def(b):
    def guard(c):
        if b == 1 and c[0] == 0:
            return False
        elif b == 0 and c[1] == 0:
            return False
        return True
    return guard
    

def alice_action_def(b):
    def action(c):
        if c[b] == 1:
            c[b] -=1
        else:
            c[b] += 1
    return action


def alice_soup():
    i_conf = ABConfig()
    soup = BehaviorSoup(i_conf)
    for i in range(2):
        for j in range(3):
            soup.add(f'{i}-{j}', alice_guard_def(i), alice_action_def(i))
    return soup


def alice_is_accepted(c):
    return c[0] == 1 and c[1] == 1