"""
lstpressure.lstcalendar.Sun
"""
from typing import Union
from astral.sun import sun as calc_sun
from astral import LocationInfo
from ..utils import normalize_coordinates, normalize_yyyymmdd_to_datetime, utc_to_lst


class Sun:
    """
    Sun statistics for a particular date, at a particular lat/long.

    Attributes
    ----------
    dawn : datetime
        The dawn time for the given date and location.
    dawn_lst : datetime
        The dawn time converted to Local Sidereal Time (LST) for the given date and location.
    sunrise : datetime
        The sunrise time for the given date and location.
    sunrise_lst : datetime
        The sunrise time converted to Local Sidereal Time (LST) for the given date and location.
    noon : datetime
        The solar noon time for the given date and location.
    noon_lst : datetime
        The solar noon time converted to Local Sidereal Time (LST) for the given date and location.
    sunset : datetime
        The sunset time for the given date and location.
    sunset_lst : datetime
        The sunset time converted to Local Sidereal Time (LST) for the given date and location.
    dusk : datetime
        The dusk time for the given date and location.
    dusk_lst : datetime
        The dusk time converted to Local Sidereal Time (LST) for the given date and location.

    Parameters
    ----------
    latitude : Union[float, str]
        The latitude of the location in decimal degrees or string format.
    longitude : Union[float, str]
        The longitude of the location in decimal degrees or string format.
    yyyymmdd : str
        The date in 'YYYYMMDD' format for which sun statistics are calculated.

    Raises
    ------
    ValueError
        If the date format is incorrect or if the location coordinates cannot be normalized.

    """

    def __init__(
        self, latitude: Union[float, str], longitude: Union[float, str], yyyymmdd: str
    ) -> None:
        """
        Initialize a Sun object.

        Parameters
        ----------
        latitude : Union[float, str]
            The latitude of the location in decimal degrees or string format.
        longitude : Union[float, str]
            The longitude of the location in decimal degrees or string format.
        yyyymmdd : str
            The date in 'YYYYMMDD' format for which sun statistics are calculated.

        Raises
        ------
        ValueError
            If the date format is incorrect or if the location coordinates cannot be normalized.
        """
        latitude, longitude = normalize_coordinates(latitude, longitude)
        self.latitude = latitude
        self.longitude = longitude
        dt = normalize_yyyymmdd_to_datetime(yyyymmdd)
        location = LocationInfo(latitude=latitude, longitude=longitude)
        location.timezone = "UTC"
        self._attributes = calc_sun(location.observer, date=dt)

    @property
    def dawn(self):
        """
        The dawn time for the given date and location.

        Returns
        -------
        datetime
            The dawn time.
        """
        return self._attributes.get("dawn")

    @property
    def dawn_lst(self):
        """
        The dawn time converted to Local Sidereal Time (LST) for the given date and location.

        Returns
        -------
        datetime
            The dawn time in LST.
        """
        return utc_to_lst(self._attributes.get("dawn"), self.latitude, self.longitude)

    @property
    def sunrise(self):
        """
        The sunrise time for the given date and location.

        Returns
        -------
        datetime
            The sunrise time.
        """
        return self._attributes.get("sunrise")

    @property
    def sunrise_lst(self):
        """
        The sunrise time converted to Local Sidereal Time (LST) for the given date and location.

        Returns
        -------
        datetime
            The sunrise time in LST.
        """
        return utc_to_lst(self._attributes.get("sunrise"), self.latitude, self.longitude)

    @property
    def noon(self):
        """
        The solar noon time for the given date and location.

        Returns
        -------
        datetime
            The solar noon time.
        """
        return self._attributes.get("noon")

    @property
    def noon_lst(self):
        """
        The solar noon time converted to Local Sidereal Time (LST) for the given date and location.

        Returns
        -------
        datetime
            The solar noon time in LST.
        """
        return utc_to_lst(self._attributes.get("noon"), self.latitude, self.longitude)

    @property
    def sunset(self):
        """
        The sunset time for the given date and location.

        Returns
        -------
        datetime
            The sunset time.
        """
        return self._attributes.get("sunset")

    @property
    def sunset_lst(self):
        """
        The sunset time converted to Local Sidereal Time (LST) for the given date and location.

        Returns
        -------
        datetime
            The sunset time in LST.
        """
        return utc_to_lst(self._attributes.get("sunset"), self.latitude, self.longitude)

    @property
    def dusk(self):
        """
        The dusk time for the given date and location.

        Returns
        -------
        datetime
            The dusk time.
        """
        return self._attributes.get("dusk")

    @property
    def dusk_lst(self):
        """
        The dusk time converted to Local Sidereal Time (LST) for the given date and location.

        Returns
        -------
        datetime
            The dusk time in LST.
        """
        return utc_to_lst(self._attributes.get("dusk"), self.latitude, self.longitude)
