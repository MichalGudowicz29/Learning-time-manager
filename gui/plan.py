from datetime import datetime

class Plan:
    def __init__(self, name: str, start_date: datetime = None):
        self.name = name
        self.start_date = start_date or datetime.now()
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def get_duration(self):
        # Przykładowa logika
        return len(self.tasks) * 2  # załóżmy, że każde zadanie trwa 2 dni

    def is_active(self):
        return datetime.now() >= self.start_date
