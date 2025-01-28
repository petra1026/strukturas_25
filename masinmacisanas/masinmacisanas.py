import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl

# pip install -U scikit - learn
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression



#Modeļu analīze
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2


# datu sagatavošana

def sagatovot_datus(fails, kolonna_x, kolonna_y):
    datu_fails = pd.read_csv(fails)
    datu_fails.dropna(inplace=True)
    X_var = datu_fails[kolonna_x]
    Y_var = datu_fails[kolonna_y]
    X_train, x_test, Y_train, y_test = train_test_split(X_var, Y_var, test_size=0.2, random_state=0)
    return(X_train, x_test, Y_train, y_test)

def modela_kvalitate(y_test, results):
    print(cl(f"Dispersija: {evs(y_test, results)}", 'red', attrs=['bold']))
    print(cl(f"Kvadrātiskā novirze: {r2(y_test, results)}", 'red', attrs=['bold']))
    return

def trenet_modeli(modelis, X_train, Y_train, x_test):
    modelis.fit(X_train, Y_train)
    result=modelis.predict(x_test)
    return result