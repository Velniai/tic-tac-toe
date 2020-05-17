from board import Board

class Manager(object):
    '''Class managing players interactions with a board'''
    b_x =  'X'
    b_y =  'O'

    player1_name = 'Player 1'
    player2_name = 'Player 2'
    player1_mark = b_x
    player2_mark = b_y  
    
    current_mark = b_x

    def start(self):
        '''Begins a game'''
        player_choise = input(f"Player 1 name (default '{self.player1_name}'): ")
        if len(player_choise.strip())  > 0:
            self.player1_name = player_choise.strip()

        player_choise = input(f"Player 2 name (default '{self.player2_name}'): ")
        if len(player_choise.strip())  > 0:
            self.player2_name = player_choise.strip()

        self._init_stats()
        self.game_board = Board(stats=self.stats)  
        self.game_board.display()
        self.make_turns()

    def make_turns(self):
        '''Asks and places player moves'''
        turn = input(self.get_current_player_turn_text())
        available_fields = self.game_board.get_free_fields()
        try:
            turn = int(turn)
            if not turn in available_fields:
                raise ValueError
        except ValueError:
            print(f'Invalid value {turn}. Available options: {", ".join(map(lambda x: str(x) ,available_fields))}')
            self.make_turns()
            return
   
        self.game_board.put_mark(turn, self.current_mark)
        self.switch_turn()
        if not self.is_game_over():     
            self.make_turns()
        else: 
            retry = input('Retry? [y]es/[n]o : ')
            if retry.lower() == 'y':
                self.game_board.reset()
                self.make_turns()

    def get_current_player_turn_text(self):
        '''Returns prompt text for required player'''
        if self.current_mark == self.player1_mark:
            return self.game_board.x_color_string(f"{self.player1_name} ({self.player1_mark}) turn: ")
        else:
            return self.game_board.y_color_string(f"{self.player2_name} ({self.player2_mark}) turn: ")

    def switch_turn(self):
        '''Switchs turn to next player'''
        if self.current_mark == self.player1_mark:
            self.current_mark = self.player2_mark
        else:            
            self.current_mark = self.player1_mark
    
    def is_game_over(self):
        '''Checks if game is over'''
        is_full = self.game_board.is_full()
        winner =  self.game_board.get_winner()
        if winner:
            if winner == self.player1_mark:
                self.stats['player1']['won'] += 1
                print(self.game_board.x_color_string(f'{self.player1_name} WON'))
            else:
                self.stats['player2']['won'] += 1
                print(self.game_board.y_color_string(f'{self.player2_name} WON'))
            
            return True
        
        if is_full:
            print('DRAW')
            self.stats['draw'] += 1
            return True
        
        return False
    
    def _init_stats(self):
        '''Initializes players stat dictionary'''
        self.stats = {
        'player1' : {
            'name': self.player1_name,
            'won' : 0
        },
        'player2' : {
            'name': self.player2_name,
            'won' : 0
        },
        'draw': 0
    }