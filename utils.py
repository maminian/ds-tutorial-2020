def load_iris(datafolder='./datasets/'):
    '''
    Load the "iris" dataset; taking flower properties
    and a label of the type of flower. The goal is to
    predict the type of flower given the combination of measurements.

    Showcasing a somewhat "manual" way to load data here.

    Output:
        data: Data array of floats (numbers) of shape 150 (datapoints) by 4 (flower attributes)
        labels: array of strings (words) of shape 150 describing the type of flower.
    '''
    import csv  # built-in package for reading "nice" data
    import numpy as np

    with open(datafolder+'bezdekIris.data', 'r') as f:
        csvr = csv.reader(f)
        rows = list(csvr)
    #
    rows = rows[:-1]    # skip last (blank) row; after-the-fact observation.
    data = np.array([ r[:4] for r in rows], dtype=float)
    labels = np.array([r[-1] for r in rows])

    return data,labels
#

###################

def load_white_wine(datafolder='./datasets/'):
    '''
    Load the white wine portion of the wine quality dataset.
    This time, we return a pandas dataframe -- a fancy tool
    for working with table-like data. I don't use most of its tools;
    mainly its data reading functionality.

    Outputs:
        df : pandas dataframe of shape 4898 (datapoints) by 12 (data/attributes)
    '''
    import pandas
    df = pandas.read_csv(datafolder+'winequality-white.csv', delimiter=';')
    return df
#

def load_red_wine(datafolder='./datasets/'):
    '''
    Load the red wine portion of the wine quality dataset.
    This time, we return a pandas dataframe -- a fancy tool
    for working with table-like data. I don't use most of its tools;
    mainly its data reading functionality.

    Outputs:
        df : pandas dataframe of shape 1599 (datapoints) by 12 (data/attributes)
    '''
    import pandas
    df = pandas.read_csv(datafolder+'winequality-red.csv', delimiter=';')
    return df
#

def load_wine(datafolder='./datasets/'):
    '''
    Load the combined set of red and white wine for analysis.
    Again, a pandas dataframe is returned, but a new column is added
    describing the type of wine; df['type'] is either 'red' or 'white'.

    Outputs:
        df : pandas dataframe of shape 6497 (datapoints) by 13 (data/attributes)
    '''
    df_r = load_red_wine(datafolder=datafolder)
    df_w = load_white_wine(datafolder=datafolder)
    # add type of wine then concatenate.
    df_r['type'] = 'red'
    df_w['type'] = 'white'

    df = df_r.append(df_w)
    return df
#

###################

def load_biorxiv(datafolder='./datasets/'):
    pass
