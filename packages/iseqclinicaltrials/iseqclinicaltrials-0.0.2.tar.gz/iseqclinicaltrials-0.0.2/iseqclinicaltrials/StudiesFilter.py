import pandas as pd
import numpy as np
import os


def filter_locations_into_countries(locations):
    countries = set()
    for location in locations.split("|"):
        detail_loc = location.split(",")
        country = detail_loc[-1]
        country = country.strip()
        countries.add(country)
    return ",".join(countries)


class StudiesFilter:
    def __init__(
        self,
        df: pd.DataFrame,
        min_phase=2,
        is_filter_country=True,
        countries_filepath="resources/asian_countries.txt",
    ) -> None:
        self.df = df
        self.min_phase = min_phase
        self.is_filter_country = is_filter_country
        self.countries_filepath = countries_filepath

    def _filter_nan_or_empty(self):
        self.df = self.df.replace(r"^\s*$", np.nan, regex=True)
        self.df = self.df.dropna()

    def _filter_phases(self):
        """We take at least 2nd phase (due to recruitment)"""
        self.df["phases"] = self.df["phases"].astype(str)
        condition = self.df["phases"].str[-1].astype(int) >= 2
        self.df = self.df[condition]

    def _filter_drugs(self):
        """We take drugs only"""
        self.df["interventions"] = self.df["interventions"].astype(str)
        self.df["interventions"] = self.df["interventions"].str.split("|")
        self.df["interventions"] = self.df["interventions"].apply(
            lambda row: [
                intervention.split("DRUG: ", maxsplit=1)[1]
                for intervention in row
                if intervention.startswith("DRUG: ")
            ]
        )
        self.df["interventions"] = self.df["interventions"].apply(
            lambda row: "|".join([intervention for intervention in row])
        )

        self.df = self.df.rename(columns={"interventions": "drugs"})

    def _filter_country(self):
        """Client wanted to remove Asian records; it's based on countries (you cannot remove continent per name, need to use countries instead)"""
        base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
        full_path = os.path.join(base_dir, self.countries_filepath)
        self.df["locations"] = self.df["locations"].astype(str)

        with open(full_path, "r") as countries_file:
            countries = countries_file.read().splitlines()
            self.df["countries"] = self.df["locations"].apply(
                filter_locations_into_countries
            )

            self.df["countries"] = self.df["countries"].astype(str)
            self.df = self.df[~self.df["countries"].str.contains("|".join(countries))]

    def filter_df(self):
        self._filter_nan_or_empty()
        self._filter_phases()
        self._filter_drugs()
        if self.is_filter_country:
            self._filter_country()
        return self.df
