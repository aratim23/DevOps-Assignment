import pytest
from ACEest_Fitness import WorkoutManager

def test_add_workout_valid():
    wm = WorkoutManager()
    wm.add_workout("Running", 30)
    assert wm.workouts == [{"workout": "Running", "duration": 30}]

def test_add_workout_invalid_duration():
    wm = WorkoutManager()
    with pytest.raises(ValueError):
        wm.add_workout("Yoga", "abc")
