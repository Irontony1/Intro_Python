class TicTacToeBoard():

    def __init__(self):
        self.field = [["-","-","-"],
                      ["-","-","-"],
                      ["-","-","-"]]
        self.player = True
    
    def new_game(self):
        self.field = [["-","-","-"],
                      ["-","-","-"],
                      ["-","-","-"]]
        self.player = True
    
    def get_field(self):
        return self.field 
    
    def check_field(self):
        if ((self.field[0][0] == 'X' and self.field[0][1] == 'X' and self.field[0][2] == 'X') or 
            (self.field[1][0] == 'X' and self.field[1][1] == 'X' and self.field[1][2] == 'X') or 
            (self.field[2][0] == 'X' and self.field[2][1] == 'X' and self.field[2][2] == 'X') or 
            (self.field[0][0] == 'X' and self.field[1][1] == 'X' and self.field[2][2] == 'X') or 
            (self.field[0][2] == 'X' and self.field[1][1] == 'X' and self.field[2][0] == 'X') or 
            (self.field[0][0] == 'X' and self.field[1][0] == 'X' and self.field[2][0] == 'X') or 
            (self.field[0][1] == 'X' and self.field[1][1] == 'X' and self.field[2][1] == 'X') or  
            (self.field[0][2] == 'X' and self.field[1][2] == 'X' and self.field[2][2] == 'X')):
            return 'X'

        elif ((self.field[0][0] == '0' and self.field[0][1] == '0' and self.field[0][2] == '0') or
            (self.field[1][0] == '0' and self.field[1][1] == '0' and self.field[1][2] == '0') or
            (self.field[2][0] == '0' and self.field[2][1] == '0' and self.field[2][2] == '0') or
            (self.field[0][0] == '0' and self.field[1][1] == '0' and self.field[2][2] == '0') or
            (self.field[0][2] == '0' and self.field[1][1] == '0' and self.field[2][0] == '0') or
            (self.field[0][0] == '0' and self.field[1][0] == '0' and self.field[2][0] == '0') or
            (self.field[0][1] == '0' and self.field[1][1] == '0' and self.field[2][1] == '0') or
            (self.field[0][2] == '0' and self.field[1][2] == '0' and self.field[2][2] == '0')):
            return '0'
        elif '-' not in self.field[0] and self.field[1] and self.field[2]: return 'D' 
        else: return None

    def make_move(self, row:int, column:int):
        if self.field[row-1][column-1] == '-':
            if self.player:
                self.field[row-1][column-1] = 'X'
                self.player = False
            else: 
                self.field[row-1][column-1] = '0'
                self.player = True
        else: 
            print(f'Клетка <{row}>, <{column}> уже занята')

        if TicTacToeBoard.check_field(self) == None:
            return 'Продолжаем играть'
        elif TicTacToeBoard.check_field(self) == 'X':
            return 'Победил игрок X!'
        elif TicTacToeBoard.check_field(self) == '0':
            return 'Победил игрок 0'
        elif TicTacToeBoard.check_field(self) == 'D':
            return 'Ничья!'


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1,1))
print(*board.get_field(), sep='\n')
print(board.make_move(1,1))
print(board.make_move(1,2))
print(*board.get_field(), sep='\n')
print(board.make_move(2,1))
print(board.make_move(2,2))
print(board.make_move(3,1))
print(board.make_move(2,2))
print(*board.get_field(), sep='\n')