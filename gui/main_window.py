from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from .plan_view import PlanView
from .calendar_view import CalendarView
from .profile_view import ProfileView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning Plan Manager")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Dodaj grafikę po lewej stronie
        # (Załóżmy, że masz plik 'logo.png' w katalogu 'assets/images/')
        logo_label = QLabel()
        pixmap = QPixmap("assets/images/logo.png")
        logo_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignLeft)

        # Przyciski do przełączania widoków
        self.plan_button = QPushButton("Ustal plan")
        self.calendar_button = QPushButton("Kalendarz")
        self.profile_button = QPushButton("Profil")

        layout.addWidget(self.plan_button)
        layout.addWidget(self.calendar_button)
        layout.addWidget(self.profile_button)

        # Stos widoków
        self.stacked_widget = QStackedWidget()
        self.plan_view = PlanView()
        self.calendar_view = CalendarView()
        self.profile_view = ProfileView()

        self.stacked_widget.addWidget(self.plan_view)
        self.stacked_widget.addWidget(self.calendar_view)
        self.stacked_widget.addWidget(self.profile_view)

        layout.addWidget(self.stacked_widget)

        # Połącz przyciski z funkcjami przełączania
        self.plan_button.clicked.connect(self.show_plan)
        self.calendar_button.clicked.connect(self.show_calendar)
        self.profile_button.clicked.connect(self.show_profile)

    def show_plan(self):
        self.stacked_widget.setCurrentWidget(self.plan_view)

    def show_calendar(self):
        self.stacked_widget.setCurrentWidget(self.calendar_view)

    def show_profile(self):
        self.stacked_widget.setCurrentWidget(self.profile_view)
