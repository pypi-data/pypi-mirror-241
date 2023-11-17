import argparse


def gen_args():
    parser = argparse.ArgumentParser(description="Gauss-Kreuger transformation.")
    parser.add_argument(
        "-p",
        "--phi",
        type=tuple_of_three_floats,
        help="Geodetic latitude in degrees, minutes and seconds.",
    )
    parser.add_argument(
        "-l",
        "--lam",
        type=tuple_of_three_floats,
        help="Geodetic longitude in degrees, minutes and seconds.",
    )
    parser.add_argument("--ellips", default="GRS1980", help="Ellipsiod, default is 'GRS1980'.")
    parser.add_argument(
        "--projection", default="SWEREF99TM", help="Projection, default is 'SWEREF99TM'."
    )
    args = parser.parse_args()
    return args


def tuple_of_three_floats(arg):
    try:
        values = [float(x) for x in arg.split(",")]
        if len(values) != 3:
            raise ValueError(
                "Input must be a tuple of three floats separated by commas"
            )
        return tuple(values)

    except ValueError as e:
        raise argparse.ArgumentTypeError(str(e))
