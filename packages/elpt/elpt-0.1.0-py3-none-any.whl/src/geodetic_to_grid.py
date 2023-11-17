import numpy as np


def degr_min_sec_to_decimal_degr(data: tuple) -> float:
    """Transform an angle expressed in degrees, minutes and seconds to
    an angle expressed as decimal degrees.

    Args:
        data (tuple): angle in degrees, minutes and seconds

    Returns:
        float: angle in decimal degrees
    """
    decimal_degr = data[0] + data[1] / 60.0 + data[2] / 3600.0
    return decimal_degr


def degr_to_radians(degrees: float) -> float:
    """Transform angle expressed in degrees to angle expressed in radians.

    Args:
        degrees (float): angle in degrees

    Returns:
        float: angle in radians
    """
    radians = degrees * (np.pi / 180)
    return radians


def get_transverse_mercator_parameters(
    projection: str,
) -> tuple[float, float, float, float]:
    """Returns the transverse mercator parameters of a projection.

    Symbols and definitions:
        lam0    longitude of central meridian
        k0      scale factor along the central meridian
        FN      false northing
        FE      false easting

    Args:
        projection (str): name of projection

    Returns:
        tuple[float, float, float, float]: transverse mercator parameters
    """
    if projection == "test":
        lam0 = (13, 35, 7.692000)
        k0 = 1.000002540000
        FN = -6226307.8640
        FE = 84182.8790

    if projection == "SWEREF99TM":
        lam0 = (15, 0, 0)
        k0 = 0.9996
        FN = 0
        FE = 500000

    lam0 = degr_min_sec_to_decimal_degr(lam0)
    lam0 = degr_to_radians(lam0)

    return lam0, k0, FN, FE


def get_ellipsoidal_parameters(ellips: str) -> tuple[float, float]:
    """Return the ellipsoidal parameters associated with an ellips.

    Args:
        ellips (str): name of ellips

    Returns:
        tuple[float, float]: ellipsoidal parameters
    """
    if ellips == "GRS1980":
        a = 6378137.0000
        f = 1 / 298.257222101
    return a, f


def from_ellipsoidal_parameters(a: float, f: float) -> tuple[float, float, float]:
    """Computes addtional parameters from ellipsoidal parameters.

    Args:
        a (float): semi-major axis of the ellipsoid
        f (float): flattening of the ellipsoid

    Returns:
        tuple[float, float, float]: additional parameters associated with ellipsoidal parameters
    """
    e_cubed = f * (2 - f)
    e = np.sqrt(e_cubed)
    n = f / (2 - f)
    a_hat = (a / (1 + n)) * (1 + (1 / 4) * n**2 + (1 / 64) * n**4)
    return e, n, a_hat


def geodetic_to_grid(
    phi: tuple, lam: tuple, ellips: str, projection: str
) -> tuple[float, float]:
    """Perform Gauss-Kruger transformation from geodetic latitude and longitude
    into grid coordiantes x and y.

    Args:
        phi (tuple): geodetic latitude in degrees, minutes and seconds, positive north
        lam (tuple): geodetic longitude in degrees, minutes and seconds, positive east
        ellips (str): ellipsiod, e.g. 'GRS1980'
        projection (str): projection, e.g. 'SWEREF99TM'

    Returns:
        tuple[float, float]: grid x, grid y
    """
    phi = degr_min_sec_to_decimal_degr(phi)
    lam = degr_min_sec_to_decimal_degr(lam)

    # Angles need to be expressed as radians
    phi = degr_to_radians(phi)
    lam = degr_to_radians(lam)

    a, f = get_ellipsoidal_parameters(ellips)
    e, n, a_hat = from_ellipsoidal_parameters(a, f)
    lam0, k0, FN, FE = get_transverse_mercator_parameters(projection)

    A = e**2
    B = (1 / 6) * (5 * e**4 - e**6)
    C = (1 / 120) * (104 * e**6 - 45 * e**8)
    D = (1 / 1260) * (1237 * e**8)

    sin_2 = np.power(np.sin(phi), 2)
    sin_4 = np.power(np.sin(phi), 4)
    sin_6 = np.power(np.sin(phi), 6)
    phi_star = phi - np.sin(phi) * np.cos(phi) * (A + B * sin_2 + C * sin_4 + D * sin_6)

    delta_lambda = lam - lam0
    epislon = np.arctan(np.tan(phi_star) / np.cos(delta_lambda))
    new = np.arctanh(np.cos(phi_star) * np.sin(delta_lambda))

    b1 = (1 / 2) * n - (2 / 3) * n**2 + (5 / 16) * n**3 + (41 / 180) * n**4
    b2 = (13 / 48) * n**2 - (3 / 5) * n**3 + (557 / 1440) * n**4
    b3 = (61 / 240) * n**3 - (103 / 140) * n**4
    b4 = (49561 / 161280) * n**4

    x = (
        k0
        * a_hat
        * (
            epislon
            + b1 * np.sin(2 * epislon) * np.cosh(2 * new)
            + b2 * np.sin(4 * epislon) * np.cosh(4 * new)
            + b3 * np.sin(6 * epislon) * np.cosh(6 * new)
            + b4 * np.sin(8 * epislon) * np.cosh(8 * new)
        )
        + FN
    )

    y = (
        k0
        * a_hat
        * (
            new
            + b1 * np.cos(2 * epislon) * np.sinh(2 * new)
            + b2 * np.cos(4 * epislon) * np.sinh(4 * new)
            + b3 * np.cos(6 * epislon) * np.sinh(6 * new)
            + b4 * np.cos(8 * epislon) * np.sinh(8 * new)
        )
        + FE
    )

    return x, y
