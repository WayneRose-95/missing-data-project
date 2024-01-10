import pandas as pd 
import plotly.express as px 
import seaborn as sns 

from pandas import DataFrame 
from missingno import matrix 


class Graphs:

    def __init__(self):
        pass

    def data_to_dataframe(self, file_name : str):
        '''
        Method to read in data into a dataframe from a source .csv file 

        Parameters: 

        file_name : str 

        The name of the file to be read into a pandas dataframe 

        Returns: 

        df : DataFrame 

        A pandas dataframe object 

        '''

        df = pd.read_csv(file_name)

        return df 

    def create_matrix(self, dataframe : DataFrame):
        '''
        Creates a matrix given a pandas dataframe 

        Parameters: 

        dataframe : DataFrame 

        A pandas dataframe 

        '''
        matrix_plot = matrix(dataframe)
        
        

    def plot_graph(self, dataframe : DataFrame, x_column_title : str, y_column_title, title : str, graph_type : str = 'scatter' or 'line'):
        '''
        Plots a line graph given two column names of a pandas dataframe 

        Parameters: 

        dataframe : DataFrame 

        A pandas dataframe object 

        x_column_title : str 

        The title of what will be on the horizontal axis 

        y_column_title : str 

        The title of what will be on the vertical axis 

        title : str 

        The name of the graph 

        Returns: 

        graph : Figure 

        The graph itself. 
        '''

        if not graph_type:
            print('Invalid graph type selected only scatter and line are supported')
            raise ValueError 
        
        if graph_type == 'line':
            graph = px.line(dataframe, x=x_column_title, y=y_column_title, title=title)
            graph.show() 
            return graph
        
        elif graph_type == 'scatter':
            graph = px.scatter(dataframe, x=x_column_title, y=y_column_title, title=title)
            graph.show() 
            return graph

       

