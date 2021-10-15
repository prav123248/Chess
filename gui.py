from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QSizePolicy,
    QStyle,
    QWidget,
)


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
    rub = pyqtSignal([])
    def __init__(self, colour, position):
        super().__init__()
        self.piece = None
        self.position = position


        if colour:
            self.setStyleSheet("border: 0.1em solid black; background: gray;")
        else:
            self.setStyleSheet("border: 0.1em solid black;")

    def setPixmap(self,image):
        super.setPixmap(image)
        self.piece = image

    def mousePressEvent(self, event):
        send_away = [self.position, self.piece]
        self.rub.emit(send_away)
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
        
        grid_places = []
        lay = QGridLayout(container)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        colour = False
        chess_grid = []


        for y in range(8):
            row = []

            for x in range(8):
                place = chess_label(colour, [y,x])
                place.rub.connect(lambda: self.hey(a))
                colour = not colour
                row.append(place)
                lay.addWidget(place,y,x)

            chess_grid.append(row)
            colour = not colour

    def hey(self, n):
        print("hey")
        print(n)



def main():
    app = QApplication([])
    app.setStyle("fusion")
    view = MainWindow()
    view.resize(860, 860)
    view.show()
    app.exec_()






if __name__ == "__main__":
    main()
