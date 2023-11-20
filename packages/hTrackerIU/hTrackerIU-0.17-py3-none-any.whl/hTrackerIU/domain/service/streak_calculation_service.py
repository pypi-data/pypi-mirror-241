from datetime import datetime
from typing import Callable, Dict, List, Optional, Tuple

is_log_within_period: Callable[[datetime, datetime, datetime], bool] = \
    lambda log_date, start_date, end_date: start_date < log_date <= end_date


def calculate_streak(log_dates: List[datetime],
                     period_start: datetime,
                     period_end: datetime,
                     streak_data: Tuple[int,
                                        int,
                                        int,
                                        Dict[datetime, int]],
                     today: datetime) -> Tuple[int,
                                               int,
                                               int,
                                               Dict[datetime, int]]:
    current_streak, max_streak, broken_streaks, consecutive_streaks = streak_data
    log_found = False

    for log_date in log_dates:
        if is_log_within_period(log_date, period_start, period_end):
            log_found = True
            current_streak += 1
            consecutive_streaks[log_date] = current_streak
            break

    if not log_found and period_end <= today and current_streak > 0:
        broken_streaks += 1
        current_streak = 0
        consecutive_streaks[period_end] = current_streak

    max_streak = max(current_streak, max_streak)
    return current_streak, max_streak, broken_streaks, consecutive_streaks


def update_streaks_data(current_date: datetime,
                        streak_data: Tuple[int,
                                           int,
                                           int,
                                           Dict[datetime, int]],
                        log_dates: List[datetime],
                        periodicity: str,
                        today: datetime) -> Tuple[int,
                                                  int,
                                                  int,
                                                  Dict[datetime, int]]:
    return streak_data if current_date > today else update_streaks_data(
        periodicity.get_next_date(current_date),
        calculate_streak(log_dates, current_date, periodicity.get_next_date(
            current_date), streak_data, today),
        log_dates,
        periodicity,
        today
    )


def get_streaks_info(logs: List[datetime],
                     periodicity: str,
                     creation_date: datetime,
                     today: Optional[datetime] = None) -> Tuple[int,
                                                                int,
                                                                int,
                                                                Dict[datetime, int]]:
    if not logs:
        return 0, 0, 0, {}
    today = today or datetime.utcnow()
    log_dates = sorted(log.date for log in logs)
    return update_streaks_data(
        creation_date, (0, 0, 0, {}), log_dates, periodicity, today)
