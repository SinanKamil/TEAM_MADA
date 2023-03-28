import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QStyleFactory, QDesktopWidget
from PyQt5.QtGui import QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize



class Page1(QWidget):
    def __init__(self, window):
        super().__init__()
        pixmap = QPixmap("images/home_page.png").scaled(window.width(), window.height(), Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.window = window

        # Create the button to go to admin login page
        self.adminlogin_btn = QPushButton(self)
        self.adminlogin_btn.setIcon(QIcon("images/adminlogin_btn.png"))
        self.adminlogin_btn.setIconSize(QSize(150, 50))
        self.adminlogin_btn.setFixedSize(QSize(150, 50))
        self.adminlogin_btn.clicked.connect(self.show_page2)
        self.adminlogin_btn.setStyleSheet("background-color: white; border: none;")

    def show_page2(self):
        self.window.stacked_widget.setCurrentWidget(self.window.page2)


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_page.png").scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class Page3(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_access.png").scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set the size of the window
        self.resize(1920, 1080)

        # Center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        cp.setX(cp.x() - round(self.width()/95))

        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle("GA")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.stacked_widget = QStackedWidget(self)
        self.page1 = Page1(self)
        self.page2 = Page2()
        self.page3 = Page3()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

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