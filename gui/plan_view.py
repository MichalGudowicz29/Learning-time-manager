from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from controllers.plan_controller import PlanController

class PlanView(QWidget):
    def __init__(self, controller: PlanController):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.plan_name_input = QLineEdit()
        self.add_plan_button = QPushButton("Dodaj plan")
        self.plans_list = QListWidget()

        layout.addWidget(self.plan_name_input)
        layout.addWidget(self.add_plan_button)
        layout.addWidget(self.plans_list)

        self.add_plan_button.clicked.connect(self.add_plan)

    def add_plan(self):
        plan_name = self.plan_name_input.text()
        self.controller.create_plan(plan_name)
        self.update_plans_list()

    def update_plans_list(self):
        self.plans_list.clear()
        for plan in self.controller.get_all_plans():
            self.plans_list.addItem(plan.name)
