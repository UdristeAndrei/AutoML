import pandas as pd


class automML():
    def __init__(self, data: pd.DataFrame = None):
        '''Automated Machine Learning data processing class
        Args:
            data (pd.DataFrame): Data to be processed, default is None
        '''
        if (not isinstance(data, pd.DataFrame)) and (data is not None):
            raise ValueError("Data must be a pandas DataFrame")
        
        self.data = data


    def load_data(self, path: str):
        '''Load data into the class
        Args:
            path (str): Path to the csv file
        '''
        if not isinstance(path, str):
            raise ValueError("Path must be a string")
        
        self.data = pd.read_csv(path)