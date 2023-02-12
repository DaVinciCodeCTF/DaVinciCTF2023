import numpy as np
#from stockfish import Stockfish
import matplotlib.pyplot as plt


#stockfish = Stockfish(path="stockfish_15_linux_x64/stockfish_15_linux_x64/stockfish_15_x64", depth=10, parameters={"Skill Level" : 5})
fen_dep = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
#stockfish.set_fen_position(fen_dep)


def CreaBoard():
    a = []

    for i in range(64):
        b = []
        for j in range (64):
            if (i//8)%2 == 0:
                if (j//8)%2 == 0 :
                    b.append(255)
                else :
                    b.append(0)
            else : 
                if (j//8)%2 == 0 :
                    b.append(0)
                else :
                    b.append(255)
        a.append(b)
    return np.array(a)

def IsolCase(board , x , y):
    a = []
    for i in range(8*x, 8*(x+1)):
        b = []
        for j in range(8*y, 8*(y+1)):
            b.append(board[i,j])
        a.append(b)
    return np.array(a)

def ModifBoard(board, x,y, case):
    
    for i in range(8*x, 8*(x+1)):
        for j in range(8*y, 8*(y+1)):
            if board[i,j] == 0:
                board[i,j] += 170*case[i - 8*x,j-8*y]
            else : 
                board[i,j] -= 170*case[i - 8*x, j - 8*y]
    return np.array(board)

def FenToBoard(board,fen):
    txtBoard = [[]]
    j = 0;
    

    for i in range(len(fen)):
        if fen[i] != "/":
            if fen[i] == "1":
                txtBoard[j].append(" ")
                i+=1
            elif fen[i] == "2":
                for k in range(2):
                    txtBoard[j].append(" ")
                    i+=1
            elif fen[i] == "3":
                for k in range(3):
                    txtBoard[j].append(" ")
                    i+=1

            elif fen[i] == "4":
                for k in range(4):
                    txtBoard[j].append(" ")
                    i+=1

            elif fen[i] == "5":
                for k in range(5):
                    txtBoard[j].append(" ")
                    i+=1

            elif fen[i] == "6":
                for k in range(6):
                    txtBoard[j].append(" ")
                    i+=1
            elif fen[i] == "7":
                for k in range(7):
                    txtBoard[j].append(" ")
                    i+=1
            elif fen[i] == "8":
                for k in range(8):
                    txtBoard[j].append(" ")
                    i+=1
            else:
                txtBoard[j].append(fen[i])
 
        else : 
            txtBoard.append([])
            j+=1
    
    for i in range(8):
        for j in range(8):
            if(txtBoard[i][j] != '1' and txtBoard[i][j] != ' '):
                board = ModifBoard(board, i , j, piece[txtBoard[i][j]])
    return np.array(board)

def saveBoard(board, posFen):
    board = FenToBoard(board, posFen)
    plt.imsave("result.png", board, cmap = 'Greys_r')

        

r = np.array([[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,1,0,1,1,0,0],
              [0,0,1,1,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]
              ])

n = np.array([[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,0,0,0,0,0,0]
              ])

b = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,0]
              ])

k = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,1,0,0,0],
              [0,0,1,1,0,0,0,0],
              [0,0,1,0,1,0,0,0],
              [0,0,1,0,1,0,0,0],
              [0,0,0,0,0,0,0,0]
              ])

q = np.array([[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,0,1,1,1,0,0],
              [0,0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0,0]
              ])

K= np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,1,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,1,0,0,0],
              [0,0,1,1,0,0,0,0],
              [0,0,1,0,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,0,1,0]
              ])

Q = np.array([[0,0,0,0,0,0,0,0],
              [0,0,0,1,1,1,0,0],
              [0,0,1,0,0,0,1,0],
              [0,0,1,0,0,0,1,0],
              [0,0,1,0,1,0,1,0],
              [0,0,1,0,0,1,0,0],
              [0,0,0,1,1,0,1,0],
              [0,0,0,0,0,0,0,0]
              ])

R = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,0,0,0,0,0,0]
              ])

N = np.array([[0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0],
              [0,1,1,0,0,0,1,0],
              [0,1,0,1,0,0,1,0],
              [0,1,0,0,1,0,1,0],
              [0,1,0,0,0,1,1,0],
              [0,1,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,0]
              ])

B = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,1,0,0,0]
              ])

P = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,1,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]
              ])
p = np.array([[0,0,0,0,0,0,0,0],
              [0,0,1,1,0,0,0,0],
              [0,1,0,0,1,0,0,0],
              [0,1,0,0,1,0,0,0],
              [0,1,1,1,0,0,0,0],
              [0,1,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]              
              ])

piece = {"r" : r, "n" : n, "b" : b, "k" : k, "q" : q,"p" : p, "R" : R, "N" : N, "B" : B, "K" : K, "Q" : Q, "P" : P}          




#board = CreaBoard()

#board = FenToBoard(board, fen_dep)
#plt.imshow(board, cmap = 'Greys_r')
#plt.show()

#saveBoard(board, fen_dep)
