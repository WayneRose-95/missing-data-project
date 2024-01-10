import unittest 

from db_utils import RDSDatabaseConnector

from pandas import DataFrame
from sqlalchemy.engine import Engine
from os import remove, path, getcwd 

class TestRDSDatabaseConnector(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        cls.file_name = 'credentials'
        cls.connector = RDSDatabaseConnector(cls.file_name)
        

    def test_read_credentials(self):

        test_creds = self.connector.read_credentials(self.file_name)

        self.assertIsInstance(test_creds, dict)
        

    def test_initialise_database_engine(self):
        test_engine = self.connector.initialise_database_engine()

        self.assertIsInstance(test_engine, Engine)
        

    def test_extract_from_source_database(self):

        test_engine = self.connector.initialise_database_engine()
        test_df = self.connector.extract_from_source_database(test_engine, 'failure_data')

        self.assertIsInstance(test_df, DataFrame)
       

    def test_dataframe_to_csv(self):
        test_engine = self.connector.initialise_database_engine()
        test_df = self.connector.extract_from_source_database(test_engine, 'failure_data')

        csv_file = self.connector.dataframe_to_csv(test_df, 'test_failure_data.csv')

        csv_file_directory = path.exists(getcwd())

        # Testing if the file pathway exists after the test
        self.assertTrue(csv_file_directory)



    @classmethod 
    def tearDownClass(cls) -> None:
        file_name = 'test_failure_data.csv'
        current_directory = getcwd()

        full_path = path.join(current_directory, file_name)
        remove(full_path)
        print("End of tests")
        


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)