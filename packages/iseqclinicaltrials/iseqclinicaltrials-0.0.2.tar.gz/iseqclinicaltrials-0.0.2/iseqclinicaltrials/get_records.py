#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from iseqclinicaltrials.DatabaseQuery import DatabaseQuery
import argparse
import pandas as pd
import os

__version__ = "0.0.1"


def parser_init() -> argparse.ArgumentParser:
    """Get user inputs"""
    parser = argparse.ArgumentParser(
        description="A tool for quering clinicaltrials.gov local db",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        required=False,
        default=20,
        help="The limit of the results (default: 20)",
    )
    parser.add_argument(
        "-p",
        "--db-path",
        type=str,
        required=True,
        help="The path to the database (sqlite)",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    return parser


def get_all_records_args():
    parser = parser_init()
    parser.add_argument(
        "-s",
        "--split-into-files",
        action="store_true",
        help="Split the records into files (each file is the combination of limit, disease and other term)",
    )
    return parser.parse_args()


def get_specific_records_args():
    parser = parser_init()
    parser.add_argument(
        "-d",
        "--disease",
        type=str,
        required=False,
        help="The condition or disease according to clinicaltrials.gov",
    )
    parser.add_argument(
        "-t",
        "--other-term",
        type=str,
        required=False,
        help="Other term describing condition or disease in clinicaltrials.gov (for example ALK)",
    )
    return parser.parse_args()


def save_to_csv(result: pd.DataFrame, filename: str) -> None:
    return result.to_csv(
        filename,
        sep="\t",
        index=False,
    )


def get_all_records():
    args = get_all_records_args()
    db_query = DatabaseQuery(args.db_path)

    prefix = f"TOP_{args.limit}_"

    results = db_query.get_all_records(args.limit)

    if args.split_into_files:
        results_dir = "clinicaltrials_records"
        os.makedirs(results_dir, exist_ok=True)

        for keyname, result in results.items():
            if not result.empty:
                filename = f"{results_dir}/{prefix}{keyname}.csv"
                save_to_csv(result, filename)
    else:
        results_list = list()
        for keyname, result in results.items():
            if not result.empty:
                results_list.append(result)

        result_df = pd.concat(results_list, ignore_index=True)
        filename = f"{prefix}all_records.csv"

        save_to_csv(result_df, filename)


def get_specific_records():
    args = get_specific_records_args()
    db_query = DatabaseQuery(args.db_path)

    prefix = f"TOP_{args.limit}_"
    result = db_query.get_specific_records(
        args.disease.lower(), args.other_term, args.limit
    )
    filename = f"{prefix}{args.disease.lower().replace(' ', '_')}_{args.other_term}.csv"
    save_to_csv(result, filename)


if __name__ == "__main__":
    get_all_records()
