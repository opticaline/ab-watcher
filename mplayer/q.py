from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog
from mplayer.player import BasePlayer


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.container = QWidget(self)
        self.container.setStyleSheet('background: red')
        self.button = QPushButton('Open', self)
        self.button.clicked.connect(self.handleButton)
        layout = QVBoxLayout(self)
        layout.addWidget(self.container)
        layout.addWidget(self.button)
        i = self.container.winId()
        print(i.__hash__())
        i = int(i)
        player = BasePlayer('mplayer', ['-wid', str(i)])
        self.mplayer = player.test()
        # mpylayer.MPlayerControl('mplayer', ['-wid', str(self.container.winId())])

    def handleButton(self):
        path = QFileDialog.getOpenFileName()
        print(self.mplayer.loadfile)
        self.mplayer.loadfile(path[0])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
