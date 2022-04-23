from Code import Code
from sklearn.model_selection import train_test_split
X,y = Code.preprocess()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)



