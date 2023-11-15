from __future__ import annotations  # Not required from python 3.11 onwards
from datetime import datetime, timedelta
from typing import List, Union
from ..Sun import Sun
from ...lstindex import LSTInterval, LSTIntervalType, normalize_interval
from ...utils import normalize_coordinates


def calculate_intervals(
    latitude: Union[str, float], longitude: Union[str, float], today_dt: datetime, self
) -> List[LSTInterval]:
    """
    Calculate intervals for a given date based on sun statistics.

    Parameters
    ----------

    Returns
    -------
    List[LSTInterval]
        A list of calculated intervals.
    """
    latitude, longitude = normalize_coordinates(latitude, longitude)

    today = today_dt
    today_sun = Sun(latitude, longitude, today)
    today_dawn_lst = today_sun.dawn_lst
    today_dawn_utc = today_sun.dawn
    today_sunrise_lst = today_sun.sunrise_lst
    today_sunrise_utc = today_sun.sunrise
    today_sunset_lst = today_sun.sunset_lst
    today_sunset_utc = today_sun.sunset
    today_dusk_lst = today_sun.dusk_lst
    today_dusk_utc = today_sun.dusk

    tomorrow = today + timedelta(days=1)
    tomorrow_sun = Sun(latitude, longitude, tomorrow)
    tomorrow_dawn_lst = tomorrow_sun.dawn_lst
    tomorrow_dawn_utc = tomorrow_sun.dawn
    tomorrow_sunrise_lst = tomorrow_sun.sunrise_lst
    tomorrow_sunrise_utc = tomorrow_sun.sunrise

    result = []

    # ALL DAY
    result.append(
        LSTInterval(
            0, 24, None, None, self, today, LSTIntervalType.ALL_DAY, today_sun, tomorrow_sun
        )
    )

    # SUNRISE_SUNSET
    SUNRISE_SUNSET = LSTInterval(
        *normalize_interval(today_sunrise_lst, today_sunset_lst),
        today_sunrise_utc.strftime("%H:%M"),
        today_sunset_utc.strftime("%H:%M"),
        self,
        today,
        LSTIntervalType.SUNRISE_SUNSET,
        today_sun,
        tomorrow_sun,
    )
    result.append(SUNRISE_SUNSET)
    if SUNRISE_SUNSET.end > 24:
        result.append(
            LSTInterval(
                0,
                today_sunset_lst,
                today_sunrise_utc.strftime("%H:%M"),
                today_sunset_utc.strftime("%H:%M"),
                self,
                today,
                LSTIntervalType.SUNRISE_SUNSET,
                today_sun,
                tomorrow_sun,
            )
        )

    # SUNSET_SUNRISE
    SUNSET_SUNRISE = LSTInterval(
        *normalize_interval(today_sunset_lst, tomorrow_sunrise_lst),
        today_sunset_utc.strftime("%H:%M"),
        tomorrow_sunrise_utc.strftime("%H:%M"),
        self,
        today,
        LSTIntervalType.SUNSET_SUNRISE,
        today_sun,
        tomorrow_sun,
    )
    result.append(SUNSET_SUNRISE)

    if SUNSET_SUNRISE.end > 24:
        result.append(
            LSTInterval(
                0,
                today_sunrise_lst,
                0,
                today_sunrise_utc.strftime("%H:%M"),
                self,
                today,
                LSTIntervalType.SUNSET_SUNRISE,
                today_sun,
                tomorrow_sun,
            )
        )

    # NIGHT
    NIGHT = LSTInterval(
        *normalize_interval(today_dusk_lst, tomorrow_dawn_lst),
        today_dusk_utc.strftime("%H:%M"),
        tomorrow_dawn_utc.strftime("%H:%M"),
        self,
        today,
        LSTIntervalType.NIGHT,
        today_sun,
        tomorrow_sun,
    )
    result.append(NIGHT)

    if NIGHT.end > 24:
        result.append(
            LSTInterval(
                0,
                today_dawn_lst,
                0,
                today_dawn_utc.strftime("%H:%M"),
                self,
                today,
                LSTIntervalType.NIGHT,
                today_sun,
                tomorrow_sun,
            )
        )

    return result
