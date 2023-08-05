import numpy as np

class DataNormalizer(object):
    """
        Creates an object that normalizes data.
        
        Args:
            data: The data that shpuld be normalized as a numpy array. 
    """
    
    def __init__(self, data):
        self.data=data
        
        
    def minmax(self):
        """
            Normalizes the data into a range between 0 and 1 using min-max normalization. 
    
            Returns:
                normalized_data: The normalized data.
        """
        normalized_data = (self.data - np.abs(self.data).min(axis=0)) / (np.abs(self.data).max(axis=0)-np.abs(self.data).min(axis=0))
        return normalized_data

    def zscore(self):
        """
            Normalizes the data using z-score normalization. 
    
            Returns:
                normalized_data: The normalized data.
        """
        normalized_data = (self.data - self.data.mean(axis=0)) / self.data.std(axis=0)
        return normalized_data