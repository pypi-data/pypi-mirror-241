from __future__ import annotations
from functools import lru_cache
from typing import List, Union
from datetime import datetime
from ...observable import Observable
from ...observation import Observation
from ...lstcalendar import LSTCalendar


@lru_cache(maxsize=None)
def calculate_observables(
    cal_start: Union[str, datetime],
    cal_end: Union[str, datetime],
    observations: List[Observation],
    latitude: Union[str, float],
    longitude: Union[str, float],
) -> List[Observable]:
    return sorted(
        LSTCalendar(
            cal_start, cal_end, observations=observations, latitude=latitude, longitude=longitude
        ).observables()
    )
