import pandas as pd
import yaml

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from os import getcwd

class RDSDatabaseConnector:
    def __init__(self, configuration_file_name: str):
        self.db_creds = self.read_credentials(configuration_file_name)
        pass

    def read_credentials(self, filename: str):
        with open(f"{filename}.yaml") as file:
            credentials = yaml.safe_load(file)

        return credentials

    def initialise_database_engine(self):
        DATABASE_TYPE = self.db_creds['DATABASE_TYPE']
        DBAPI = self.db_creds['DBAPI']
        USER = self.db_creds['RDS_USER']
        PASSWORD = self.db_creds['RDS_PASSWORD']
        HOST = self.db_creds['RDS_HOST']
        PORT = self.db_creds['RDS_PORT']
        DATABASE = self.db_creds['RDS_DATABASE']

        database_engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        )
        return database_engine

    def extract_from_source_database(self, engine_object: Engine, table_name: str):
        source_dataframe = pd.read_sql_table(table_name, engine_object)

        return source_dataframe

    def dataframe_to_csv(self, dataframe: pd.DataFrame, csv_filename: str):
        csv_dataframe = dataframe.to_csv(csv_filename)
        print(f"{csv_filename} saved to {getcwd()}")
        return csv_dataframe


if __name__ == "__main__":
    connector = RDSDatabaseConnector("credentials")
    source_engine = connector.initialise_database_engine()
    finance_df = connector.extract_from_source_database(source_engine, "failure_data")
    finance_csv = connector.dataframe_to_csv(finance_df, "failure_data.csv")
