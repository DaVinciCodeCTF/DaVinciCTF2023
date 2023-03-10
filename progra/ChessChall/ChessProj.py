from stockfish import Stockfish
from datetime import datetime, timedelta
import BoardToImage as bti
import base64


stockfish = Stockfish(path="./stockfish_14_x64", depth=5, parameters={"Skill Level" : 2})

fen_dep = "rnbqkbnr/pppppppp/11111111/11111111/11111111/11111111/PPPPPPPP/RNBQKBNR w KQkq"


print("Hello :) \nLet's play some chess \nI want to find someone better than me. \nYou will have to beat me 3 times in a row. \nTo do this, look at the board and send your move like this : StartingSquareFinalSquare (e2e4 for example)\n")
win = 0
dt = datetime.now()


for i in range(3):

    stockfish.set_fen_position(fen_dep)
    info_color = 0
   
    while win == i:
        
        if(i%2 == 0): #ordi qui commence
            if info_color == 0:
                print("You play as black.")
                info_color = 1
     
            stockfish.make_moves_from_current_position([stockfish.get_best_move()])
            if (stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0) or stockfish.get_top_moves(3) == []:
                win -=1

            
            #print(stockfish.get_board_visual()) #affiche
            board = bti.CreaBoard()
            bti.saveBoard(board, stockfish.get_fen_position())
            with open("result.png", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read())
            print(f"\n{b64_string.decode('utf-8')}\n")



            if win == i:
                try : 
                    stockfish.make_moves_from_current_position([input("your move :")])
                except : 
                    win = 65
                    i = 24
                    print("This move isn't legal, you won't beat me by cheating ;)\n")
                if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
                    win +=1
                elif stockfish.get_top_moves(3) == []:
                    win-=1
                #print(stockfish.get_board_visual())
            

        else: #joueur qui commence
            if info_color == 0:
                print("You play as white.")
                info_color = 1


            #print(stockfish.get_board_visual())affiche
            board = bti.CreaBoard()
            bti.saveBoard(board, stockfish.get_fen_position())
            with open("result.png", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read())
            print(f"\n{b64_string.decode('utf-8')}\n")


            try : 
                stockfish.make_moves_from_current_position([input("your move :")])
            except : 
                win = 65
                i = 24
                print("This move isn't legal, you won't beat me by cheating ;)\n")

            if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
                win +=1
            elif stockfish.get_top_moves(3) == []:
                win -=1
            #print(stockfish.get_board_visual())
            
            if win == i:
                stockfish.make_moves_from_current_position([stockfish.get_best_move()])
                if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
                    win -=1
                elif stockfish.get_top_moves(3) == []:
                    win -=1



            
if win == 3 and (datetime.now()-dt) <= timedelta(minutes = 1) :
    print(f"you did it in {datetime.now()-dt} ! Congrats, here is your flag : ")
    print("dvCTF{Br4v0K4sP4r0V}")
else:
    print("Sorry, you took too much time my student.")
    exit()
