# coding:utf-8
import sys
from PyQt5.QtCore import QEvent, QPoint, Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from qfluentwidgets import ToolTip, ToolTipFilter, setTheme, Theme, PushButton


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.hBox = QHBoxLayout(self)
        self.button1 = PushButton('キラキラ', self)
        self.button2 = PushButton('食べた愛', self)
        self.button3 = PushButton('シアワセ', self)
        self._toolTip = ToolTip(parent=self)

        # use dark theme
        # setTheme(Theme.DARK)

        self.button1.setToolTip('aiko - キラキラ ✨')
        self.button2.setToolTip('aiko - 食べた愛 🥰')
        self.button3.setToolTip('aiko - シアワセ 😊')
        self.button1.setToolTipDuration(1000)
        self.button2.setToolTipDuration(5000)

        self.button1.installEventFilter(self)
        self.button2.installEventFilter(self)
        self.button3.installEventFilter(ToolTipFilter(self.button3))

        self.button1.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=S0bXDRY1DGM&list=RDMM&index=1')))
        self.button2.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=CZLs8GuCq2U&list=RDMM&index=4')))
        self.button3.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            'https://www.youtube.com/watch?v=fp-yJUB7sS8&list=RDMM&index=3')))

        self.hBox.setContentsMargins(24, 24, 24, 24)
        self.hBox.setSpacing(16)
        self.hBox.addWidget(self.button1)
        self.hBox.addWidget(self.button2)
        self.hBox.addWidget(self.button3)

        self.resize(480, 240)
        self._toolTip.hide()

        self.setStyleSheet('Demo{background:white}')

    def eventFilter(self, obj, e: QEvent):
        if obj is self:
            return super().eventFilter(obj, e)

        tip = self._toolTip
        if e.type() == QEvent.Enter:
            tip.setText(obj.toolTip())
            tip.setDuration(obj.toolTipDuration())
            tip.adjustPos(obj.mapToGlobal(QPoint()), obj.size())
            tip.show()
        elif e.type() == QEvent.Leave:
            tip.hide()
        elif e.type() == QEvent.ToolTip:
            return True

        return super().eventFilter(obj, e)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()
