"""
lstpressure.lstcalendar.LSTCalendarDate
"""
from __future__ import annotations  # Not required from Python 3.11 onwards
from datetime import timedelta, date
from typing import List
from lstpressure.lstindex import LSTInterval
from ..lstcalendar import LSTCalendar
from ..observable import Observable
from .Sun import Sun
from .helpers import calculate_intervals


class LSTCalendarDate:
    """
    Represents a date within the LSTCalendar.

    Parameters
    ----------
    dt : date
        The date for which LSTCalendarDate is instantiated.
    cal : LSTCalendar
        The parent LSTCalendar object that manages this date.

    Attributes
    ----------
    dt : date
        The date for which LSTCalendarDate is instantiated.
    tomorrow_dt : date
        The date following the current date.
    sun : Sun
        An object representing sun statistics for the current date.
    tomorrow_sun : Sun
        An object representing sun statistics for the following date.
    calendar : LSTCalendar
        The parent LSTCalendar object that manages this date.
    intervals : List[LSTInterval]
        A list of LSTInterval objects associated with this date.

    Methods
    -------
    observables() -> List[Observable]
        Retrieve observable observations for this date.
    to_yyyymmdd() -> str
        Convert the date to a string in the 'YYYYMMDD' format.
    """

    def __init__(self, dt, cal) -> None:
        """
        Initialize an LSTCalendarDate object.

        Parameters
        ----------
        dt : date
            The date for which LSTCalendarDate is instantiated.
        cal : LSTCalendar
            The parent LSTCalendar object that manages this date.

        Raises
        ------
        TypeError
            If the "cal" argument is missing.
        """
        if not cal:
            raise TypeError(
                'Missing "cal" argument, LSTCalendarDate instances must be instantiated via instances of LSTCalendar so that the self.cal can be assigned'
            )

        self.dt: date = dt
        self.tomorrow_dt = dt + timedelta(days=1)
        self.sun = Sun(cal.latitude, cal.longitude, dt)
        self.tomorrow_sun = Sun(cal.latitude, cal.longitude, dt + timedelta(days=1))
        self.calendar: LSTCalendar = cal
        self.intervals: List[LSTInterval] = calculate_intervals(
            cal.latitude, cal.longitude, dt, self
        )
        for interval in self.intervals:
            cal.interval_index.insert(interval.interval)

    def observables(self) -> List[Observable]:
        """
        Retrieve observable observations for this date.

        Returns
        -------
        List[Observable]
            A list of observable observations for this date.
        """
        result = set()

        # Cycle through dt intervals
        for cal_interval in self.intervals:
            cal_interval_end = cal_interval.end
            interval_type = cal_interval.type
            query = cal_interval.interval

            # Note that overlap() returns a Set
            query_result = self.calendar.observations_index.overlap(query)

            for obs_interval_raw in query_result:
                (
                    obs_window_start,
                    obs_window_end,
                    obs_interval,
                ) = obs_interval_raw
                obs = obs_interval.parent
                utc_constraints = obs.utc_constraints
                duration = obs.duration

                if (utc_constraints is None or len(utc_constraints) == 0) or (
                    len(utc_constraints) > 0 and interval_type in utc_constraints
                ):
                    if query.end > obs_window_start:
                        if (
                            obs_window_start + duration < cal_interval_end
                            or obs_window_end + duration < cal_interval_end
                        ):
                            result.add(Observable(cal_interval, obs))

        return list(result)

    def to_yyyymmdd(self) -> str:
        """
        Convert the date to a string in the 'YYYYMMDD' format.

        Returns
        -------
        str
            The date in 'YYYYMMDD' format.
        """
        return self.dt.strftime("%Y%m%d")
