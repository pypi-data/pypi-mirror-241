import pandas as pd
import sqlite3
from sqlalchemy import create_engine, text


class DatabaseInitializer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.engine = create_engine("sqlite:///clinicaltrials.db", echo=False)
        self.df.to_sql("researches", con=self.engine, if_exists="replace")
