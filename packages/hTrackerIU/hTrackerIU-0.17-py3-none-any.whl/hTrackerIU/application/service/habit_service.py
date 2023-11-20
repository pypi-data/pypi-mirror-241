from .analytics_service import AnalyticsService
from ...domain.model.habit import Habit
from ...domain.model.periodicity import Periodicity
from ...infrastructure.repository.habit_repository import HabitRepository


class HabitService:
    def __init__(self, repository: HabitRepository,
                 analytics_service: AnalyticsService):
        self.repository = repository
        self.analytics_service = analytics_service

    def create_habit(
            self,
            description: str,
            periodicity: Periodicity) -> Habit:
        habit = Habit(description=description, periodicity=periodicity)
        self.repository.add(habit)
        return habit

    def complete_habit(self, habit_id):
        habit = self.repository.find_by_id(habit_id)
        if not habit:
            raise ValueError(f"No habit found with id {habit_id}")
        habit.complete()
        self.repository.save(habit)

    def delete_habit(self, habit_id: int) -> None:
        habit = self.repository.find_by_id(habit_id)
        if habit:
            self.repository.remove(habit)

    def get_habit_by_id(self, habit_id: int) -> dict:
        habit = self.repository.find_by_id(habit_id)
        if habit:
            analytics_data = self.get_analytics_data(habit.id)
            return {'habit': habit, **analytics_data}
        return None

    def list_all_tracked_habits(self) -> list:
        habits = self.repository.get_all()
        result = []
        for habit in habits:
            analytics_data = self.get_analytics_data(habit.id)
            result.append({'habit': habit, **analytics_data})
        return result

    def get_analytics_data(self, habit_id):
        habit = self.repository.find_by_id(habit_id)
        return {
            'consecutive_streaks': self.analytics_service.consecutive_streaks(
                habit.completion_logs,
                habit.periodicity,
                habit.creation_date),
            'current_streak': self.analytics_service.current_streak(
                habit.completion_logs,
                habit.periodicity,
                habit.creation_date),
            'longest_streak': self.analytics_service.longest_streak(
                habit.completion_logs,
                habit.periodicity,
                habit.creation_date)}
