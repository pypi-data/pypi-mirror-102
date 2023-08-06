from pycaret.datasets import get_data
class AutoML:
    """
    Performs Auto-mated machine learning 
    """
    def __init__(self,dataframe=None,csv=None):
        self.dataframe=dataframe
        if(csv!=None):
            self.csv=csv
    
    def data(self,dataset):
        get_data(dataset)
        
# df=AutoML()
# df.data("diabetes")    