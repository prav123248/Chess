from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QWidget,
)
import Pieces


class CentralWidget(QWidget):
    def __init__(self, widget):
        super().__init__()
        self._widget = widget
        self.widget.setParent(self)

    @property
    def widget(self):
        return self._widget

    def resizeEvent(self, event):
        super().resizeEvent(event)
        size = min(self.width(), self.height())
        r = QStyle.alignedRect(
            Qt.LeftToRight, Qt.AlignCenter, QSize(size, size), self.rect()
        )
        self.widget.setGeometry(r)


class chess_label(QLabel):
    
    chess_grid = None
    top_colour = False   #Default top of the board is white (so false) but included this for help in possible future colour switch addition
    moving_piece = None
    selected_label = None
    valid_moves = []

    def __init__(self, colour, position):
        super().__init__()
        self.piece = None
        self.position = position
        self.colour = colour
        self.setAlignment(Qt.AlignCenter)
        
        self.reset_colour()

    def set_piece(self,piece_object):
        self.setPixmap(piece_object.getImage())
        self.piece = piece_object

    def reset_colour(self):

        if self.colour:
            self.setStyleSheet("border: 0.1em solid black; background: #481f1b;")
        else:
            self.setStyleSheet("border: 0.1em solid black; background: #cfac86;")
        
    def mousePressEvent(self, event):
        if self.piece and chess_label.moving_piece == None:
            chess_label.moving_piece = self.piece
            chess_label.selected_label = self
            chess_label.valid_moves = (self.piece).move(chess_label.chess_grid, chess_label.top_colour)
            for move in chess_label.valid_moves:

                #Only valid moves returned so piece must be opponent piece, impossible for same team
                if chess_label.chess_grid[move[0]][move[1]].piece:
                    chess_label.chess_grid[move[0]][move[1]].colour_request("red")
                else:
                    chess_label.chess_grid[move[0]][move[1]].colour_request("green")
            
        elif self.position in chess_label.valid_moves:
            self.travel_here(chess_label.moving_piece)
            for move in chess_label.valid_moves:
                chess_label.chess_grid[move[0]][move[1]].reset_colour()
            chess_label.valid_moves = []

        elif self.position not in chess_label.valid_moves:
            chess_label.moving_piece = None
            for move in chess_label.valid_moves:
                chess_label.chess_grid[move[0]][move[1]].reset_colour()
            chess_label.valid_moves = []

    def colour_request(self, colour):
        if colour == "green":
            self.setStyleSheet("border: 0.1em solid black; background: green;")
        elif colour == "red":
            self.setStyleSheet("border: 0.1em solid black; background: red;")

    def travel_here(self, piece):
        (chess_label.selected_label).removePiece()
        chess_label.selected_label = None
        self.set_piece(piece)
        piece.move_update(self.position)
        chess_label.moving_piece = None
        return

    def removePiece(self):
        self.piece = None
        self.clear()



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        container = QWidget()
        central_widget = CentralWidget(container)
        self.setCentralWidget(central_widget)
        self.setMinimumSize(800,800)
        lay = QGridLayout(container)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        colour = False
        self.chess_grid = []


        for y in range(8):
            row = []

            for x in range(8):
                place = chess_label(colour, [y,x])
                colour = not colour
                row.append(place)
                lay.addWidget(place,x,y)

            self.chess_grid.append(row)
            colour = not colour
            chess_label.chess_grid = self.chess_grid
    def initialise_board(self, pieces):

        for item in pieces:
            self.chess_grid[item.getX()][item.getY()].set_piece(item)



    def set_chess_grid(self, chess_grid):
        self.chess_grid = chess_grid

    def get_chess_grid(self):
        return self.chess_grid
