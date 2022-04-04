"""Geocode utility functions"""
import requests
from haversine import haversine, Unit


class GeoCodeError(Exception):
    pass


def get_postcode_coordinates(postcode: str) -> tuple:
    """Geocode postcode with external API and return coordinates

    Args:
        postcode (str): Valid UK postcode

    Raises:
        GeoCodeError: Raises if postcode is not found
        GeoCodeError: Raises if postcode is found but there is no coordinates
            data in response

    Returns:
        tuple: tuple with longitude and latitude as floats
    """
    r = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
    if r.ok:
        geocode_data = r.json()
        try:
            return (
                geocode_data['result']['longitude'],
                geocode_data['result']['latitude'],
            )
        except KeyError:
            raise GeoCodeError
    raise GeoCodeError


def get_users_within_radius(
    long: float, lat: float, users_list: list, radius_miles: int
) -> list:
    """Filter user list within given radius. Return users that are equal to the
    radius from point of interest or less

    Args:
        long (float): Longitude of point of interest
        lat (float): Latitude of point of interest
        users_list (list): WalkerUser list of users
        radius_miles (int): Radius in miles

    Returns:
        list: Filtered list of WalkerUser objects
    """
    users_within_radius = []
    for i in users_list:
        distance_miles = haversine(
            (lat, long),
            (i.address_details.latitude, i.address_details.longitude),
            unit=Unit.MILES,
        )
        if distance_miles <= float(radius_miles):
            users_within_radius.append(i)
    return users_within_radius
