from management import clear_screen, Colors

class Board(object):
    '''Class holding board object'''
    _wildcard = '#'
   
    GAME_BOARD_MARK_X = 'X'
    GAME_BOARD_MARK_O = 'O'
    
    COLOR_X = Colors.OKGREEN
    COLOR_O = Colors.OKBLUE
    COLOR_END = Colors.ENDC
    COLOR_BORDER = Colors.MAGENTA
    
    WHITESPACE = ' '
    SYMBOL = '*'

    def __init__(self,*, stats = None):
        '''stats: provided by caller, holds players scores'''
        self._initial_board = [self._wildcard for x in range(0,10)]
        self._board = self._initial_board[:]
        self._stats= stats

    def put_mark(self, index, mark):
        '''Places X or O mark on the board'''
        if not type(index) is int:
            index = int(index)
        self._board[index] = mark
        self.display()

    def is_full(self):
        '''Checks wheter all fields are filled by Xs or Os'''
        return len(list(filter(lambda x: x == self._wildcard, self._board))) == 1

    def reset(self):
        '''Clears game board'''
        print(self._board)
        self._board = self._initial_board[:]
        print(self._board)
        self.display()

    def get_free_fields(self):
        '''Returns array of available fields'''
        return [ix for ix, val  in enumerate(self._board) if ix > 0 and val == self._wildcard]

    def _get_winner(self):
        ''' Internal get winer function, 
            checks if exists wining combinations
        '''
        b = self._board
        win_x = self.GAME_BOARD_MARK_X * 3
        win_o = self.GAME_BOARD_MARK_O * 3
        
        # this matrix design with winning indexes, 
        # those suppose to make winning combination to blink (not implemented)
        winning_matrix = [
            [f'{b[1]}{b[2]}{b[3]}', [1,2,3]], # bottom row
            [f'{b[4]}{b[5]}{b[6]}', [4,5,6]], # middle row
            [f'{b[7]}{b[8]}{b[9]}', [7,8,9]], # top row
            [f'{b[1]}{b[4]}{b[7]}', [1,4,7]], # left column
            [f'{b[2]}{b[5]}{b[8]}', [2,5,8]], # middle column
            [f'{b[3]}{b[6]}{b[9]}', [3,6,9]], # right column
            [f'{b[1]}{b[5]}{b[9]}', [1,5,9]], # diagonal 1-5-9
            [f'{b[3]}{b[5]}{b[7]}', [3,5,7]], # diagonal 3-5-7
        ]

        winner_x = list(filter(lambda x: x[0] == win_x, winning_matrix))
        winner_y = list(filter(lambda x: x[0] == win_o, winning_matrix ))
        if  len(winner_x) > 0:
            return [self.GAME_BOARD_MARK_X, winner_x[0][1]]
        elif len(winner_y) > 0:
            return [self.GAME_BOARD_MARK_O, winner_y[0][1]]
        else:
            return [None, None]    

    def get_winner(self):
        '''Public get winner function'''
        return self._get_winner()[0]

    def x_color_string(self, string):
        color = self.COLOR_X
        endcolor = self.COLOR_END
        return f'{color}{string}{endcolor}'
    
    def y_color_string(self, string):
        color = self.COLOR_O
        endcolor = self.COLOR_END
        return f'{color}{string}{endcolor}'

    def display(self):
        '''Displays game board in the console'''
        clear_screen()

        print(self._draw_stats())
        print(self._draw_r())
        print(self._draw_c() + self._draw(7,1) + self._draw_c() + self._draw(8,1) + self._draw_c() + self._draw(9,1) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,2) + self._draw_c() + self._draw(8,2) + self._draw_c() + self._draw(9,2) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,3) + self._draw_c() + self._draw(8,3) + self._draw_c() + self._draw(9,3) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,4) + self._draw_c() + self._draw(8,4) + self._draw_c() + self._draw(9,4) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,5) + self._draw_c() + self._draw(8,5) + self._draw_c() + self._draw(9,5) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,6) + self._draw_c() + self._draw(8,6) + self._draw_c() + self._draw(9,6) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,7) + self._draw_c() + self._draw(8,7) + self._draw_c() + self._draw(9,7) + self._draw_c()) 
        print(self._draw_c() + self._draw(7,8) + self._draw_c() + self._draw(8,8) + self._draw_c() + self._draw(9,8) + self._draw_c()) 
        print(self._draw_r())  
        print(self._draw_c() + self._draw(4,1) + self._draw_c() + self._draw(5,1) + self._draw_c() + self._draw(6,1) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,2) + self._draw_c() + self._draw(5,2) + self._draw_c() + self._draw(6,2) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,3) + self._draw_c() + self._draw(5,3) + self._draw_c() + self._draw(6,3) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,4) + self._draw_c() + self._draw(5,4) + self._draw_c() + self._draw(6,4) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,5) + self._draw_c() + self._draw(5,5) + self._draw_c() + self._draw(6,5) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,6) + self._draw_c() + self._draw(5,6) + self._draw_c() + self._draw(6,6) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,7) + self._draw_c() + self._draw(5,7) + self._draw_c() + self._draw(6,7) + self._draw_c()) 
        print(self._draw_c() + self._draw(4,8) + self._draw_c() + self._draw(5,8) + self._draw_c() + self._draw(6,8) + self._draw_c()) 
        print(self._draw_r())  
        print(self._draw_c() + self._draw(1,1) + self._draw_c() + self._draw(2,1) + self._draw_c() + self._draw(3,1) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,2) + self._draw_c() + self._draw(2,2) + self._draw_c() + self._draw(3,2) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,3) + self._draw_c() + self._draw(2,3) + self._draw_c() + self._draw(3,3) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,4) + self._draw_c() + self._draw(2,4) + self._draw_c() + self._draw(3,4) + self._draw_c())
        print(self._draw_c() + self._draw(1,5) + self._draw_c() + self._draw(2,5) + self._draw_c() + self._draw(3,5) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,6) + self._draw_c() + self._draw(2,6) + self._draw_c() + self._draw(3,6) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,7) + self._draw_c() + self._draw(2,7) + self._draw_c() + self._draw(3,7) + self._draw_c()) 
        print(self._draw_c() + self._draw(1,8) + self._draw_c() + self._draw(2,8) + self._draw_c() + self._draw(3,8) + self._draw_c())
        print(self._draw_r())

    def _draw(self, index, part):
        "Returns disired printable object"
        numbers = {
            1 : self._draw_one,
            2 : self._draw_two,
            3 : self._draw_three,
            4 : self._draw_four,
            5 : self._draw_five,
            6 : self._draw_six,
            7 : self._draw_seven,
            8 : self._draw_eight,
            9 : self._draw_nine,
        }

        if self._board[index] == self.GAME_BOARD_MARK_X:
            func = self._draw_x
        elif  self._board[index] == self.GAME_BOARD_MARK_O:
            func = self._draw_o
        else:
            func = numbers.get(index)

        return func(part)

    def _draw_stats(self):
        '''Prints players scores'''
        pass      
        if self._stats:
            p1_name = self._stats['player1']['name']
            p1_won = self._stats['player1']['won']
            p2_name = self._stats['player2']['name']
            p2_won = self._stats['player2']['won']
            draw_name = 'Draw'
            draw = self._stats['draw']
            width = max(len(p1_name),len(p2_name), len(draw_name))
            color_p1 = self.COLOR_X
            color_p2 = self.COLOR_O
            endcolor = self.COLOR_END
            return  f'{color_p1}{p1_name: <{width}}: {p1_won}{endcolor}\n' + \
                    f'{color_p2}{p2_name: <{width}}: {p2_won}{endcolor}\n' + \
                    f'{draw_name: <{width}}: {draw}\n'
        return ''

    def _draw_x(self, part):
        "Returns X mark on the board"

        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_X
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{symbol*5}{space*14}{symbol*5}{endcolor}',
            2: f'{color}{space*3}{symbol*6}{space*5}{symbol*6}{space*4}{endcolor}',
            3: f'{color}{space*7}{symbol*4}{space*2}{symbol*4}{space*7}{endcolor}',
            4: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
            5: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
            6: f'{color}{space*7}{symbol*4}{space*2}{symbol*4}{space*7}{endcolor}',
            7: f'{color}{space*3}{symbol*6}{space*5}{symbol*6}{space*4}{endcolor}',
            8: f'{color}{symbol*5}{space*14}{symbol*5}{endcolor}',
        }

        return parts.get(part) 
    def _draw_o(self, part):
        "Returns O mark on the board"
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_O
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*5}{symbol*14}{space*5}{endcolor}',
            2: f'{color}{space*3}{symbol*18}{space*3}{endcolor}',
            3: f'{color}{space}{symbol*4}{space*14}{symbol*4}{space}{endcolor}',
            4: f'{color}{symbol*4}{space*16}{symbol*4}{endcolor}',
            5: f'{color}{symbol*4}{space*16}{symbol*4}{endcolor}',
            6: f'{color}{space}{symbol*4}{space*14}{symbol*4}{space}{endcolor}',
            7: f'{color}{space*3}{symbol*18}{space*3}{endcolor}',
            8: f'{color}{space*5}{symbol*14}{space*5}{endcolor}',
        }
        
        return parts.get(part) 
    def _draw_r(self):
        '''Returns horozontal lines'''
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        symbol = '|'
        return f'{color}{symbol*80}{endcolor}'
    def _draw_c(self):
        '''Returns vertical lines'''
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        symbol = '||'
        return f'{color}{symbol}{endcolor}'
    def _draw_one(self, part):
        '''Returns 2 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*12}{symbol*3}{space*9}{endcolor}',
            2: f'{color}{space*11}{symbol*4}{space*9}{endcolor}',
            3: f'{color}{space*10}{symbol*5}{space*9}{endcolor}',
            4: f'{color}{space*9}{symbol*3}{space}{symbol*2}{space*9}{endcolor}',
            5: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            6: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            8: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
        }
        return parts.get(part) 
    def _draw_two(self, part):
        '''Returns 2 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*9}{symbol*2}{space*13}{endcolor}',
            7: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            8: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
        }
        return parts.get(part) 
    def _draw_three(self, part):
        '''Returns 3 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            8: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
        }
        return parts.get(part)
    def _draw_four(self, part):
        '''Returns 4 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            3: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            8: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
        }
        return parts.get(part)  
    def _draw_five(self, part):
        '''Returns 5 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*9}{symbol*2}{space*13}{endcolor}',
            4: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            8: f'{color}{space*9}{symbol*6}{space*9}{endcolor}'
        }
        return parts.get(part)  
    def _draw_six(self, part):
        '''Returns 6 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*9}{symbol*2}{space*13}{endcolor}',
            4: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            8: f'{color}{space*9}{symbol*6}{space*9}{endcolor}'
        }
        return parts.get(part)  
    def _draw_seven(self, part):
        '''Returns 7 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            5: f'{color}{space*11}{symbol*4}{space*9}{endcolor}',
            6: f'{color}{space*11}{symbol*3}{space*10}{endcolor}',
            7: f'{color}{space*11}{symbol*2}{space*11}{endcolor}',
            8: f'{color}{space*11}{symbol*2}{space*11}{endcolor}'
        }
        return parts.get(part)  
    def _draw_eight(self, part):
        '''Returns 8 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
            2: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            3: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
            5: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
            6: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            8: f'{color}{space*10}{symbol*4}{space*10}{endcolor}',
        }
        return parts.get(part)     
    def _draw_nine(self, part):
        '''Returns 9 placeholder'''
        symbol = self.SYMBOL
        space = self.WHITESPACE
        color = self.COLOR_BORDER
        endcolor = self.COLOR_END
        parts = {
            1: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            2: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            3: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            4: f'{color}{space*9}{symbol*2}{space*2}{symbol*2}{space*9}{endcolor}',
            5: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            6: f'{color}{space*13}{symbol*2}{space*9}{endcolor}',
            7: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
            8: f'{color}{space*9}{symbol*6}{space*9}{endcolor}',
        }
        return parts.get(part)     
