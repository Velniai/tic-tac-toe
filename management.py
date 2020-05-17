from os import system, name 
def clear_screen():
    '''Clears terminal''' 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

class Colors:
    '''Class holding available colors'''
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    MAGENTA = '\033[35m'

    #EndColor
    ENDC = '\033[0m'
