"""
lstpressure.lstindex.LSTInterval
"""

from __future__ import annotations
from datetime import datetime
from intervaltree import Interval
from .LSTIntervalType import LSTIntervalType
from ..lstcalendar import Sun, LSTCalendarDate
from ..observation import Observation
from typing import Union, Optional
from ..utils import normalize_yyyymmdd_to_datetime


def normalize_interval(start, end, days=1):
    """
    Normalize an interval's start and end times.

    This function ensures that the end time is greater than or equal to the start time, even if the interval spans multiple days.

    Parameters
    ----------
    start : float
        The start time of the interval (in hours).
    end : float
        The end time of the interval (in hours).
    days : int, optional
        The number of days the interval spans. Defaults to 1.

    Returns
    -------
    tuple
        A tuple containing the normalized start and end times.
    """
    if end < start:
        end += 24
    end += 24 * (days - 1)
    return (start, end)


class LSTInterval:
    """
    A wrapper around the intervaltree Interval class for easier access in the context of lst-pressure.

    Attributes
    ----------
    parent : Union[LSTCalendarDate, Observation], optional
        The parent object associated with the interval.
    interval : Interval
        The underlying interval object.
    start : float
        The start time of the interval (in hours).
    start_utc : Union[datetime, float]
        The start time of the interval in UTC.
    end : float
        The end time of the interval (in hours).
    end_utc : Union[datetime, float]
        The end time of the interval in UTC.
    type : LSTIntervalType, optional
        The type of the interval.
    dt : datetime, optional
        The datetime associated with the interval.
    sun : Sun, optional
        The Sun object associated with the interval.
    tomorrow_sun : Sun, optional
        The Sun object associated with the next day.

    Methods
    -------
    None
    """

    def __init__(
        self,
        start: float,
        end: float,
        start_utc: Union[datetime, float],
        end_utc: Union[datetime, float],
        parent: Optional[Union[LSTCalendarDate, Observation]] = None,
        dt: Optional[datetime] = None,
        type: Optional[LSTIntervalType] = None,
        sun: Optional[Sun] = None,
        tomorrow_sun: Optional[Sun] = None,
    ) -> None:
        """
        Initialize an LSTInterval object.

        Parameters
        ----------
        start : float
            The start time of the interval (in hours).
        end : float
            The end time of the interval (in hours).
        start_utc : Union[datetime, float]
            The start time of the interval in UTC.
        end_utc : Union[datetime, float]
            The end time of the interval in UTC.
        parent : Union[LSTCalendarDate, Observation], optional
            The parent object associated with the interval. Defaults to None.
        dt : datetime, optional
            The datetime associated with the interval. Defaults to None.
        type : LSTIntervalType, optional
            The type of the interval. Defaults to None.
        sun : Sun, optional
            The Sun object associated with the interval. Defaults to None.
        tomorrow_sun : Sun, optional
            The Sun object associated with the next day. Defaults to None.
        """
        self._type = type if type else None
        self._dt = normalize_yyyymmdd_to_datetime(dt) if dt else None
        self._sun = sun if sun else None
        self._tomorrow_sun = tomorrow_sun if tomorrow_sun else None
        self._parent = parent if parent else None
        self._interval = Interval(start, end, self)
        self._start_utc = start_utc
        self._end_utc = end_utc

    @property
    def parent(self) -> Union[LSTCalendarDate, Observation]:
        """
        The parent object associated with the interval.

        Returns
        -------
        Union[LSTCalendarDate, Observation]
            The parent object.
        """
        return self._parent

    @property
    def interval(self) -> Interval:
        """
        The underlying interval object.

        Returns
        -------
        Interval
            The interval object.
        """
        return self._interval

    @property
    def start(self) -> float:
        """
        The start time of the interval (in hours).

        Returns
        -------
        float
            The start time.
        """
        return self._interval[0]

    @property
    def start_utc(self) -> Union[datetime, float]:
        """
        The start time of the interval in UTC.

        Returns
        -------
        Union[datetime, float]
            The start time in UTC.
        """
        return self._start_utc

    @property
    def end(self) -> float:
        """
        The end time of the interval (in hours).

        Returns
        -------
        float
            The end time.
        """
        return self._interval[1]

    @property
    def end_utc(self) -> Union[datetime, float]:
        """
        The end time of the interval in UTC.

        Returns
        -------
        Union[datetime, float]
            The end time in UTC.
        """
        return self._end_utc

    @property
    def type(self) -> Optional[LSTIntervalType]:
        """
        The type of the interval.

        Returns
        -------
        Optional[LSTIntervalType]
            The type of the interval, or None if not specified.
        """
        return self._type

    @property
    def dt(self) -> Optional[datetime]:
        """
        The datetime associated with the interval.

        Returns
        -------
        Optional[datetime]
            The datetime, or None if not specified.
        """
        return self._dt

    @property
    def sun(self) -> Optional[Sun]:
        """
        The Sun object associated with the interval.

        Returns
        -------
        Optional[Sun]
            The Sun object, or None if not specified.
        """
        return self._sun

    @property
    def tomorrow_sun(self) -> Optional[Sun]:
        """
        The Sun object associated with the next day.

        Returns
        -------
        Optional[Sun]
            The Sun object for the next day, or None if not specified.
        """
        return self._tomorrow_sun
