from enum import Enum
from typing import Optional

from fastapi import APIRouter, Depends, Query

from .schemas import HabitCreateSchema

from ..application.service.analytics_service import AnalyticsService
from ..application.service.habit_service import HabitService
from ..domain.model.periodicity import Periodicity
from ..infrastructure.orm.session import SessionLocal
from ..infrastructure.repository.habit_repository import HabitRepository
from .dependencies import get_analytics_service, get_habit_service

router = APIRouter()


@router.post("/habits/",
             response_model=HabitCreateSchema,
             operation_id="createHabit")
def create_habit(
        habit: HabitCreateSchema,
        habit_service: HabitService = Depends(get_habit_service)):
    return habit_service.create_habit(habit.description, habit.periodicity)


@router.get("/habits/", operation_id="getAllHabits")
def list_habits(
    periodicity: Optional[str] = Query(None),
    habit_service: HabitService = Depends(get_habit_service),
    analytics_service: AnalyticsService = Depends(get_analytics_service)
):
    if periodicity:
        periodicity_enum = Periodicity(periodicity)
        return analytics_service.list_habits_by_periodicity(periodicity_enum)
    return habit_service.list_all_tracked_habits()


@router.put("/habits/{habit_id}/complete", operation_id="completeHabitTask")
def complete_habit(
        habit_id: int,
        habit_service: HabitService = Depends(get_habit_service)):
    habit_service.complete_habit(habit_id)
    return {"status": "completed"}


@router.delete("/habits/{habit_id}", operation_id="deleteHabit")
def delete_habit(
        habit_id: int,
        habit_service: HabitService = Depends(get_habit_service)):
    habit_service.delete_habit(habit_id)
    return {"status": "deleted"}


@router.get("/habits/analytics/longest-streak",
            operation_id="getLongestStreakForAllHabits")
def get_longest_streak(
        analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return {"streak": analytics_service.longest_streak_for_all_habits()}


@router.get("/habits/{habit_id}/analytics/streak",
            operation_id="getLongestStreakForHabit")
def get_longest_streak_for_habit(
        habit_id: int,
        analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return {"streak": analytics_service.longest_streak_for_habit(habit_id)}


@router.get("/habits/analytics/struggled-last-month",
            operation_id="getStruggledHabitsLastMonth")
def get_struggled_habits_last_month(
        analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return analytics_service.struggled_habits_last_month()


@router.get("/habits/{habit_id}", operation_id="getHabitDetails")
def get_habit(
        habit_id: int,
        habit_service: HabitService = Depends(get_habit_service)):
    return habit_service.get_habit_by_id(habit_id)
