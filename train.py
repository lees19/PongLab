import pandas as pd 

df = pd.read_csv("pong_data.csv")

ytrain = df['paddle_y']
Xtrain = df.drop('paddle_y', axis = 1)

#you can change this to any regression
from sklearn.neural_network import MLPRegressor
model = MLPRegressor(random_state=1, max_iter=1000).fit(Xtrain, ytrain)

from joblib import dump, load 
dump(model, 'mymodel.joblib') #save
#model2 = load('mymodel.joblib')  #load