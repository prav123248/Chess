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
    
    def __init__(self, colour, position):
        super().__init__()
        self.piece = None
        self.position = position
        self.setAlignment(Qt.AlignCenter)

        if colour:
            self.setStyleSheet("border: 0.1em solid black; background: #481f1b;")
        else:
            self.setStyleSheet("border: 0.1em solid black; background: #cfac86;")

    def set_piece_pic(self,image):
        h = self.height()
        w = self.width()
        image = image.scaledToHeight(self.height()/5.5, Qt.SmoothTransformation)
        self.setPixmap(image)
        self.piece = image


    def mousePressEvent(self, event):
        send_away = [self.position, self.piece]
       
        if self.piece:
            
            self.setStyleSheet("border: 0.1em solid black; background: green;")
        else:
            
            self.setStyleSheet("border: 0.1em solid black; background: red;")


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
        chess_grid = []


        for y in range(8):
            row = []

            for x in range(8):
                place = chess_label(colour, [y,x])
                colour = not colour
                row.append(place)
                lay.addWidget(place,y,x)

            chess_grid.append(row)
            colour = not colour

        #Making the Pawns
        for x in range (len(chess_grid[0])):
                    
            chess_grid[1][x].set_piece_pic(QPixmap("Pieces/whitepawn.png"))
            chess_grid[6][x].set_piece_pic(QPixmap("Pieces/blackpawn.png"))
           
        chess_grid[0][0].set_piece_pic(QPixmap("Pieces/whiterook.png"))
        chess_grid[0][7].set_piece_pic(QPixmap("Pieces/whiterook.png"))

        chess_grid[7][0].set_piece_pic(QPixmap("Pieces/blackrook.png"))
        chess_grid[7][7].set_piece_pic(QPixmap("Pieces/blackrook.png"))

        chess_grid[0][1].set_piece_pic(QPixmap("Pieces/whiteknightl.png"))
        chess_grid[0][6].set_piece_pic(QPixmap("Pieces/whiteknightr.png"))
        chess_grid[7][1].set_piece_pic(QPixmap("Pieces/blackknightl.png"))
        chess_grid[7][6].set_piece_pic(QPixmap("Pieces/blackknightr.png"))
        
        chess_grid[0][2].set_piece_pic(QPixmap("Pieces/whitebishopl.png"))
        chess_grid[0][5].set_piece_pic(QPixmap("Pieces/whitebishopr.png"))
        chess_grid[7][2].set_piece_pic(QPixmap("Pieces/blackbishopl.png"))
        chess_grid[7][5].set_piece_pic(QPixmap("Pieces/blackbishopr.png"))
        
        chess_grid[0][3].set_piece_pic(QPixmap("Pieces/whitequeen.png"))
        chess_grid[7][4].set_piece_pic(QPixmap("Pieces/blackqueen.png"))

        chess_grid[0][4].set_piece_pic(QPixmap("Pieces/whiteking.png"))
        chess_grid[7][3].set_piece_pic(QPixmap("Pieces/blackking.png"))

