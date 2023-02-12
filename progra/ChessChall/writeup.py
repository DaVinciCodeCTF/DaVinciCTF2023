from pwn import *
import time
import base64
from PIL import Image
import numpy as np
from stockfish import Stockfish

def TransfoFen(fen):
    ret ="" 

    for i in range (fen.find(" ")):
        if(fen[i] != " "):
            if (fen[i] in piece.keys()) == False and fen[i] != "/" and fen[i] != "1":
                for j in range(int(fen[i])):
                    ret+="1"
            else:
                ret+= fen[i]
        
    return ret
        

def FenToBoard(fen):
    tab = []
    
    for i in range(8):
        tab.append([])
        for j in range (8):
            if(fen[8*i+j+i] != "/"):
                tab[i].append(fen[8*i+j+i])
    return tab

def Coup(fen1, fen2, c):
    alpha = "abcdefgh"
    tab =[]
    ret =""
    b1 = FenToBoard(fen1)
    b2 = FenToBoard(fen2)
    for i in range(8):
        for j in range(8):
            if b1[i][j] != b2[i][j]:
                tab.append([i,j])
    
    if len(tab) == 2:
        if c == 1:
            if b1[tab[0][0]][tab[0][1]].upper() == b2[tab[1][0]][tab[1][1]] and b1[tab[0][0]][tab[0][1]] != "1" :
                ret =f"{alpha[tab[0][1]]}{8-tab[0][0]}{alpha[tab[1][1]]}{8-tab[1][0]}"
            
            else : 
                ret =f"{alpha[tab[1][1]]}{8-tab[1][0]}{alpha[tab[0][1]]}{8-tab[0][0]}"
        elif c == 0:
            if b1[tab[0][0]][tab[0][1]].lower() == b2[tab[1][0]][tab[1][1]] and b1[tab[0][0]][tab[0][1]] != "1" :
                ret =f"{alpha[tab[0][1]]}{8-tab[0][0]}{alpha[tab[1][1]]}{8-tab[1][0]}"

            else : 
                ret =f"{alpha[tab[1][1]]}{8-tab[1][0]}{alpha[tab[0][1]]}{8-tab[0][0]}"
    else:
        if c == 1:
            if b2[7][5] == "R":
                ret = "e1g1"
            else:
                ret = "e1c1"
        elif c == 0:
            if b2[0][5] == "r":
                ret = "e8g8"
            else:
                ret = "e8c8"
 
    return ret
    

def main():
    color = 1 #color%2 == 0 pour blanc 
    stockfish = Stockfish(path="./stockfish_15_linux_x64/stockfish_15_linux_x64/stockfish_15_x64") #mettre le path de son propre stockfish
    r = remote('localhost',6464)
    
    stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    pastFen = TransfoFen(stockfish.get_fen_position())

    while True:
        try:
            data = r.recvuntil(b"move :")
        except :
            data = r.recv(timeout = 1000)
    
        print(data.decode('UTF-8'))
        try:
            board = b"iVBO"+data.split(b"iVBO")[1].split(b"\r\n")[0]
        except:
            print(data)
            r.interactive()
        #print(board)
    
        

        
        print(color)
        with open("board.png", "wb") as fh:
            fh.write(base64.decodebytes(board))


        im = Image.open("board.png")
        im = im.convert('RGB')
        size = im.size
    
        board=""
        verif = False
        for x in range(8):
            for y in range(8):
                c = np.zeros((8,8))
                for i in range(x*8,x*8+8):
                    for j in range(y*8,y*8+8):
                        pixel = im.getpixel((j,i))
                        if pixel==(104,104,104) or pixel==(198, 198, 198):
                            c[i%8][j%8]=1 # to reverse symmetry
                #print(x,y,"\n",c)
                verif = False
                for k,v in piece.items():
                
                    if (c==v).all():
                        #print(k)
                        board+=k
                        verif = True
                if verif == False:
                    board+="1"
            
            
                
            if(x!=7):
                board+="/"

                
        
        newFen = board
        #print(newFen)
        if(newFen == "rnbqkbnr/pppppppp/11111111/11111111/11111111/11111111/PPPPPPPP/RNBQKBNR"):
            stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            color+=1
            
        else:
            coup = Coup(pastFen, newFen,color%2)

            if stockfish.is_move_correct(coup):
                stockfish.make_moves_from_current_position([coup])
            else:
                #print("coucou")
                color+=1
                stockfish.set_fen_position(newFen+" b KQkq")
            
                


        
        #print(stockfish.get_board_visual())

        bcoup = stockfish.get_best_move()
        
        stockfish.make_moves_from_current_position([bcoup])
        
        pastFen = TransfoFen(stockfish.get_fen_position())
        #print(bcoup)

        #print(stockfish.get_board_visual())
        


        r.send(bytes(bcoup+"\n", 'UTF-8'))


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



if __name__ == "__main__":
    #print(FenToBoard("rnbqkbnr/pppppppp/11111111/11111111/11111111/11111N11/PPPPPPPP/RNBQKB1R"))
    #print(FenToBoard("rnbqkbnr/pppppppp/11111111/11111111/11111111/11111111/PPPPPPPP/RNBQKBNR"))

    main()