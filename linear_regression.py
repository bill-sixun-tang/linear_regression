### Tools for linear regression ###
# Jiahao

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm



def simulate_data(beta,n):
    """
    Simulates data for testing linear_regression models.
    INPUT
        nobs (int) the number of observations in the dataset
    RETURNS
        data (dict) contains X, y, and beta vectors.
    """
    x = np.random.randn(1,n)

    epsilon = np.random.randn(1,n)

    a = beta[0]
    b = beta[1]

    y = a + b*x + epsilon 

    output = {'x':list(x[0]),'y':list(y[0]),'beta':beta}

    return output


def compare_models(x,y):
    """
    Compares output from different implementations of OLS.
    INPUT
        X (ndarray) the independent variables in matrix form
        y (array) the response variables vector
    RETURNS
        results (pandas.DataFrame) of estimated beta coefficients
    """
    results = sm.OLS(y,x).fit()
    return pd.DataFrame(results.params)

def load_hospital_data(path_to_data):
    """
    Loads the hospital charges data set found at data.gov.
    INPUT
        path_to_data (str) indicates the filepath to the hospital charge data (csv)
    RETURNS
        clean_df (pandas.DataFrame) containing the cleaned and formatted dataset for regression
    """
    data = pd.read_csv(path_to_data)
    return data

    pass


def prepare_data(hospi_data):
    """
    Prepares hospital data for regression (basically turns df into X and y).
    INPUT
        df (pandas.DataFrame) the hospital dataset
    RETURNS
        data (dict) containing X design matrix and y response variable
    """
    

    pass


def run_hospital_regression():
    """
    Loads hospital charge data and runs OLS on it.
    INPUT
        path_to_data (str) filepath of the csv file
    RETURNS
        results (str) the statsmodels regression output
    """
    pass
 

### END ###


