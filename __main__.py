from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from Pieces import *


class Chess():

    def __init__(self):
        app = QApplication([])
        app.setStyle("fusion")
        view = MainWindow()
        view.resize(860, 860)
        self.chess_pieces = self.piece_initialisation()
        
        view.initialise_board(self.chess_pieces)
        view.show()
        app.exec_()



    def piece_initialisation(self):
        pieces_collection = []

        #White/Black Pawn Objects
        for x in range ((8)):
            pieces_collection.append(Pawn([x,6], True,QPixmap("Pieces/blackpawn.png")))
            pieces_collection.append(Pawn([x,1], False,QPixmap("Pieces/whitepawn.png")))

        #Rook Objects
        pieces_collection.append(Rook([0,0],False,QPixmap("Pieces/whiterook.png")))
        pieces_collection.append(Rook([7,0], False,QPixmap("Pieces/whiterook.png")))
        pieces_collection.append(Rook([0,7],True,QPixmap("Pieces/blackrook.png")))
        pieces_collection.append(Rook([7,7], True,QPixmap("Pieces/blackrook.png")))
        
        #Knight Objects
        pieces_collection.append(Knight([1,0],False,QPixmap("Pieces/whiteknightl.png")))
        pieces_collection.append(Knight([6,0], False,QPixmap("Pieces/whiteknightr.png")))
        pieces_collection.append(Knight([1,7],True,QPixmap("Pieces/blackknightl.png")))
        pieces_collection.append(Knight([6,7], True,QPixmap("Pieces/blackknightr.png")))

        #Bishop Objects
        pieces_collection.append(Bishop([2,0],False,QPixmap("Pieces/whitebishopl.png")))
        pieces_collection.append(Bishop([5,0], False,QPixmap("Pieces/whitebishopr.png")))
        pieces_collection.append(Bishop([2,7],True,QPixmap("Pieces/blackbishopl.png")))
        pieces_collection.append(Bishop([5,7], True,QPixmap("Pieces/blackbishopr.png")))

        #Queen Objects
        pieces_collection.append(Queen([3,0], False,QPixmap("Pieces/whitequeen.png")))
        pieces_collection.append(Queen([4,7],True,QPixmap("Pieces/blackqueen.png"))) 
        
        #Queen Objects
        pieces_collection.append(King([4,0], False, QPixmap("Pieces/whiteking.png")))
        pieces_collection.append(King([3,7],True, QPixmap("Pieces/blackking.png")))
        
        return pieces_collection

    def get_chess_objects(self):
        return self.chess_pieces
    
new_game = Chess()

