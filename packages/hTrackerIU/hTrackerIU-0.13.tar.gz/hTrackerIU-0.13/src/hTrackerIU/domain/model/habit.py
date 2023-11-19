from datetime import datetime

from .completion_log import CompletionLog
from .periodicity import Periodicity


class Habit:
    def __init__(
            self,
            description: str,
            periodicity: Periodicity,
            creation_date: datetime = None,
            id: int = None):
        self.id = id
        self.description = description
        self.periodicity = periodicity
        self.creation_date = creation_date or datetime.utcnow()
        self.completion_logs = []

    def complete(self):
        completion_log = CompletionLog(habit_id=self.id)
        self.completion_logs.append(completion_log)
