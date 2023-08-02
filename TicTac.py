t=['#','1','2','3','4','5','6','7','8','9']
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def displayboard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def p1input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        print('Player 1 is X')
        return ('X', 'O')
    else:
        print('Player 1 is O')
        return ('O', 'X')
    
def place_marker(board, marker, position):
    board[position] = marker

def wincheck(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))



def pos():
    pos=''
    while pos not in ['#','1','2','3','4','5','6','7','8','9']:
        
        pos=input("Enter position :")
        
    return pos

def gamest():
    print("Welcome to Tic-Tac-Toe")
    displayboard(t)
    p1,p2=p1input()
    w=''
    p=[]
    for i in range(1,10):
        
        if i%2==0:
            print('Player 2\'s turn')
            position=int(pos())
            
            marker=p2
            while position  in p:
                print('Position already occupied')
                position=int(pos())
            place_marker(board, marker, position)
            displayboard(board)
            p.append(position)
            if wincheck(board,marker)==True:
                w=2
                print('Player 2 wins')
                break
        else:
            print('Player 1\'s turn')
            position=int(pos())
            marker=p1
            while position  in p:
                print('Position already occupied')
                position=int(pos())
            place_marker(board, marker, position)
            displayboard(board)
            p.append(position)
            if wincheck(board,marker)==True:
                print('Player 1 wins')
                w=1
                break
        
    
    if w=='':
        print('Tie')
        

