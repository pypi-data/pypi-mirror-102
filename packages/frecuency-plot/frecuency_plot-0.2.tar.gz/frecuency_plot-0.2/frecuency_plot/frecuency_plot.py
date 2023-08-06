import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


class Countplot():
    '''The Countplot class is used to visualize in a bar plot the frecuency 
    of occurrence of a unique value list contained in an list-like column
    
    Attributes:
        Color (string): the color of the bars in the plot
        N_bars (int): number of top values that appear in the plot
        Size (float array 2x1): size of the visualization
        Title (string): title of the plot
        Sep_type: separator between values in the original column
        data: a list-like column
        '''

    def __init__(self, data, color = 'cornflowerblue', n_bars = 10,
                 size = [11.69, 8.27], title = 'Frecuency of occurrence', sep_type = ';'):

        self.color = color
        self.size = size
        self.title = title
        self.n_bars = n_bars
        self.sep_type = sep_type
        self.data = data
        self.ratio = None
        self.split_array_like()
        self.calculate_percentage()



    def split_array_like (self):
        '''
        Method to separate all the single values in the array and append them
        to a list. It iterates trough all the rows in the data
        
        Args: 
            None
        
        Returns: 
            pandasseries: list of values
        '''


        #Order values by count, rename columns and split strings
        temp = self.data.value_counts().reset_index()
        temp.rename(columns = {'index': 'method',
                               'col_name':'count'}, inplace = True)
        temp['method'] = temp['method'].str.split(self.sep_type)

        #Create a list with all separated values
        val_list = []
        for i in range(temp.shape[0]):
            for j in temp['method'][i]:
                val_list.append(j)

        #Convert list to series
        series = pd.Series(val_list)

        return series


    def calculate_percentage(self):
        '''
        Method to calculate the frecuency of ocurrence of each unique value in
        a pandas series.
        
        Args: 
            None
        
        Returns: 
            pandasseries: frecuency of occurrence of each unique value
        '''

        #Calculate the unique value frecuency
        split = self.split_array_like ()
        self.ratio = split.value_counts()/self.data.shape[0]


    def barplot(self):
        '''
        

        Method to plot the frecuency of occurrence of each unique value
        -------
        Args: 
            None
        
        Returns: 
            ax object: bar plot of the ratio variable
        '''

        temp = self.ratio.head(self.n_bars)
        plt.figure(figsize = self.size)
        ax = sb.barplot(temp.values, temp.index, orient='h', color = self.color)
        plt.title(self.title, fontsize = 18, loc = 'left', pad = 20)


        #Remove plot frame
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

        #Draw y grid below the bars
        ax.set_axisbelow(True)
        ax.grid(axis='x')

        #Introducte percentages
        for p in ax.patches:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy()
            ax.annotate( f'{width:.1%}', (0.5*width, y + height/1.6),
                        ha='right')

        return ax