import os
import argparse
from lstpressure import LSTIntervalType as I, Observation
from lstpressure.lstcsv import LSTcsv
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "../../", "all_obs.csv")
output_path = os.path.join(script_dir, "../../", "output.csv")


def cli():
    parser = argparse.ArgumentParser(description="Run LST Calendar CLI")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    parser_observables = subparsers.add_parser(
        "observables", help="Description of observable commands"
    )

    parser_observables.add_argument(
        "--dt-start",
        type=str,
        default=datetime.today().strftime("%Y%m%d"),
        help="Start date in YYYYMMDD format",
    )
    parser_observables.add_argument(
        "--dt-end", type=str, default=argparse.SUPPRESS, help="End date in YYYYMMDD format"
    )
    parser_observables.add_argument(
        "--opt-csv", type=str, default=csv_path, help="Path to the OPT csv file"
    )
    parser_observables.add_argument(
        "--output", type=str, default=output_path, help="Path to the output csv file"
    )
    parser_observables.add_argument(
        "--filter",
        type=str,
        required=False,
        help="Select from: NIGHT, SUNRISE_SUNSET, ALL_DAY, SUNSET_SUNRISE, OBSERVATION_WINDOW",
    )

    args = parser.parse_args()

    filter_mapping = {
        I.NIGHT.name: I.NIGHT,
        I.SUNRISE_SUNSET.name: I.SUNRISE_SUNSET,
        I.ALL_DAY.name: I.ALL_DAY,
        I.SUNSET_SUNRISE.name: I.SUNSET_SUNRISE,
        I.OBSERVATION_WINDOW.name: I.OBSERVATION_WINDOW,
    }

    filter_default = I.NIGHT
    lst_interval = filter_mapping.get(args.filter, filter_default)
    dt_end = args.dt_end if "dt_end" in args else args.dt_start

    if args.command == "observables":

        def observation_filter(observation: Observation):
            if lst_interval in observation.utc_constraints:
                return True
            return False

        LSTcsv(args.opt_csv)
        LSTcsv(args.opt_csv, calendar_start=args.dt_start)
        LSTcsv(
            args.opt_csv,
            calendar_start=args.dt_start,
            calendar_end=dt_end,
            observation_filter=observation_filter,
        ).write_to_csv(args.output)

    else:
        print("Invalid command")
