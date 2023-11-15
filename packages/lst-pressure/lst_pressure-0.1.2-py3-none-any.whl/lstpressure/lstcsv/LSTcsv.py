"""
lstpressure.lstcsv.LSTcsv
"""
from __future__ import annotations
import pandas as pd
import warnings
from pandas import DataFrame
from datetime import datetime
from typing import Optional, Union, List, Callable
from ..observation import Observation
from ..observable import Observable
from .helpers import calculate_observations, calculate_observables
from collections import defaultdict


class LSTcsv:
    """
    Wrap the LSTCalendar/Observation API for use with SARAO OPT
    CSV downloads.

    Parameters
    ----------
    input : Union[DataFrame, str, List[List[str]]]
        The input data source, which can be a DataFrame, a file path to a CSV file, or a list of lists (rows).
    input_filter : Optional[Callable[[List[List[str]]], bool]], optional
        A filter function to apply to the input data during instantiation. Defaults to None.
    observation_filter : Optional[Callable[[List[Observation]], bool]], optional
        A filter function to apply to the observations data after filtering the input data. Defaults to None.
    calendar_start : Optional[Union[str, datetime]], optional
        The start date for the LST calendar. Defaults to the current date.
    calendar_end : Optional[Union[str, datetime]], optional
        The end date for the LST calendar. Defaults to the value of calendar_start.

    Attributes
    ----------
    df : DataFrame
        The filtered DataFrame based on the input data and filters.
    input : Union[str, List[list[str]]]
        The input data source, which can be a file path to a CSV file, a DataFrame, or a list of lists (rows).
    calendar_start : Union[str, datetime]
        The start date for the LST calendar.
    calendar_end : Union[str, datetime]
        The end date for the LST calendar.
    observation_filter : Callable[[List[Observation]], bool]
        The filter function applied to the observations data.
    observations : List[Observation]
        A list of Observation objects based on the filtered data.
    observables : List[Observable]
        A list of Observable objects calculated based on the observations.

    Methods
    -------
    write_to_csv(output: str) -> None:
        Write the observables data to a CSV file.

    """

    def __init__(
        self,
        input: Union[DataFrame, str, List[List[str]]],
        input_filter: Optional[Callable[[List[str]], bool]] = None,
        observation_filter: Optional[Callable[[Observation], bool]] = None,
        calendar_start: Optional[Union[str, datetime]] = None,
        calendar_end: Optional[Union[str, datetime]] = None,
        latitude: Union[str, float] = "-30:42:39.8",
        longitude: Union[str, float] = "21:26:38.0",
    ) -> None:
        """
        Initialize an LSTcsv object.

        Parameters
        ----------
        input : Union[DataFrame, str, List[List[str]]]
            The input data source, which can be a DataFrame, a file path to a CSV file, or a list of lists (rows).
        input_filter : Optional[Callable[[List[str]], bool]], optional
            A filter function to apply to the input data during instantiation. Defaults to None.
        observation_filter : Optional[Callable[[Observation], bool]], optional
            A filter function to apply to the observations data after filtering the input data. Defaults to None.
        calendar_start : Optional[Union[str, datetime]], optional
            The start date for the LST calendar. Defaults to the current date.
        calendar_end : Optional[Union[str, datetime]], optional
            The end date for the LST calendar. Defaults to the value of calendar_start.
        latitude : Union[str, float], optional
            Latitude for the location. Defaults to -30:42:39.8.
        longitude : Union[str, float], optional
            Longitude for the location. Defaults to 21:26:38.0.

        Raises
        ------
        TypeError
            If the input is not a valid type (DataFrame, str, or list of lists).
        """
        self._input = input
        self._calendar_start = (
            calendar_start if calendar_start else datetime.now().strftime("%Y%m%d")
        )
        self._calendar_end = calendar_end or calendar_start

        self._latitude = latitude
        self._longitude = longitude

        if input_filter and observation_filter:
            warnings.warn(
                "Both 'input_filter' and 'observation_filter' are set. Be aware that 'input_filter' "
                "is applied during instantiation with CSV row data, while 'observation_filter' is applied "
                "afterwards to the already filtered data. Future versions of this API might deprecate "
                "'observation_filter' to streamline data processing.",
                category=UserWarning,
            )

        self._observation_filter = observation_filter if observation_filter else lambda _: True
        input_filter = input_filter if input_filter else lambda _: True

        # Process input based on its type
        if isinstance(input, str):
            # Input is a file path, read CSV and filter rows
            df = pd.read_csv(input)
        elif isinstance(input, list):
            # Input is a list of lists, the first list is treated as header
            header, *data = input
            df = pd.DataFrame(data, columns=header)
        elif isinstance(input, DataFrame):
            # Input is already a DataFrame, make a copy
            df = input.copy()
        else:
            raise TypeError(
                "Input must be a path to a CSV file, a DataFrame, or a list of lists (rows)."
            )

        # Apply the filter to the DataFrame
        self._df = df[df.apply(input_filter, axis=1)]

    @property
    def df(self) -> DataFrame:
        """
        The filtered DataFrame based on the input data and filters.

        Returns
        -------
        DataFrame
            The filtered DataFrame.
        """
        return self._df

    @property
    def input(self) -> Union[str, List[list[str]]]:
        """
        The input data source, which can be a file path to a CSV file, a DataFrame, or a list of lists (rows).

        Returns
        -------
        Union[str, List[list[str]]]
            The input data source.
        """
        return self._input

    @property
    def calendar_start(self) -> Union[str, datetime]:
        """
        The start date for the LST calendar.

        Returns
        -------
        Union[str, datetime]
            The start date.
        """
        return self._calendar_start

    @property
    def calendar_end(self):
        """
        The end date for the LST calendar.

        Returns
        -------
        Union[str, datetime]
            The end date.
        """
        return self._calendar_end

    @property
    def observation_filter(self) -> Callable[[List[Observation]], bool]:
        """
        The filter function applied to the observations data.

        Returns
        -------
        Callable[[List[Observation]], bool]
            The observation filter function.
        """
        return self._observation_filter

    @property
    def latitude(self) -> Union[str, float]:
        return self._latitude

    @property
    def longitude(self) -> Union[str, float]:
        return self._longitude

    @property
    def observations(self) -> List[Observation]:
        """
        A list of Observation objects based on the filtered data.

        Returns
        -------
        List[Observation]
            A list of Observation objects.
        """
        return calculate_observations(self)

    @property
    def observables(self) -> List[Observable]:
        """
        A list of Observable objects calculated based on the observations.

        Returns
        -------
        List[Observable]
            A list of Observable objects.
        """
        return calculate_observables(
            self.calendar_start, self.calendar_end, self.observations, self.latitude, self.longitude
        )

    def write_to_csv(self, output: str) -> None:
        """
        Write the observables data to a CSV file.

        Parameters
        ----------
        output : str
            The path to the output CSV file.
        """
        data = [o.to_tuple() for o in self.observables]

        # Use a defaultdict to group data by date
        grouped_data = defaultdict(list)
        for record in data:
            (
                id,
                proposal_id,
                date,
                constraint,
                duration,
                lst_window_start,
                lst_window_end,
                lst_interval_start,
                lst_interval_end,
                utc_interval_start,
                utc_interval_end,
            ) = record
            grouped_data[date].append(
                [
                    id,
                    proposal_id,
                    constraint,
                    duration,
                    lst_window_start,
                    lst_window_end,
                    lst_interval_start,
                    lst_interval_end,
                    utc_interval_start,
                    utc_interval_end,
                ]
            )

        # Create a list of dictionaries to construct the DataFrame
        data_list = [
            {
                "Date": date,
                "Observation ID": id,
                "Proposal ID": proposal_id,
                "UTC interval": constraint,
                "Duration": duration,
                "Observation LST start": lst_window_start,
                "Observation LST end": lst_window_end,
                "Observable LST start": lst_interval_start,
                "Observable LST end": lst_interval_end,
                "Observable UTC start": utc_interval_start,
                "Observable UTC end": utc_interval_end,
            }
            for date, id_value in grouped_data.items()
            for id, proposal_id, constraint, duration, lst_window_start, lst_window_end, lst_interval_start, lst_interval_end, utc_interval_start, utc_interval_end in id_value
        ]

        # Construct the DataFrame
        df = pd.DataFrame(data_list)

        # Write dataFrame to CSV
        df.to_csv(output, sep=",", quotechar='"', quoting=1, index=False, encoding="utf-8")
