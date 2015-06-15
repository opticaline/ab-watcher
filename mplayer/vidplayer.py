#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mpylayer
from PyQt4 import QtGui, QtCore
from mplayer.player import BasePlayer


class VidPlayer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(VidPlayer, self).__init__(parent)
        self.centralWidget = QtGui.QWidget(self)
        self.video = QtGui.QWidget(self.centralWidget)
        self.video.setStyleSheet('background: red')
        self.playButton = QtGui.QPushButton('Play', self.centralWidget)
        self.stopButton = QtGui.QPushButton('Stop', self.centralWidget)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.addWidget(self.playButton)
        self.buttonsLayout.addWidget(self.stopButton)
        self.mainLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.mainLayout.addWidget(self.video)
        self.mainLayout.addLayout(self.buttonsLayout)
        self.setCentralWidget(self.centralWidget)

        i = self.video.winId()
        player = BasePlayer('mplayer', ['-wid', str(i)])
        self.mplayer = player.test()

        # self.mplayer = mpylayer.MPlayerControl(extra_args=['-wid', str(self.video.winId())])

        self.connect(self.playButton, QtCore.SIGNAL('clicked(bool)'), self.play)
        self.connect(self.stopButton, QtCore.SIGNAL('clicked(bool)'), self.stop)

    def play(self):
        self.mplayer.loadfile('test.mkv')

    def stop(self):
        self.mplayer.stop()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    vp = VidPlayer()
    vp.show()
    sys.exit(app.exec_())
