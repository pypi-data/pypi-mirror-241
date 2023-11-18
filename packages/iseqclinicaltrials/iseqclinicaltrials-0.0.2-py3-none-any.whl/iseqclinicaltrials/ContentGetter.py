import requests
import pandas as pd
from io import StringIO
import time


class ContentGetter:
    def __init__(
        self,
        disease,
        term,
        endpoint="https://clinicaltrials.gov/api/v2/studies",
        format="csv",
        overall_status="NOT_YET_RECRUITING,RECRUITING",
        advanced="AREA[InterventionType]DRUG",
        fields="NCT Number,Study Title,Conditions,Interventions,Phases,Start Date,Study Status,Locations",
        sort="StartDate",
        page_size=1000,
    ):
        self._disease = disease
        self._term = term
        self.endpoint = endpoint
        self._params = {
            "format": format,
            "query.cond": disease,
            "query.term": term,
            "filter.overallStatus": overall_status,
            "filter.advanced": advanced,
            "fields": fields,
            "sort": sort,
            "pageSize": page_size,
        }
        self._request = requests.get(self.endpoint, params=self._params)

    def _get_records_dataframe(self, column_names=None):
        raw_data = self._request.content.decode("utf-8")
        data = StringIO(raw_data)

        return (
            pd.read_csv(data, sep=",")
            if not column_names
            else pd.read_csv(data, sep=",", names=column_names)
        )

    def get_all_content_into_dataframe(self) -> pd.DataFrame:
        """To iterate through all pages and gather records into dataframe"""
        return_df = self._get_records_dataframe()
        column_names = return_df.columns.values.tolist()

        while "x-next-page-token" in self._request.headers:
            time.sleep(5)
            self._params["pageToken"] = self._request.headers["x-next-page-token"]
            self._request = requests.get(self.endpoint, params=self._params)
            df = self._get_records_dataframe(column_names)
            return_df = pd.concat([return_df, df], ignore_index=True)

        return_df.columns = return_df.columns.str.replace(" ", "_")
        return_df.columns = return_df.columns.str.lower()

        return_df["disease"] = self._disease
        return_df["term"] = self._term
        time.sleep(5)

        return return_df
