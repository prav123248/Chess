from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        container = QWidget()
        central_widget = CentralWidget(container)
        self.setCentralWidget(central_widget)

        lay = QGridLayout(container)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        colour = False
        for i in range(8):
            for j in range(8):
                label = QLabel(f"Place {i} {j}", alignment=Qt.AlignCenter)
                label.setStyleSheet(
                    "border: 0.1em solid black;"
                    if colour
                    else "border: 0.1em solid black; background: gray;"
                )
                lay.addWidget(label, i, j)
                colour = not colour
            colour = not colour


def main():
    app = QApplication([])
    app.setStyle("fusion")
    view = MainWindow()
    view.resize(860, 860)
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()
