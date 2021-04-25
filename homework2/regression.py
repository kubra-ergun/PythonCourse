import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 

def regression(df):
    #dropping the missing values
    df.dropna(axis=0, how='any', inplace=True)
    
    y = np.array(df.iloc[:,2:3].values)
    x = df.iloc[:, 0:2]
    x = np.hstack([np.ones((len(x),1)), x])
    
    #regression formula: beta = (X'X)^-1X'y
    beta = np.linalg.inv(x.T@x)@x.T@y
    
    #for the error term
    n = len(y) # count of rows
    k = len(x[0]) # # count of columns
    e = y-(x@beta) 
    sigmasquare = (e.T@e)/(n-k-1)
    variance = sigmasquare * np.linalg.inv(x.T@x) #var = sigma^2 (X'X)^-1
    SE = np.sqrt(np.diag(variance)).reshape(3,1)    
    #for the confidence interval
    t = stats.t.ppf(.975, n-k-1) # two-tailed, alpha is 0.05
    upperbound = beta + SE*t
    lowerbound = beta - SE*t 
    CI = np.hstack([lowerbound, upperbound]) 
    
    #printing the regression results and plotting
    results = pd.DataFrame(np.hstack([beta,SE,CI]), 
                          columns=['Coefficient', 'Std. Err.', 'Lower Bound','Upper Bound'])
    results.rename(index={0: "_cons", 1: "arable_land", 2: "gdppc"}, inplace=True)
    print(results)
    
    plt.xlabel("Arable land")
    plt.ylabel("Net migration")
    plt.plot(df.iloc[:,0:1],y)
    # plt.plot(x,y) controlling for GDP per capita
