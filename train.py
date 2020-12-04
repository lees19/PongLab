import pandas as pd 

df = pd.read_csv("pong_data.csv")

Xtrain = df.drop('paddle_y', axis = 1)
ytrain = df['paddle_y']

from sklearn.neural_network import MLPRegressor
model = MLPRegressor(random_state=1, max_iter=1000).fit(Xtrain, ytrain)

from joblib import dump, load 
dump(model, 'mymodel.joblib') #save
#model2 = load('mymodel.joblib')  load