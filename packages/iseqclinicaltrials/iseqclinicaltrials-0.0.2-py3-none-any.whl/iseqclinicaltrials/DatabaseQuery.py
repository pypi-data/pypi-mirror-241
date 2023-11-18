import sqlite3
from sqlalchemy import create_engine, text, TextClause
import pandas as pd


class DatabaseQuery:
    def __init__(self, db_path, table="researches"):
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self.table = table

    def _query(
        self, query_str: TextClause, index_col="index", params={}
    ) -> pd.DataFrame:
        with self.engine.connect() as con:
            return pd.read_sql(query_str, con=con, index_col=index_col, params=params)

    def _get_unique_diseases(self) -> pd.DataFrame:
        unique_diseases_query_str = """SELECT DISTINCT disease
                                                FROM researches"""
        return self._query(unique_diseases_query_str, index_col=None)

    def _get_unique_terms(self) -> pd.DataFrame:
        unique_terms_query_str = """SELECT DISTINCT term
                                                FROM researches"""
        return self._query(unique_terms_query_str, index_col=None)

    def get_all_records(self, limit) -> dict:
        unique_diseases = self._get_unique_diseases()
        unique_terms = self._get_unique_terms()

        unique_diseases = unique_diseases["disease"].tolist()
        unique_terms = unique_terms["term"].tolist()

        results = dict()

        for disease in unique_diseases:
            for term in unique_terms:
                params = {
                    "disease": disease,
                    "term": term,
                    "limit": limit,
                }

                query_str = text(
                    """SELECT * FROM researches
                        WHERE disease=:disease 
                        AND term=:term
                        LIMIT :limit"""
                )

                result = self._query(query_str, params=params)
                keyname = f"{disease}_{term}"
                results[keyname] = result

        return results

    def get_specific_records(self, disease: str, term: str, limit: int) -> pd.DataFrame:
        params = {
            "disease": disease,
            "term": term,
            "limit": limit,
        }

        query_str = text(
            """SELECT * FROM researches
                        WHERE disease=:disease 
                        AND term=:term
                        LIMIT :limit"""
        )

        return self._query(query_str, params)

    # def get_all_records_deprecated(self, disease: str, term: str) -> pd.DataFrame:
    #     params = {
    #         "disease": disease,
    #         "term": f"%{term}%",
    #     }
    #     query_str = text(
    #         f"""SELECT * FROM researches
    #                      WHERE disease=:disease
    #                      AND (study_title LIKE :term
    #                      OR conditions LIKE :term)"""
    #     )
    #     return self._query(query_str, params)

    # def get_top_20_records_deprecated(self, disease: str, term: str) -> pd.DataFrame:
    #     params = {
    #         "disease": disease,
    #         "term": f"%{term}%",
    #     }

    #     query_str = text(
    #         f"""SELECT * FROM researches
    #                      WHERE disease=:disease
    #                      AND (study_title LIKE :term
    #                      OR conditions LIKE :term)
    #                      LIMIT 20"""
    #     )

    #     return self._query(query_str, params)
