"""
lstpressure.lstcalendar.LSTCalendar
"""
from __future__ import annotations  # Not required from python 3.11 onwards
from datetime import timedelta, datetime
from typing import Union, List, Dict, Optional
from ..observation import Observation
from ..observable import Observable
from .LSTCalendarDate import LSTCalendarDate
from ..lstindex import LSTIndex, LSTInterval
from ..utils import (
    normalize_yyyymmdd_to_datetime,
    normalize_coordinates,
)


class LSTCalendar:
    """
    Calendar tailored for LST (Local Sidereal Time) related interval lookups.

    Attributes
    ----------
    start : datetime
        The beginning of the date range for the calendar.
    end : datetime
        The conclusion of the date range for the calendar.
    latitude : float
        The geographic latitude in decimal degrees. Defaults to 0.
    longitude : float
        The geographic longitude in decimal degrees. Defaults to 0.
    interval_index : LSTIndex
        An index to manage intervals efficiently.
    observations_index : LSTIndex
        An index to manage observations efficiently.
    dates : List[LSTCalendarDate]
        A list containing dates and corresponding sun statistics within the range.

    Methods
    -------
    __init__(start, end, latitude=0, longitude=0, observations=[])
        Initialize the LSTCalendar object.
    __enter__()
        Enter context management.
    __exit__(exc_type, exc_val, exc_tb)
        Exit context management.
    load_observations(observations: List[Observation]) -> LSTCalendar
        Load a list of observations and insert their intervals into the observation index.
    observables(observations: Optional[List[Observation]] = None) -> List[Observable]
        Retrieve observable observations for the dates maintained by this calendar.

    """

    def __enter__(self):
        """
        Enter context management.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit context management.
        """
        pass

    def __init__(
        self,
        start: Union[str, datetime],
        end: Optional[Union[str, datetime]] = None,
        observations: List[Observation] = [],
        latitude: Union[str, float] = "-30:42:39.8",
        longitude: Union[str, float] = "21:26:38.0",
    ):
        """
        Initialize the LSTCalendar object.

        Parameters
        ----------
        start : Union[str, datetime]
            Start date of the calendar range.
        end : (Optional) Union[str, datetime]
            End date of the calendar range. Defaults to start.
        observations : List[Observation], optional
            List of observation instances. Called load_observations method under the hood.
        latitude : Union[str, float], optional
            Latitude for the location. Defaults to -30:42:39.8.
        longitude : Union[str, float], optional
            Longitude for the location. Defaults to 21:26:38.0.

        Raises
        ------
        ValueError
            If the start date is after the end date.
        """
        start = normalize_yyyymmdd_to_datetime(start)
        end = start if not end else normalize_yyyymmdd_to_datetime(end)

        if start > end:
            raise ValueError("start day should be <= end day")

        latitude, longitude = normalize_coordinates(latitude, longitude)
        self.latitude = latitude
        self.longitude = longitude
        self._interval_index = LSTIndex()
        self._observations_index = LSTIndex()
        self._dates = [
            LSTCalendarDate(start + timedelta(days=d), self)
            for d in range(0, (end - start).days + 1)
        ]
        self.load_observations(observations)

    @property
    def interval_index(self) -> LSTIndex:
        """
        Property to retrieve the interval index.

        Returns
        -------
        LSTIndex
            An index to manage intervals efficiently.
        """
        return self._interval_index

    @property
    def observations_index(self) -> LSTIndex:
        """
        Property to retrieve the observations index.

        Returns
        -------
        LSTIndex
            An index to manage observations efficiently.
        """
        return self._observations_index

    @property
    def dates(self) -> List[LSTCalendarDate]:
        """
        Property to retrieve the list of dates.

        Returns
        -------
        List[LSTCalendarDate]
            A list containing dates and corresponding sun statistics within the range.
        """
        return self._dates

    def load_observations(self, observations: List[Observation]) -> LSTCalendar:
        """
        Load a list of observations, set the calendar attribute for each observation,
        and insert their intervals into the observation index.

        Observations must have unique IDs.

        Parameters
        ----------
        observations : List[Observation]
            A list of observation instances.

        Returns
        -------
        LSTCalendar
            The LSTCalendar object.
        """
        self._observations = []
        self._observations_index = LSTIndex()
        _ids = set()
        for observation in observations:
            if observation.id in _ids:
                raise ValueError(
                    f"Duplicate ID detected: '{observation.id}'. "
                    "Each observation must have a unique ID to be loaded into the calendar."
                )
            _ids.add(observation.id)
            observation.calendar = self
            self._observations.append(observation)
            for interval in observation.intervals:
                self.observations_index.insert(interval.interval)
        return self

    @property
    def observations(self) -> List[Dict[str, Union[LSTInterval, Observation]]]:
        """
        Property to retrieve the list of observations.

        Returns
        -------
        List[Dict[str, Union[LSTInterval, Observation]]]
            A list of observations.
        """
        return self._observations

    @observations.setter
    def observations(self, observations: List[Observation]) -> None:
        """
        Setter for the observations property. It serves as an alias for the load_observations method.

        Parameters
        ----------
        observations : List[Observation]
            A list of observation instances.

        Returns
        -------
        None
        """
        self.load_observations(observations)

    def observables(self, observations: Optional[List[Observation]] = None) -> List[Observable]:
        """
        Retrieve observable observations for the dates maintained by this calendar.

        This method processes a list of dates within the calendar and aggregates their observable observations into observation windows. If a list of observations is provided, it replaces the current observations of the calendar with the new list.

        Parameters
        ----------
        observations : Optional[List[Observation]], optional
            A list of Observation objects to process, which is optional. If provided, it overwrites any existing observations in the calendar.

        Raises
        ------
        TypeError
            If no observations have been loaded into the calendar and none are provided.

        Returns
        -------
        List[Observable]
            A list of aggregated observation windows, each representing observable observations for a specific date in the calendar.

        Example usage:

        .. code-block:: python

            calendar = Calendar()
            calendar.load_dates(dates)
            try:
                observation_windows = calendar.observable_observations()
            except TypeError as e:
                print(e)

        """
        # If observations provided as an argument, assume the intent is to overwrite
        if observations:
            self.load_observations(observations)

        if not self.observations:
            raise TypeError(
                "No observations have been loaded on this calendar, and no observations have been provided as an argument"
            )

        results = []
        for dt in self.dates:
            results = results + dt.observables()

        return results
