from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from Pieces import *


class Chess():

    def __init__(self):
        app = QApplication([])
        app.setStyle("fusion")
        view = MainWindow()
        view.resize(860, 860)
        #chess_pieces = piece_initialisation()
        view.show()
        app.exec_()

    def piece_initialisation():
        pieces_collection = []
        
        #White/Black Pawn Objects
        for x in range (len(8)):
            pieces_collection.append(Pawn([6,x], True))
            pieces_collection.append(Pawn([1,x], False))

        #Rook Objects
        pieces_collection.append(Rook([0,0],False))
        pieces_collection.append(Rook([0,7], False))
        pieces_collection.append(Rook([7,0],True))
        pieces_collection.append(Rook([7,7], True))
        
        #Knight Objects
        pieces_collection.append(Knight([0,1],False))
        pieces_collection.append(Knight([0,6], False))
        pieces_collection.append(Knight([7,1],True))
        pieces_collection.append(Knight([7,6], True))

        #Bishop Objects
        pieces_collection.append(Bishop([0,2],False))
        pieces_collection.append(Bishop([0,5], False))
        pieces_collection.append(Bishop([7,2],True))
        pieces_collection.append(Bishop([7,5], True))

        #Queen Objects
        pieces_collection.append(Queen([0,3], False))
        pieces_collection.append(Queen([7,4],True))  
        
        #Queen Objects
        pieces_collection.append(King([0,4], False))
        pieces_collection.append(King([7,3],True))
 

    
new_game = Chess()

