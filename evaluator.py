import pandas as pd
import argparse
import sys
import numpy as np 

from joblib import dump, load

np.set_printoptions(threshold=sys.maxsize)



def evaluate_data(data=None):
    """
    input
    data - pandas dataframe of the farmers market dataset
    
    return 
    predicted labels
    """
    
    if data is None:
        print("You have not passed in data")
        return None
    
    features = ['state_nums', 'number of households', 'population', 'median family income', 
                'median household income', 'per capita income']
    data = data[features]
    rf_loaded = load("./models/random_forest_07102020.pkl")
    labels = rf_loaded.predict(data)
    return labels

def evaluate_dataframe(full_filepath):
    df = pd.read_csv(full_filepath)
    labels = evaluate_data(data=df)
    return labels

def main():
    parser = argparse.ArgumentParser(description='Predict labels on a Farmers Market csv file')
    parser.add_argument('-f', 
                        type=str,
                        help='full file path of Farmers Market csv')

    args = parser.parse_args()
    args = vars(args)
    labels = evaluate_dataframe(args['f'])
    print(labels)
    
    
if __name__=="__main__":
    main()
    
    