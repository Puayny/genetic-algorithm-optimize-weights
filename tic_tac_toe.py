class TicTacToe:
    status_dict = {0: 'Ongoing', 1: 'X won', 2: 'O won', 3: 'Draw'}
    def __init__(self, first_player):
        import numpy as np
        first_player = str.upper(first_player)
        self.board_state = [[' ' for i in range(3)] for j in range(3)]
        self.curr_player = first_player
        self.game_status = 0
    
    def __repr__(self):
        return self.board_state
    
    def __str__(self):
        str_format = ''
        for row_num, row in enumerate(self.board_state):
            for cell_num, cell in enumerate(row):
                str_format += ' {} '.format(cell)
                if cell_num!=2:
                    str_format += '|'
            str_format += '\n'
            if row_num!=2:
                str_format+='-----------\n'
        if self.game_status == 0:
            str_format += '\nPlayer {}\'s turn'.format(self.curr_player)
        else:
            str_format += '\n{}'.format(TicTacToe.status_dict[self.game_status])
        
        return str_format
                
    
    def is_valid_move(self, row, col):
        if row<0 or row>2 or col<0 or col>2:
            print('Index out of tic-tac-toe bounds')
            return False
        elif self.board_state[row][col] == ' ':
            return True
        else:
            return False
        
    def switch_player(self):
        self.curr_player = 'O' if self.curr_player == 'X' else 'X' 
    
    def update_game_status(self):
        curr_diag_left = ''
        curr_diag_right = ''
        
        for i in range(3):
            curr_row = ''
            curr_col = ''
            for j in range(3):
                curr_row += self.board_state[i][j]
                curr_col += self.board_state[j][i]
            if curr_row=='XXX' or curr_col=='XXX':
                self.game_status = 1
                return
            elif curr_row=='OOO' or curr_col=='OOO':
                self.game_status = 2
                return
            
            curr_diag_right += self.board_state[i][i]
            curr_diag_left += self.board_state[i][2-i]
            
        if curr_diag_right=='XXX' or curr_diag_left=='XXX':
            self.game_status = 1
            return
        elif curr_diag_right=='OOO' or curr_diag_left=='OOO':
            self.game_status = 2
            return
        
        for i in range(3):
            for j in range(3):
                if self.board_state[i][j]==' ':
                    return
        self.game_status = 3
        
    def get_game_status(self):
        return self.game_status
    
    #Each game board is represented by an 18 by 1 vector. Each game cell occupies 2 cells on this vector.
    #If the game cell is empty, both vector cells are 0. If the game cell is occupied by the players piece, 
    #the first cell on the vector is 1. If the game cell is occupied by the opponent's piece, the second cell on the vector is 1.
    def get_vector_repr(self):
        import numpy as np
        vector_repr = np.zeros(18).reshape(18,1)
        for row in range(3):
            for col in range(3):
                if self.board_state[row][col]==' ':
                    next
                elif self.board_state[row][col] == self.curr_player:
                    vector_repr_cell = row*6+col*2
                    vector_repr[vector_repr_cell] = 1
                else:
                    vector_repr_cell = row*6+col*2+1
                    vector_repr[vector_repr_cell] = 1
        return vector_repr
    
    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            print('Invalid move')
        elif self.game_status!=0:
            print('Game already over')
        else:
            self.board_state[row][col] = self.curr_player
            #check game end here
            self.update_game_status()
            
        self.switch_player()