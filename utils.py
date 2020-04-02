def load_iris(datafolder='./datasets/'):
    '''
    Load the "iris" dataset; taking flower properties
    and a label of the type of flower. The goal is to
    predict the type of flower given the combination of measurements.

    Showcasing a somewhat "manual" way to load data here.

    Inputs:
        Required: none.
        *args: datafolder : a string, indicating the folder location
            where the data sits. It's expected the data can be accessed via
            loading the file datafolder + 'bezdekIris.data'.
            Default: './datasets/'

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

    Inputs:
        Required: none.
        *args: datafolder : a string, indicating the folder location
            where the data sits. It's expected the data can be accessed via
            loading the file datafolder + 'winequality-white.csv'.
            Default: './datasets/'

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

    Inputs:
        Required: none.
        *args: datafolder : a string, indicating the folder location
            where the data sits. It's expected the data can be accessed via
            loading the file datafolder + 'winequality-red.csv'.
            Default: './datasets/'

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

    Inputs:
        Required: none.
        *args: datafolder : a string, indicating the folder location
            where the data sits. It's expected the data can be accessed via
            loading the file datafolder + 'winequality-white.csv'
            AS WELL AS datafolder + 'winequality-red.csv'.
            Default: './datasets/'

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
    '''
    Loads a collection of preprints associated with coronaviruses,
    either directly or indirectly, from a dataset provided online recently
    in relation to COVID19/SARS-CoV-2.

    These papers aren't as "nice" to work with because they're papers,
    so we're not getting a nice matrix and labels out of this -- or a
    question to handle at all, for that matter. So instead, we're just
    returning a list of all the loaded papers to be looked at later.

    Inputs:
        Required: none.
        *args: datafolder : a string, indicating the folder location
            where the bioRxiv/medRxiv preprint FOLDER sits.
            It's expected the individual JSON files are located in
            datafolder + 'biorxiv_medrxiv/', for example
            './datasets/biorxiv_medrxiv/blahblah.json'
            Default: './datasets/'

    Outputs:
        preprints : Python list. Each entry is a dictionary (from a JSON file)
            corresponding to a paper, with various information attached;
            authors (?), institution(s) (?), along with the text of the paper
            itself.
    '''
    import glob
    import json

    # looking for anything with a "json" suffix; the "*" is a wildcard
    # which means "fill in the gap with literally anything, I don't care"
    files = glob.glob(datafolder+'biorxiv_medrxiv/*.json')

    # Let's not bother with the fancy python list-loop things here.
    preprints = []
    for j,fname in enumerate(files):
        # These are probably all nicely formatted, but I don't really trust
        # it 100%. "try" and "except" is my way of saying "just pretend
        # that didn't happen" if something goes wrong.
        try:
            with open(fname, 'rb') as f:
                paper = json.load(f)
            preprints.append( paper )
        except:
            print('Oh no, file %s failed to load.'%fname)
            continue
        #
        # fancy counter; print roughly every 5% of progress.
        if (j % (len(files)//20) ) == 0:
            print('%i of %i files read.'%(j+1,len(files)))
    #

    return preprints
#
