import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import warnings
warnings.filterwarnings('ignore')

#############################################################################################
data = pd.read_csv("IMPIMPIMP2.csv")
#############################################################################################
from sklearn.model_selection import train_test_split
predictors = data[['pH','E.C.','O.C.','CaCO3','N','P','K','Ca','Mg','S','Fe','Mn','Zn','Cu','B']]
target = data["target"]
#############################################################################################
X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=50)
print("Training features have {0} records and Testing features have {1} records.".\
format(X_train.shape[0], X_test.shape[0]))
#############################################################################################

print()

#svm
from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
print(X_test)
#print(X_test.loc[418])
#print(X_test.loc[477])
def callme(X):
    #X=[[7.79,0.21,0.58,6.60,225.79,10.92,347.20,21.93,11.24,17.13,3.37,3.35,0.50,3.26,0.44]]
    soil_value=clf.predict(X)
    if soil_value == [0]:
        return("Black soil")
    elif soil_value == [1]:
        return("Red soil")
    elif soil_value==[2]:
        return("Alluvial Soil")
    elif soil_value==[3]:
        return("Laterite Soil")
    elif soil_value==[4]:
        return("Shallow Soil")
    elif soil_value==[5]:
        return("MB soil")
    #print("The predicted Soil",soil_value)
    
    return (clf.predict(X))
#print(y_pred)
score_svm = round(accuracy_score(y_pred,Y_test)*100,2)
print("The accuracy score achieved using SVM is: "+str(score_svm)+" %")

cm = confusion_matrix(Y_test, y_pred)
print(cm)
print('Accuracy Rate: {}'.format(np.mean(y_pred == Y_test)))
print('Misclassification Rate: {}'.format(np.mean(y_pred != Y_test)))
#############################################################################################
print()
#############################################################################################










