from datetime import datetime


class CompletionLog:
    def __init__(self, habit_id: int, date: datetime = None):
        self.habit_id = habit_id
        self.date = date or datetime.utcnow()
