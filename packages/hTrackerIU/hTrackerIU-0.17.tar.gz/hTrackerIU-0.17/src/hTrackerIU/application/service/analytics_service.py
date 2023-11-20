from datetime import datetime
from typing import List

from ...domain.model.periodicity import Periodicity
from ...domain.service.streak_calculation_service import get_streaks_info
from ...infrastructure.repository.habit_repository import HabitRepository


class AnalyticsService:
    def __init__(self, repository: HabitRepository):
        self.repository = repository

    @staticmethod
    def current_streak(
            logs: List[datetime],
            periodicity: str,
            creation_date: datetime,
            today: datetime = None) -> int:
        current_streak, _, _, _ = get_streaks_info(
            logs, periodicity, creation_date, today)
        return current_streak

    @staticmethod
    def longest_streak(
            logs: List[datetime],
            periodicity: str,
            creation_date: datetime,
            today: datetime = None) -> int:
        _, max_streak, _, _ = get_streaks_info(
            logs, periodicity, creation_date, today)
        return max_streak

    @staticmethod
    def broken_streaks_count(
            logs: List[datetime],
            periodicity: str,
            creation_date: datetime,
            today: datetime = None) -> int:
        _, _, count, _ = get_streaks_info(
            logs, periodicity, creation_date, today)
        return count

    @staticmethod
    def consecutive_streaks(
            logs: List[datetime],
            periodicity: str,
            creation_date: datetime,
            today: datetime = None) -> int:
        _, _, _, consecutive_streaks = get_streaks_info(
            logs, periodicity, creation_date, today)
        return consecutive_streaks

    def list_habits_by_periodicity(self, periodicity: Periodicity) -> list:
        return self.repository.find_by_periodicity(periodicity)

    def longest_streak_for_all_habits(self) -> int:
        habits = self.repository.get_all()
        max_streaks = [
            self.longest_streak(
                habit.completion_logs,
                habit.periodicity,
                habit.creation_date) for habit in habits]
        return max(max_streaks, default=0)

    def longest_streak_for_habit(self, habit_id: int) -> int:
        habit = self.repository.find_by_id(habit_id)
        return self.longest_streak(
            habit.completion_logs,
            habit.periodicity,
            habit.creation_date) if habit else 0

    def struggled_habits_last_month(self, today: datetime = None) -> list:

        habits = self.repository.get_all()
        struggled_habits = []

        for habit in habits:
            count = self.broken_streaks_count(
                habit.completion_logs,
                habit.periodicity,
                habit.creation_date,
                today)
            if count > 3:
                struggled_habits.append(habit)

        return struggled_habits
