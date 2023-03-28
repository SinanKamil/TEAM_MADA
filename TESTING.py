import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation
from PyQt5.QtCore import QEasingCurve


class Page1(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/home_page.png").scaled(1900, 1000, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_page.png").scaled(1900, 1000, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class Page3(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_access.png").scaled(1900, 1000, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1920, 1080)
        self.setWindowTitle("3-Page GUI with Smooth Transitions")

        self.stacked_widget = QStackedWidget(self)
        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        button_layout = QHBoxLayout()
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")
        self.button3 = QPushButton("Page 3")
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        layout.addLayout(button_layout)

        self.button1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page1))
        self.button2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page2))
        self.button3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page3))

        self.show()

        self.animation = QPropertyAnimation(self.stacked_widget, b"geometry")
        self.animation.setDuration(500)
        easing_curve = QEasingCurve.InOutQuad

        # Set the easing curve of the animation
        self.animation.setEasingCurve(easing_curve)

    def animate(self, start, end):
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
