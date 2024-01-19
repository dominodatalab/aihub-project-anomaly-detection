import unittest
import os
import importlib.util

class TestAnomalyDetectionTSData(unittest.TestCase):

    def test_library_numpy_installed(self):
        """ Test if numpy library is installed """
        numpy_installed = importlib.util.find_spec("numpy") is not None
        self.assertTrue(numpy_installed, "numpy library is not installed")

    def test_library_pandas_installed(self):
        """ Test if pandas library is installed """
        pandas_installed = importlib.util.find_spec("pandas") is not None
        self.assertTrue(pandas_installed, "pandas library is not installed")
        
    def test_library_sklearn_installed(self):
        """ Test if sklearn library is installed """
        sklearn_installed = importlib.util.find_spec("sklearn") is not None
        self.assertTrue(sklearn_installed, "sklearn library is not installed")
        
    def test_library_seaborn_installed(self):
        """ Test if seaborn library is installed """
        seaborn_installed = importlib.util.find_spec("seaborn") is not None
        self.assertTrue(seaborn_installed, "seaborn library is not installed")
        
    def test_library_pandas_installed(self):
        """ Test if matplotlib library is installed """
        matplotlib_installed = importlib.util.find_spec("matplotlib") is not None
        self.assertTrue(matplotlib_installed, "matplotlib library is not installed")

    def test_csv_file_exists(self):
        """ Test if the csv data file exists """
        data_file_path = '/mnt/code/cpu_util.csv'
        self.assertTrue(os.path.isfile(data_file_path), "csv data file does not exist")

if __name__ == '__main__':
    unittest.main()
