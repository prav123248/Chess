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

    def set_piece(self,piece_object):

        image = ((piece_object).getImage()).scaledToHeight(self.height()/5.5, Qt.SmoothTransformation)
        self.setPixmap(image)
        self.piece = image

    def mousePressEvent(self, event):
        
        if self.piece:
            (self.piece).move()
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
        self.chess_grid = []


        for y in range(8):
            row = []

            for x in range(8):
                place = chess_label(colour, [y,x])
                colour = not colour
                row.append(place)
                lay.addWidget(place,y,x)

            self.chess_grid.append(row)
            colour = not colour

    def initialise_board(self, pieces):

        for item in pieces:
            self.chess_grid[item.getX()][item.getY()].set_piece(item)

    def set_chess_grid(self, chess_grid):
        self.chess_grid = chess_grid

    def get_chess_grid(self):
        return self.chess_grid
