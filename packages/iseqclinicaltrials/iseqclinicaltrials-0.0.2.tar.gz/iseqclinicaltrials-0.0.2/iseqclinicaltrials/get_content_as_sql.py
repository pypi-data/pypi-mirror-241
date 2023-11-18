#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from iseqclinicaltrials.ContentGetter import ContentGetter
from iseqclinicaltrials.StudiesFilter import StudiesFilter
from iseqclinicaltrials.DatabaseInitializer import DatabaseInitializer
import argparse
import pandas as pd

__version__ = "0.0.1"


def args_parser_init() -> argparse.Namespace:
    """Get user inputs"""
    parser = argparse.ArgumentParser(
        description="A tool for quering and filtering clinicaltrials.gov",
    )
    parser.add_argument(
        "-d",
        "--diseases-file",
        type=str,
        help="The condition or disease according to clinicaltrials.gov passed as a comma separated list in a file",
    )
    parser.add_argument(
        "-o",
        "--other-terms-file",
        type=str,
        help="The other terms according to clinicaltrials.gov passed as a comma separated list in a file",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s {}".format(__version__)
    )
    args = parser.parse_args()
    return args


def get_csv_list_from_file(csv_list_file: str) -> list:
    with open(csv_list_file, "r") as f:
        content = f.read()
        content_list = content.split(",")

        return content_list


def get_and_format_diseases(args: argparse.Namespace) -> list:
    diseases = get_csv_list_from_file(args.diseases_file)

    return [disease.strip().lower() for disease in diseases]


def main():
    args = args_parser_init()

    final_df = pd.DataFrame()
    diseases = get_and_format_diseases(args)
    print(args.other_terms_file)
    other_terms = get_csv_list_from_file(args.other_terms_file)

    print(
        f"""Started clinicaltrials based database initialization using diseases: {diseases}
and other terms: {other_terms}"""
    )

    for disease in diseases:
        for term in other_terms:
            cg = ContentGetter(disease, term)
            df = cg.get_all_content_into_dataframe()

            sf = StudiesFilter(df)
            df = sf.filter_df()
            final_df = pd.concat([final_df, df])

    final_df = final_df.reset_index(drop=True)
    db_initializer = DatabaseInitializer(final_df)

    print(f"Database initialization completed with {diseases} and {other_terms}")


if __name__ == "__main__":
    main()
